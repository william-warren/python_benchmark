import json
import datetime

MENU_FILENAME = "./menu.json"
TRANSACTION_FILENAME = "./transactions.txt"


def get_menu():
    with open("./coffee_shop/menu.json") as reference:
        data = json.load(reference)
        return data


def print_menu(menu):
    options = []
    for item in menu:
        name = item.get("name")
        price = item.get("price")
        dots = (20 - len(name)) * "."
        options.append(f"{name}{dots}${price}")
    for item in options:
        print(item)


def get_choice(menu):
    options = []
    for item in menu:
        options.append(item.get("name").strip().lower())
    while True:
        choice = input("Which item would you like?")
        for item in options:
            if choice.lower().strip() == item:
                return choice


def checkout_message(menu, choice):
    for item in menu:
        if choice == item.get("name").lower().strip():
            total = round((item.get("price") * 1.07), 2)
            print(f"Here is your {choice}, your total is ${total}")


def log_transaction(menu, choice):
    for item in menu:
        if item.get("name").strip().lower() == choice:
            pretax = item.get("price")
            break
    tax = round((pretax * 0.07), 2)
    time = datetime.datetime.now()
    log = f"\n{time}, {choice}, {pretax}, {tax}"
    with open("./coffee_shop/transactions.txt", "a") as updated_log:
        updated_log.write(log)


def main():
    menu = get_menu()
    print_menu(menu)
    choice = get_choice(menu)
    checkout_message(menu, choice)
    log_transaction(menu, choice)


if __name__ == "__main__":
    main()
