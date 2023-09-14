import os.path
import pickle
import sqlite3

from Article import Article


class Inventory:
    def __init__(self, article_list):
        """
        Create a new Inventory
        :param article_list: the articles that you want to store in your inventory
        """
        self.article_list = article_list

    def __str__(self):
        """
        :return: a string representation with an overview of all the articles and quantities
        """
        rep = f"\n{'___---Inventory---___':^32}\n"
        for article in self.article_list:
            rep += str(self.article_list[article]) + "\n"
        if not self.article_list:
            rep += "Empty"
        return rep

    def add_new_article(self, code=None, name=None, quantity=None):
        """
        Add a new article to the list of articles
        :param code: optional code for the new article
        :param name: optional name for the new article
        :param quantity: optional quantity for the new article
        """
        if code:
            c = code
        else:
            c = input("Please provide a code for the new article: ")
        if name:
            n = name
        else:
            n = input("Please provide a name for the new article: ")
        if quantity and int(quantity) >= 0:
            q = int(quantity)
        else:
            q = input("Please provide a quantity for the new article: ")
        self.article_list[c] = Article(c, n, q)

    def add_new_transaction(self, article=None, quantity=None, action=None):
        """Start a new transaction for an article
        :param article: code of the article you want to transfer
        :param quantity: how many times you want to transfer this article
        :param action: direction of the transfer
        :return: a dictionary containing the transaction or cancelled if the transaction failed
        """
        ar, qu, ac = article, int(quantity), action
        while type(ar) != str or not ar:
            ar = input("Please provide the code of the article you want to transfer: ")
        while qu < 0 or not qu:
            qu = int(input("How many times should this article be transferred?: "))
        while ac != "Incoming" and ac != "Outgoing":
            ac = input('Is this transfer "Incoming" or "Outgoing"?: ')

        if self.article_list.get(ar):
            self.article_list[ar].incoming(
                qu
            ) if ac == "Incoming" else self.article_list[ar].outgoing(qu)
        elif ac == "Incoming":
            self.add_new_article(ar, quantity=qu)
        else:
            print(
                "Transfer: Article could not be transferred because it does not exist"
            )
            return "cancelled"
        return {"article": ar, "quantity": qu, "action": ac}

    def save_binary(self, file_path=None):
        """
        Saves the current inventory state in a binary file
        :param file_path: full path to the file
        :return: If the inventory was saved successfully
        """
        path = file_path
        if not file_path:
            path = (
                f"aufgabe/inventory_saves/{input('Please provide a name for you file: ')}.bin"
            )
        try:
            f = open(path, mode="wb")
            pickle.dump(self.article_list, f)
            f.close()
            return "Inventory saved successfully"
        except Exception as e:
            return e

    def save_csv(self, file_path=None):
        """
        Saves the current inventory state in a csv file
        :param file_path: full path to the file
        :return: If the inventory was saved successfully
        """
        path = file_path
        if not file_path:
            path = (
                f"aufgabe/inventory_saves/{input('Please provide a name for you file: ')}.csv"
            )
        try:
            f = open(path, mode="w")
            for article in self.article_list.values():
                f.write(f"\n{article.article_to_csv()}")
            f.close()
            return "Inventory saved successfully"
        except Exception as e:
            return e

    def save_db(self, file_path=None):
        """
        Saves the current inventory state in a sqlite database
        :param file_path: full path to the file
        :return: If the inventory was saved successfully
        """
        path = file_path
        if not path or not os.path.exists(path):
            path = f"aufgabe/inventory_saves/{input('Please provide a name for you database (example_db): ')}.db"
            if not os.path.exists(path):
                try:
                    db_connection = sqlite3.connect(path)
                    cursor = db_connection.cursor()
                    cursor.execute(
                        "CREATE TABLE articles("
                        "code TEXT PRIMARY KEY,"
                        "name TEXT,"
                        "quantity INTEGER)"
                    )
                    db_connection.commit()
                    db_connection.close()
                except Exception as e:
                    return e
        try:
            db_connection = sqlite3.connect(path)
            cursor = db_connection.cursor()
            for article in self.article_list:
                cursor.execute(
                    f"INSERT OR REPLACE INTO articles VALUES('{article}',"
                    f"'{self.article_list.get(article).name}',"
                    f"'{self.article_list.get(article).stock}')"
                )
            db_connection.commit()
            db_connection.close()
            return "Inventory saved successfully"
        except Exception as e:
            return e

    def load_binary(self, file_path=None):
        """
        Reads a saved inventory state from a binary file
        :param file_path: full path to the file
        :return: If the inventory was loaded successfully
        """
        path = file_path
        if not file_path:
            path = f"aufgabe/inventory_saves/{input('Please provide the file name (example_filename): ')}.bin"
        try:
            f = open(path, "rb")
            self.article_list = pickle.load(f)
            f.close()
            return "Inventory loaded successfully"
        except Exception as e:
            return e

    def load_csv(self, file_path=None):
        """
        Reads a saved inventory state from a csv file
        :param file_path: full path to the file
        :return: If the inventory was loaded successfully
        """
        path = file_path
        if not file_path:
            path = f"aufgabe/inventory_saves/{input('Please provide the file name (example_filename): ')}.csv"
        try:
            f = open(path, mode="r")
            content = f.read()
            lines = content.split(chr(10))
            for line in lines:
                if line:
                    s = line.split(";")
                    self.add_new_article(s[0], s[1], s[2])
            f.close()
            return "Inventory loaded successfully"
        except Exception as e:
            return e

    def load_db(self, file_path=None):
        """
        Reads a saved inventory state from a sqlite .db file
        :param file_path: full path to the file
        :return: If the inventory was loaded successfully
        """
        path = file_path
        while not path or not os.path.exists(path):
            try:
                path = f"aufgabe/inventory_saves/{input('Please provide the database name (example_db): ')}.db"
                db_connection = sqlite3.connect(path)
                cursor = db_connection.cursor()
                cursor.execute("SELECT * FROM articles")
                db_connection.commit()
                for data_tuple in cursor:
                    if data_tuple:
                        self.add_new_article(
                            data_tuple[0], data_tuple[1], data_tuple[2]
                        )
                db_connection.close()
                return "Inventory loaded successfully"
            except Exception as e:
                return e
