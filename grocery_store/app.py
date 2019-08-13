FILENAME = './grocery_store/inventory.txt'
SALES_TAX = 0.07


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


def calc_sales_tax(untaxed_total):
    return SALES_TAX * untaxed_total


def save_inventory(filename, inventory):
    with open(filename, 'r') as file:
        header_line = file.readline()
        lines = file.readlines()

    new_inventory = header_line
    header_keys = header_line.split(',')
    line_keys = []
    for line in lines:
        code = line.split(',')[0].strip()
        line_keys.append(code)

    for code in line_keys:
        item = inventory.get(code)
        values = []
        for unformatted_key in header_keys:
            key = unformatted_key.strip()
            value = str(item.get(key))
            values.append(value)
        new_inventory += ', '.join(values) + '\n'

    with open(filename, 'w') as file:
        file.write(new_inventory)


def grocery_store():
    print('Welcome to our grocery store!\nPlease review our inventory and make your selection.')

    inventory = open_inventory(FILENAME)
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
    sales_tax = calc_sales_tax(untaxed_total)
    total_sale = untaxed_total + sales_tax
    receipt = '''
    TOTAL:   ${:.2f}
       cost: ${:.2f}
       tax:  ${:.2f}
    '''.format(total_sale, untaxed_total, sales_tax)
    print(receipt)

    save_inventory(FILENAME, inventory)


if __name__ == '__main__':
    grocery_store()
