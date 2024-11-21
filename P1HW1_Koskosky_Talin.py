

#Talin Koskosky
#10-6-24
#P1HW1
#Using Input and Print functions

    # Function to calculate exponent
def calculate_exponent(base, exponent):
    result = base ** exponent
    print(f"-----Calculating Exponents----")
    print(f"Enter an integer as the base value: {base}")
    print(f"Enter an integer as the exponent: {exponent}")
    print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

    # Function to perform addition and subtraction
def add_and_subtract(starting_integer, add_value, subtract_value):
    result = starting_integer + add_value - subtract_value
    print(f"-----Addition and Subtraction----")
    print(f"Enter a starting integer: {starting_integer}")
    print(f"Enter an integer to add: {add_value}")
    print(f"Enter an integer to subtract: {subtract_value}")
    print(f"\n{starting_integer} + {add_value} - {subtract_value} is equal to {result}\n")

    # Main program
if __name__ == "__main__":
    # Input for exponentiation
    base_value = int(input("Enter the base integer: "))
    exponent_value = int(input("Enter the exponent integer: "))
    
    # Input for addition and subtraction
    start_value = int(input("Enter the starting integer: "))
    add_value = int(input("Enter the integer to add: "))
    subtract_value = int(input("Enter the integer to subtract: "))
    
    # Calculate and display the results
    calculate_exponent(base_value, exponent_value)
    add_and_subtract(start_value, add_value, subtract_value)
