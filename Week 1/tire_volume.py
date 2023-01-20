import math
from datetime import datetime

w = int(input('Enter the width of the tire in mm (ex: 205): '))
a = int(input('Enter the aspect ratio of the tire (ex 60): '))
d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

v = (math.pi * w ** 2 * a * (w * a + 2540 * d)) / 10000000000

print(f"The approximate volume is {v:.2f} liters")

with open("volumes.txt", "at") as volumes_file:
    current_date_and_time = datetime.now()
    print("_/\_" * 15, file = volumes_file)
    print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v}", file = volumes_file)

answer = input("Would you like to receive a quote for your tire size?: ")

if answer == "yes":
    phone_number = input("Please enter your phone number: ")
    print("Thank you for your information! We will text you with a quote as soon as possible.")
    with open("volumes.txt", "at") as volumes_file:
        print(f"Customers phone number: {phone_number}", file = volumes_file)
        
elif answer == "no":
    print("Have a great day!")
else:
    print("Invalid input. Please enter yes or no.")
