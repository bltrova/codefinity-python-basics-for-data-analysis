# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item in inventory:
    crt_stk, min_stk, rest_qty, sale_status = inventory[item]
    
    print(f"Processing {item}")
    
    while crt_stk < min_stk:
        crt_stk += rest_qty
        
    inventory[item][0] = crt_stk

    if crt_stk > discount_threshold and sale_status == False:
        inventory[item][3] = True
        
print("Processing completed")