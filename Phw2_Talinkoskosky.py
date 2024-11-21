# P3HW2
#Talin koskosky
# Program to calculate the employee's weekly pay with normal and OT 

#name
employee_name = input("Enter employee's name: ")

#hours worked and pay rate
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate regular hours and overtime hours
overtime_hours = max(0, hours_worked - 40)  # Any hours over 40 are overtime
regular_hours = min(40, hours_worked)  # Regular hours are up to 40

# Calculate pay
overtime_pay = overtime_hours * pay_rate * 1.5  # Overtime = 1.5 times 
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Display the results
print("------------------------------")
print(f"Employee name:  {employee_name}")
print("Hours Worked  - Pay Rate -  Overtime -  Overtime Pay -  RegHour Pay  - Gross Pay")
print("----------------------------------------------------------------------")
print(f"{hours_worked:<14.1f}{pay_rate:<10.2f}{overtime_hours:<11.1f}${overtime_pay:<13.2f}${regular_pay:<13.2f}${gross_pay:<13.2f}")
