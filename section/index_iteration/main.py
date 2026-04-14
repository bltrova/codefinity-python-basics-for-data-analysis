prices = [29.99, 45.50, 12.75, 38.20]

#discounts = 0.10, 0.20, 1.15, 5.

for i in range(len(prices)):
    if i == 0:
        prices[i] *= 0.90
    elif i == 1:
        prices[i] *= 0.80
    elif i == 2:
        prices[i] *= 0.85
    elif i == 3:
        prices[i] *= 0.95

    print(f"Updated price for item {i}: ${prices[i]:.2f} for each item.")
