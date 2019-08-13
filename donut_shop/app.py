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


def donut_shop():
    toppings, flavors = open_donut_file(DONUT_FILENAME)
    print('''Hello! Welcome to the Donut Shop!
    
    All donuts are $1, cash only.
    
    Choose your topping and flavor! Or get a random flavor!
    ''')

    print('What topping would you like?')
    print(' | '.join(toppings))
    topping = get_choice(toppings)
    flavor = get_choice(flavors)


if __name__ == '__main__':
    donut_shop()
