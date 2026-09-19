# Program to calculate the percentage of a student
# based on marks obtained in 5 subjects

print("Student Percentage Calculator")

# Taking marks as input
subject1 = float(input("Enter marks obtained in Subject 1: "))
subject2 = float(input("Enter marks obtained in Subject 2: "))
subject3 = float(input("Enter marks obtained in Subject 3: "))
subject4 = float(input("Enter marks obtained in Subject 4: "))
subject5 = float(input("Enter marks obtained in Subject 5: "))

# Calculating total marks
total_marks = subject1 + subject2 + subject3 + subject4 + subject5

# Maximum marks for 5 subjects
maximum_marks = 500

# Calculating percentage
percentage = (total_marks / maximum_marks) * 100

# Displaying the result
print("\n----- Result -----")
print("Total Marks Obtained:", total_marks)
print("Maximum Marks:", maximum_marks)
print("Percentage:", percentage, "%")
