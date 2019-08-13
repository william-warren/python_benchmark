import json

DONUT_FILENAME = './donut_shop/donuts.json'


def open_donut_file(filename):
    with open(filename, 'r') as file:
        donut_dictionary = json.load(file)

    toppings = donut_dictionary.get('toppings')
    flavors = donut_dictionary.get('flavors')
    return toppings, flavors


def get_topping(toppings):
    while True:
        topping = input(' ? >>> ').strip().lower()
        if topping in toppings:
            return topping
        print('Sorry!', topping, 'is not an option')


def donut_shop():
    toppings, flavors = open_donut_file(DONUT_FILENAME)
    print('''Hello! Welcome to the Donut Shop!
    
    All donuts are $1, cash only.
    
    Choose your topping and flavor! Or get a random flavor!
    ''')

    print('What topping would you like?')
    print(' | '.join(toppings))
    topping = get_topping(toppings)


if __name__ == '__main__':
    donut_shop()
