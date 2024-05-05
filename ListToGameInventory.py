from InventoryVisualizer import visualize

def addToInventory(inventory, addedItems):
    inv = inventory
    
    for each in addedItems:
        inv.setdefault(each, 0)
        inv[each] += 1

    return inv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

visualize(inv)