age = int(input('Please enter your age: '))

max_rate = 220 - age

rate_1 = max_rate * .65
rate_2 = max_rate * .85

print("When exercising you should keep your heart rate between")
print(f"{rate_1:.0f} and {rate_2:.0f} beats per minute")