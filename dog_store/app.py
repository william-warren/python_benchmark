from datetime import datetime

INVENTORY_FILENAME = "./inventory.txt"
TRANSACTION_FILENAME = "./transactions.txt"
SALES_TAX = 1.07


def load_menu():
    menu = []
    with open("./dog_store/inventory.txt") as reference:
        data = reference.readlines()
        data.pop(0)
        for item in data:
            info = item.split(",")
            item = info.pop(0)
            category = info.pop(0)
            size = info.pop(0)
            price = info.pop(0)
            quantity = info.pop(0)
            menu.append(
                {
                    "name": item,
                    "type": category,
                    "size": size,
                    "price": price,
                    "quantity": quantity,
                }
            )
    return menu


def show_menu(menu):
    for item in menu:
        name = item.get("name")
        category = item.get("type")
        size = item.get("size")
        price = item.get("price")
        quantity = item.get("quantity")
        dots = (6 + len(name)) * "."
        message = f"""
                {name}
        Price {dots} ${price[1:]}
        Type {dots + "."}{category}
        Size {dots + "."}{size}
        Quantity {dots[3:]}{quantity}
        """
        print(message)


def get_choice(menu):
    options = []
    for item in menu:
        options.append(item.get("name"))
    while True:
        choice = input("Which would you like to buy?").strip().lower()
        for item in options:
            if choice == item:
                return choice


def checkout_message(menu, choice):
    for item in menu:
        if item.get("name") == choice:
            total = str(round((float(item.get("price")) * 1.07), 2))
            print(
                f"What a great choice, your {choice} will be ${total[0:]}\nHave a nice day!"
            )


def log_transaction(menu, choice):
    time = datetime.now()
    for item in menu:
        if item["name"] == choice:
            pretax = float(item.get("price"))
            tax = round((float(pretax) * 0.07), 2)
            total = pretax + tax
    log = f"\n{time}, {pretax}, {tax}, {total}"
    with open("./dog_store/transactions.txt", "a") as updated_log:
        updated_log.write(log)


def dog_store():
    print("Welcome to the Dog Store! Woof!")
    menu = load_menu()
    show_menu(menu)
    choice = get_choice(menu)
    checkout_message(menu, choice)
    log_transaction(menu, choice)


if __name__ == "__main__":
    dog_store()
