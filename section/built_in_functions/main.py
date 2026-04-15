# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for item in products:
    price, qty_sold = products[item]
    price_flt = float(price)
    qty_sold_int = int(qty_sold)
    total = price_flt * qty_sold_int
    
    total_sales_list.append(price_flt * qty_sold_int)
    print(f"Total sales for {item}: ${total}")

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
#print(min_sales)
print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")
    