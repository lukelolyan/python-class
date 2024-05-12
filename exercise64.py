total_cost = 0

while True:
    price = input("Enter the price of the item (or press Enter to finish): ")
    if price == "":
        break
    total_cost += float(price)

cash_payment = round(total_cost * 100) % 5
if cash_payment < 2.5:
    cash_payment = round(total_cost) - cash_payment / 100
else:
    cash_payment = round(total_cost) + (5 - cash_payment) / 100

print(f"Total cost of all items: ${total_cost:.2f}")
print(f"Amount due for cash payment: ${cash_payment:.2f}")
