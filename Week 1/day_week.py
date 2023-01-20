from datetime import datetime

current_date_time = datetime.now()

day = current_date_time.weekday()
day = 1
tax = .6
discount = .10

total = float(input("Please enter the subtotal: "))

if total >= 50 and (day == 1 or day == 2):
    discount_amount = total * discount
    print(f"Discount amount: {discount_amount:.2f}")
    total -= discount_amount

sales_tax = total * tax
print(f"Sales tax amount {sales_tax:.2f}")

print(f"Total {total:.2f}")