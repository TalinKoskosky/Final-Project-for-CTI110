# P4LAB2
# Talin Koskosky
#11-3-24


def display_multiplication_table(number):
    # For loop to display the multiplication table from 1 to 12
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:

        #While loop to keep asking if the user wants to run the program again
        try:

            #Ask the user to enter an integer
            user_input = int(input("Enter an integer: "))

            if user_input >= 0:
                #Display the multiplication table if the integer is zero or higher
                display_multiplication_table(user_input)
            else:
                #Display an error message if the integer is negative
                print("The program cannot accept negative values.")

            #Ask the user if they want to run the program again
            run_again = input("Do you wish to run the program again? (yes or no): ").strip().lower()
            #use strip and lower so you can use any yes or no style
            if run_again != "yes":
                print("Thank you for using the program. Goodbye!")
                break
            #End the loop if the user types anything other than "yes"
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


main()
