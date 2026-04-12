grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

#retrieve details
bread_details = grocery_inventory.get("Bread")
print(f"Details of Bread: {bread_details}")
#add an item
grocery_inventory["Cookies"] = (143, "Bakery")
print(f"Inventory after adding Cookies: {grocery_inventory}")
#remove an item
grocery_inventory.pop("Eggs")
print(f"Inventory after removing Eggs: {grocery_inventory}")

print(f"Detais of Bread: {bread_details}")