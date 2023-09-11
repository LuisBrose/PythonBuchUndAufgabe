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
        return rep

    def add_new_article(self, code=None, name=None):
        """
        Add a new article to the list of articles
        :param code: optional code for the new article
        :param name: optional name for the new article
        """
        if code:
            c = code
        else:
            c = input("Please provide a code for the new article: ")
        if name:
            n = name
        else:
            n = input("Please provide a name for the new article: ")
        self.article_list[c] = Article(c, n)

    def add_new_transaction(self, article=None, quantity=None, action=None):
        """Start a new transaction for an article
        :param article: code of the article you want to transfer
        :param quantity: how many times you want to transfer this article
        :param action: direction of the transfer
        :return: a dictionary containing the transaction or False if the transaction failed
        """
        ar, qu, ac = article, int(quantity), action
        while type(ar) != str:
            if not ar:
                ar = input(
                    "Please provide the code of the article you want to transfer: "
                )
        while type(qu) != int and qu < 0:
            if not qu:
                qu = int(input("How many times should this article be transferred?: "))
        while ac != "Incoming" and ac != "Outgoing":
            ac = input('Is this transfer "Incoming" or "Outgoing"?: ')

        if self.article_list[ar]:
            self.article_list[ar].incoming(
                qu
            ) if ac == "Incoming" else self.article_list[ar].outgoing(qu)
        elif ac == "Incoming":
            self.add_new_article(ar)
        else:
            print("Transfer: Article could not be transferred because it does not exist")
            return False
        return {"article": ar, "quantity": qu, "action": ac}
