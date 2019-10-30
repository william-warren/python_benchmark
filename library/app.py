import json
from datetime import datetime

BOOK_FILENAME = "./books.json"
LOG_FILENAME = "./log.txt"


def load_books():
    inventory = []
    with open(BOOK_FILENAME) as book_reference:
        inventory_file = json.load(book_reference)
        for dictionary in inventory_file:
            inventory_dict = inventory_file[f"{dictionary}"]
            for category in inventory_dict:
                inventory_list = inventory_dict[f"{category}"]
                for book_dict in inventory_list:
                    for key in book_dict:
                        book = book_dict[f"{key}"]
                    inventory.append(book)
    return inventory, inventory_file


def load_log():
    with open(LOG_FILENAME, "r") as log_reference:
        log = log_reference.readlines()
    return log


def selection_in(inventory):
    print("Here's the books we are missing")
    for book in inventory:
        if book["in-stock"] == False:
            r_numbers = book["class"].split(" ")
            r_num = r_numbers[-1]
            print(book["title"], "----", r_num)
    while True:
        choice = input("What book would you like to checkin? ").lower().strip()
        for book in inventory:
            r_numbers = book["class"].split(" ")
            r_num = r_numbers[-1]
            if choice == r_num.lower().strip() and book["in-stock"] == False:
                return book


def selection(inventory, action):
    print("Here's the books we have in stock.")
    for book in inventory:
        if book["in-stock"] == True:
            r_numbers = book["class"].split(" ")
            r_num = r_numbers[-1]
            print(book["title"], "----", r_num)
    while True:
        choice = input("What book would you like to checkout? ").lower().strip()
        for book in inventory:
            r_numbers = book["class"].split(" ")
            r_num = r_numbers[-1]
            if choice == r_num.lower().strip() and book["in-stock"] == True:
                return book


def file_management(inventory, inventory_file, action):
    now = datetime.now()
    if action == "in":
        choice_book = selection_in(inventory)
    elif action == "out":
        choice_book = selection_out(inventory)
    for category in inventory_file["books"]:
        inventory_list = inventory_file["books"][f"{category}"]
        for book in inventory_list:
            for key in book:
                if choice_book == book[f"{key}"]:
                    if action == "in":
                        book[f"{key}"]["in-stock"] = True
                        title = book[f"{key}"]["title"]
                        log_update = f"\n{now}, {category} {key}, CHECK IN, {title}"
                    elif action == "out":
                        book[f"{key}"]["in-stock"] = False
                        title = book[f"{key}"]["title"]
                        log_update = f"\n{now}, {category} {key}, CHECK OUT, {title}"
    with open(BOOK_FILENAME, "w") as update_file_books:
        json.dump(inventory_file, update_file_books)
    with open(LOG_FILENAME, "a") as update_file_log:
        update_file_log.write(log_update)


def action_selection():
    while True:
        action = input("Checking in or out a book? [in/out]").strip().lower()
        if action == "in":
            return "in"
        elif action == "out":
            return "out"
        print("Please choose a vilid action.")


def main():
    print("welcome to the middle-earth public library.".title())
    inventory, inventory_file = load_books()
    action = action_selection()
    file_management(inventory, inventory_file, action)


if __name__ == "__main__":
    main()
