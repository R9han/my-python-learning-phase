items = []
prices = []
total = 0 

while True:
    item = input("Enter a item to buy(q to 'quit'): ")
    if item.lower() == "q":
        break 
    else:
        price = float(input(f"Enter the price of {item}: $"))
        items.append(item)
        prices.append(price)

print("_______YOUR CART________")

for item in items:
    print(item, end= ", ")    

for price in prices:
    total += price 
print(f"\n your total price is: {total}")        