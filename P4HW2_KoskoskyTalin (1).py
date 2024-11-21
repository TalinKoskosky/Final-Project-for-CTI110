# Talin Koskosky
# 11-10-24
# Assignment P4HW2
# This program calculates gross pay, overtime, and total payments for multiple employees
#"Finished" will end the program. 

# Pseudocode:
# 1. Initialize total counters for employees, overtime pay, regular pay, and gross pay.
# 2. Use a loop to repeatedly ask for employee name, hours worked, and pay rate.
#    a. If the name is "Finished", break the loop.
#    b. Calculate regular pay and overtime pay based on hours worked.
#    c. Display individual employee details.
# 3. After the loop ends, display total amounts for overtime pay, regular pay, gross pay, and number of employees.

# Initialize counters
total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

while True:
    # Get employee name
    employees_names = input("Enter employee's name or 'Finished' to terminate: ")
    
    # Check if user wants to stop entering data
    if employees_names.lower() == "finished":
        break
    
    # Get hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employees_names} work? "))
    pay_rate = float(input(f"What is {employees_names}'s pay rate? "))
    
    # Calculate regular and overtime pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Add to totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Display individual employee pay details also using \n to make it break and look clean. 
    print("\nEmployee name:", employees_names)
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("-"*69)
    print(f"{hours_worked:<14}{pay_rate:<11}{overtime_hours:<10}{overtime_pay:<14.2f}{regular_pay:<13.2f}{gross_pay:<10.2f}")
    print()

# Display total summary
print("\nTotal number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")


#maybe add taxes for fun and catch a boss not paying you correctly?
