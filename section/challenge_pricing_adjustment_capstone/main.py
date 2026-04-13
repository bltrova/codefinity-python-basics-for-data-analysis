grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

egg_price = grocery_inventory["Eggs"][1]
if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"][1] - 1
    cat, pr, stk = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (cat, pr -1, stk)
else:
    print("The price of Egg is reasonable")

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"][2] + 20
    category, price, stock = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (category, price, stock + 20)

else:
    print('Milk has sufficient stock')

apple_price = grocery_inventory["Apples"][1]
if apple_price > 2:
    del grocery_inventory["Apple"]
    print("Apples removed from inventory due to high price")

print("Updated inventory:", grocery_inventory)