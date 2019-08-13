def open_inventory(filename):
    with open(filename, 'r') as file:
        header = file.readline()
        body = file.readlines()

    header_keys = header.split(',')

    inventory = {}
    for i in range(len(body)):
        unformatted_item = body[i].split(',')
        item = {}
        for j in range(len(header_keys)):
            key = header_keys[j].strip()

            if key == 'price':
                val = float(unformatted_item[j].strip())
            elif key == 'quantity':
                val = int(unformatted_item[j].strip())
            else:
                val = unformatted_item[j].strip()
            item[key] = val
        inventory_key = item.get('code')
        inventory[inventory_key] = item

    return inventory


def print_inventory(inventory):
    for item in inventory.values():
        s = '''{} {}
        {}.
        Price: ${:.2f}\n'''.format(item['name'].title(), item['code'], item['description'].capitalize(), item['price'])
        print(s)


def get_choice(valid_keys):
    while True:
        choice = input('>>> ').strip()
        if choice in valid_keys or choice == 'q':
            return choice
        print('invalid choice')


def calculate_order(inventory, selections):
    untaxed_total = 0
    for code in selections:
        name = inventory[code].get('name')
        if inventory[code].get('quantity') > 0:
            inventory[code]['quantity'] -= 1
            price = inventory[code].get('price')
            untaxed_total += price
            line = '\t{} @ ${:.2f}'.format(name.upper(), price)
        else:
            line = '\t{} UNAVAILABLE'.format(name)
        print(line)

    return untaxed_total


def grocery_store():
    print('Welcome to our grocery store!\nPlease review our inventory and make your selection.')

    inventory = open_inventory('./grocery_store/inventory.txt')
    print_inventory(inventory)
    print('What would you like today? Select the code from above and enter q when you are done.')
    choice = ''
    selections = []
    while True:
        choice = get_choice(inventory.keys())
        if choice == 'q':
            break
        selections.append(choice)

    print('calculating order...')
    untaxed_total = calculate_order(inventory, selections)
    # sales_tax = calc_sales_tax(untaxed_total)


if __name__ == '__main__':
    grocery_store()
