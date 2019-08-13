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
            val = unformatted_item[j].strip()
            item[key] = val
        inventory_key = item.get('code')
        inventory[inventory_key] = item

    return inventory


def grocery_store():
    print('Welcome to our grocery store!\nPlease review our inventory and make your selection.')

    inventory = open_inventory('./grocery_store/inventory.txt')
    print(inventory)


if __name__ == '__main__':
    grocery_store()
