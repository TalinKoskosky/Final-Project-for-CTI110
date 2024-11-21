# Talin Koskosky
# 11/16/2024
# P5LAB: Self-Checkout Change Dispersal
# This program simulates a self-checkout machine, calculates the change owed to a customer, and displays the breakdown of change into dollars, quarters, dimes, nickels, and pennies.

import random

# Function to calculate and display change
def disperse_change(change):
    # Convert the change to cents
    cents = int(round(change * 100))

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

    # If no change is needed
    if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        print("No change")

# Main function to control program flow
def main():
    # Generate a random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${amount_owed}")

    # Prompt the user to enter the amount paid
    amount_paid = float(input("Enter amount paid: $"))

    # Calculate the change owed
    if amount_paid < amount_owed:
        print("Insufficient payment. Please try again.")
    else:
        change = round(amount_paid - amount_owed, 2)
        print(f"Change owed: ${change}")
        # Call the disperse_change function to display change breakdown
        disperse_change(change)

# Call the main function
if __name__ == "__main__":
    main()
