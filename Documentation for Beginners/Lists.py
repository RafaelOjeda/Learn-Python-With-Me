# Lists store sets of information in one place.
# Stored in a variable
names = []

# Currently the list is empty but I can add items using append()
names.append("Rafael")
names.append("Carlos")
names.append("Ana")
names.append("Rachel")

# Shows the list names with all appeneded items 
print(names)

# Inserting adds items to a list in the index value that you wish. Shifting everything by one
names.insert(0, "Donald")
print(f"Adds {names[0]} to the list: {names}")

# The del statements can remove a specific item within a list
print(f"Deleted {names[0]}")
del names[0]

# The pop() method removes the last item in a list unless  the index value is stated within the method.
remove_name = names.pop(3)
print(f"User {remove_name} has been removed from the list")

# The .remove() method can remove an item using the specific value that the item contains rather than the index value
names.remove("Rafael")

# All items can be accessed individually using their corresponding index value
print(names[1]) # Prints second item in the names list

# Used in a string
print(f"Hello my name is {names[0]}.")

# To change a value treat it like a variable and equal it to the value you wish to have.
names[1] = "Miguel"

print(f"An item has been changed to {names[1]}: {names}")

