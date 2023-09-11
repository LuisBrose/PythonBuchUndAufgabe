class Article:
    def __init__(self, code=None, name=None, stock=0):
        """
        Create an Article
        :param code: a unique code used as an identifier
        :param name: the name of the article
        :param stock: how many articles are already stored the default is zero
        """
        self.code = code
        self.name = name
        self.stock = stock

    def __str__(self):
        return f"Article {self.name} ({self.code}) exists {self.stock} times"

    def incoming(self, quantity):
        """
        Adds the specified amount of these articles to the inventory
        :param quantity: how many articles are being added
        """
        self.stock += quantity

    def outgoing(self, quantity):
        """
        Tries to transfer a specified amount of these articles from the inventory
        :param quantity: how many articles you want
        :return: True if successful otherwise raises an Exception if the stock is too low
        """
        if self.stock - quantity > 0:
            self.stock -= quantity
        else:
            raise Exception(
                f"The article {self.name} could not be transferred {quantity} "
                f"times because there are only {self.stock} in stock"
            )

    def check_stock(self):
        """
        :return: the current stock for this article
        """
        return self.stock

    def article_to_csv(self):
        """
        :return: this article in csv format
        """
        return f"{self.code};{self.name};{self.stock}"

    @staticmethod
    def csv_to_article(csv):
        """Convert an article in csv format back to normal
        :param csv: the article in csv format
        :return: an article
        """
        split = str(csv).split(";")
        return Article(split[0], split[1], int(split[2]))
