# P3LAB
#Talin Koskosky
#10/26/2024
# Program to calculate change such as dollars, penny, etc 

# Get the amount of money from the user
amount = float(input("Enter Cash Amount: $"))

# Convert the amount to cents
cents = int(round(amount * 100))

# Calculate the number of dollars and remaining cents
dollars = cents // 100
cents %= 100

# Calculate the number of quarters and remaining cents
quarters = cents // 25
cents %= 25

# Calculate the number of dimes and remaining cents
dimes = cents // 10
cents %= 10

# Calculate the number of nickels and remaining cents
nickels = cents // 5
cents %= 5

# Remaining cents are pennies
pennies = cents

# Display the result
if dollars > 0:
    print(f"{dollars} Dollar" + ("s" if dollars > 1 else ""))
if quarters > 0:
    print(f"{quarters} Quarter" + ("s" if quarters > 1 else ""))
if dimes > 0:
    print(f"{dimes} Dime" + ("s" if dimes > 1 else ""))
if nickels > 0:
    print(f"{nickels} Nickel" + ("s" if nickels > 1 else ""))
if pennies > 0:
    print(f"{pennies} Penn" + ("y" if pennies == 1 else "ies"))
#Ask about a cleaner way to do pennies, hurts brain to look at. 

# If no change is needed
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change")
