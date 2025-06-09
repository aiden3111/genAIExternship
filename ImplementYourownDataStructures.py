inventory = {}
inventory["mango"] = (15, 3.0)
inventory["banana"] = (15, 3)
print(inventory)
del inventory["banana"]
print(inventory)
inventory["mango"] = (10, 4.0)
print(inventory)
print("\n")

print("Welcome to the Inventory Manager!")
print("Current inventory:")
del inventory["mango"]
inventory["apple"] = (10, 2.5)
inventory["banana"] = (20, 1.2)
for key, value in inventory.items():
    print("Item: " + str(key) + ", Quantity: " + str(value[0]) + ", Price: $" + str(value[1]))
print("Adding a new item: mango")
inventory["mango"] = (15, 3.0)
print("Updated inventory:")
for key, value in inventory.items():
    print("Item: " + str(key) + ", Quantity: " + str(value[0]) + ", Price: $" + str(value[1]))
total_value = 0
for key, value in inventory.items():
    total_value+=(value[0]*value[1])
print("Total value of inventory: $" + str(total_value)) 