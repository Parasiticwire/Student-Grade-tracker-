import statistics

print("--------------------------------------------------------")
student_gpa = []

n = int(input("Enter the number of students: "))
i=0
while n > 0:  
    gpa = float(input(f"Enter GPA for student {i + 1}: "))     
    if gpa < 0 or gpa > 4.0:
        print("Invalid GPA. Please enter a value between 0 and 4.0.")
        continue
    student_gpa.append(gpa)
    n -= 1
    i += 1

student_gpa.sort()
print("--------------------------------------------------------")
print("GPA list:", student_gpa)
if student_gpa:
    print("Minimum GPA:", min(student_gpa))
    print("Maximum GPA:", max(student_gpa))
    print("Average GPA:", statistics.mean(student_gpa))
    print("Median GPA:", statistics.median(student_gpa))
    print("Standard Deviation of GPA:", statistics.stdev(student_gpa))
else:
    print("No valid GPA entries were made.")
print("--------------------------------------------------------")
print("\n")