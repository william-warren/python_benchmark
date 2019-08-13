import json

DONUT_FILENAME = './donut_shop/donuts.json'


def open_donut_file(filename):
    with open(filename, 'r') as file:
        donut_dictionary = json.load(file)

    toppings = donut_dictionary.get('toppings')
    flavors = donut_dictionary.get('flavors')
    return toppings, flavors


def get_choice(options):
    while True:
        choice = input(' ? >>> ').strip().lower()
        if choice in options:
            return choice
        print('Sorry!', choice, 'is not an option')


def check_money(str_money):
    split_money = str_money.split('.')
    if len(split_money) != 2:
        return False
    dollars, cents = split_money[0], split_money[1]
    if dollars.isdigit() and cents.isdigit() and len(cents) == 2:
        return True
    return False


def get_money():
    while True:
        str_money = input('? >>> $').strip()
        if check_money(str_money):
            money = float(str_money)
            if money >= 1.00:
                return money
            else:
                print('Not enough money!')
        else:
            print('Please enter amount in 0.00 format!')


def donut_shop():
    toppings, flavors = open_donut_file(DONUT_FILENAME)
    print('''Hello! Welcome to the Donut Shop!
    
    All donuts are $1, cash only.
    
    Choose your topping and flavor! Or get a random flavor!
    ''')

    print('What topping would you like?')
    print(' | '.join(toppings))
    topping = get_choice(toppings)
    print('\nWhat flavor would you like?')
    print(' | '.join(flavors))
    flavor = get_choice(flavors)

    print('''
        Your order: donut with {} topping and {} flavored icing, great choice!
        Your total is $1.00
    How much are you paying with?''')
    cash_in = get_money()
    cash_out = cash_in - 1
    print(cash_in, cash_out)


if __name__ == '__main__':
    donut_shop()
