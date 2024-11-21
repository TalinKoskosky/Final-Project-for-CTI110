#Talin Koskosky
#CTI110
#10-9-24    #10-10-24 


#calculation of travel expense.

#SelfNotes: Stop using Inputs, use floats for money::floats permit decimals like 10.1 where inputs dont:: Also find out word wrappign again:: 

budget = float(input("Enter your budget for the trip $"))

    
destination = input("Enter your travel destination: ")


    #gas useage
gas_expense = float(input("enter how much you will spend on gas $"))

            #over all extra cash, gifts, food, etc

accommodation_expense = float(input("enter how much you will spend on accommandations: $"))
            #food
food_expense = float(input("Enter how much you will spend on food: $"))


                #adding expenses using "+"
total_expenses = gas_expense + accommodation_expense + food_expense





#10-10-24 updated with new showcase. 

remaining_budget = budget - total_expenses
print("----------Travel Expenses---------")
print(f"Budget                   ${budget}")
print(f"Travel Destination:      {destination}")
print(f"Gas Expense:             ${gas_expense}")
print(f"Accommodation Expense:   ${accommodation_expense}")
print(f"Food expenese:           ${food_expense}")
print(f"Total Expenses:          ${total_expenses:.2f}")
print("-" * 34)
print(f"Remaining Budget:       ${remaining_budget:2f}")

