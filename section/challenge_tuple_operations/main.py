# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#Count
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")
#Find banana 1st Index
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")
#Check
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
#Count grapes
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")
#Check if oranges in the shelf
if "oranges" in shelf:
    print("Oranges are at index:", shelf.index("oranges"))
else:
    print("Oranges are out of stock.")
