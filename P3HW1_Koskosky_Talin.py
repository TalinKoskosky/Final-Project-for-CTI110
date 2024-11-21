#Talin Koskosky
#10-11-24
#P2HW2
#Making a quick program to show avg grades plus more in class.
#------------10-14-24-----------
#P3HW1
#use branching to determine a letter grade. 
#
#-------------------------------

#list
grades = []

#grades for modules
#grades.append adds the grade to list. 

grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

#Calculate numbers

highest_grade = max(grades)

lowest_grade =min(grades)

sum_of_grades =sum(grades)

average_grade = sum_of_grades / len(grades)

#show results
print("-" * 34)
print("Lowest grade: ", lowest_grade)
print("Highest grade: ", highest_grade)
print("Sum of grades: ", sum_of_grades)
print("Average of grades: {:.2f}" .format(average_grade))
print("-" * 34)



#make list named grades
#ask for grades from the 6 modules
#cal the highest to the lowest while calculating the sum and average
#display grades




#----------------new lines------------------

#create a branching to get the letter grade
# average = float(input("what is the average? ") )

if average_grade>= 90:
    letter_grade = "A"

elif average_grade>= 80:
    letter_grade = "B"

elif average_grade>= 70:
    letter_grade = "C"

elif average_grade>= 60:
    letter_grade = "D"

else:
    letter_grade = "F"


#display the results.

print(f"The average is {average_grade:.2f} -- letter grade: {letter_grade}")



