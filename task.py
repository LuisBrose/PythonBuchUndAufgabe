import sys

from Article import Article
from Inventory import Inventory


if __name__ == "__main__":
    company_inventory = Inventory({})

    print("___---Welcome to Inventory management---___\n")

    mode = input(
        f"Choose your Inventory management mode: \n"
        f"New empty Inventory: 0\n"
        f"New Inventory populated with demo data: 1\n"
        f"Load existing Inventory from csv file: 2\n"
        f"Load existing Inventory from binary file: 3\n"
        f"Exit Inventory management: 4\n"
        f"your choice: "
    )
    try:
        mode = int(mode)
    except ValueError as e:
        print(e)
    if mode == 0:
        pass
    elif mode == 1:
        pass
    elif mode == 2:
        print(company_inventory.load_csv())
    elif mode == 3:
        print(company_inventory.load_binary())
    else:
        sys.exit(0)

    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    )

    print("___---Welcome to Inventory management---___")
    article_dict = {
        "A123": Article("A123", "Screw"),
        "B456": Article("B456", "Hammer"),
        "C789": Article("C789", "Nut"),
    }

    if mode == 1:
        company_inventory = Inventory(article_dict)

    transactions = [
        {"article": "A123", "quantity": 10, "action": "Incoming"},
        {"article": "B456", "quantity": 5, "action": "Outgoing"},
        {"article": "A123", "quantity": 15, "action": "Outgoing"},
        {"article": "C789", "quantity": 8, "action": "Incoming"},
    ]

    if mode == 1:
        for transaction in transactions:
            try:
                print(
                    "Transfer: ",
                    company_inventory.add_new_transaction(
                        transaction["article"],
                        transaction["quantity"],
                        transaction["action"],
                    ),
                )
            except Exception as e:
                print(e)

    print(company_inventory)

    while True:
        choice = int(
            input(
                f"\n\n{'___---Menu---___':^30}\nWhat do you want to do next? \n\n"
                f"Create a new article : 0\n"
                f"Check stock of an article : 1\n"
                f"Transfer an article from the inventory : 2\n"
                f"Transfer an article to the inventory : 3\n"
                f"Display the whole inventory : 4\n"
                f"Save the current inventory in a csv file : 5\n"
                f"Save the current inventory in a binary file : 6\n"
                f"Exit the program : 7\n"
                f"\nchoose an action: "
            )
        )

        if choice == 0:
            company_inventory.add_new_article()
        elif choice == 1:
            print(
                company_inventory.article_list[
                    input("Code of the article you want to check: ")
                ].check_stock()
            )
        elif choice == 2:
            try:
                print(
                    "Transaction: ",
                    company_inventory.add_new_transaction(
                        input("Code of the article you want to transfer: "),
                        input("How many times you want to transfer this article: "),
                        "Outgoing",
                    ),
                )
            except Exception as e:
                print(e)
        elif choice == 3:
            print(
                "Transaction: ",
                company_inventory.add_new_transaction(
                    input("Code of the article you want to transfer: "),
                    input("How many times you want to transfer this article: "),
                    "Incoming",
                ),
            )
        elif choice == 4:
            print(company_inventory)
        elif choice == 5:
            print(company_inventory.save_csv())
        elif choice == 6:
            print(company_inventory.save_binary())
        else:
            sys.exit(0)
