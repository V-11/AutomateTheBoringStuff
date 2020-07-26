def DisplayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total Items: ' + str(item_total))

def AddToInventory(inventory, added_items):
    for item in DragonLoot:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1

inventory = {'gold coin': 42, 'rope': 1}
DragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'torch', 'arrow', 'arrow', 'rope']

AddToInventory(inventory, DragonLoot)
DisplayInventory(inventory)
