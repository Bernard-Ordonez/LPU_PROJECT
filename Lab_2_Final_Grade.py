# Initialize
Final_Grade = 0
# Input
Student_Name = str(input("Enter Student Name = "))
Final_Quizzes = float(input("Enter Midterm Grade = "))
Final_Research_and_Assignment = float(input("Enter Final Research/Assignment = "))
Final_Project = float(input("Enter Final Project = "))
Final_Exam = float(input("Enter Final Exam = "))
# Compute
Final_Grade = ((0.30*Final_Quizzes)+(0.10*Final_Research_and_Assignment)+(0.40*Final_Exam)+(0.20*Final_Project))
# Decision
if 100.00 < Final_Grade:
    print("NO GRADE MUST EXCEED 100")
    Remark = float("Nan")
elif 98 <= Final_Grade:
    Remark = 4.00
elif 95 <= Final_Grade:
    Remark = 3.75
elif 92 <= Final_Grade:
    Remark = 3.50
elif 89 <= Final_Grade:
    Remark = 3.25
elif 86 <= Final_Grade:
    Remark = 3.00
elif 83 <= Final_Grade:
    Remark = 2.75
elif 80 <= Final_Grade:
    Remark = 2.50
elif 77 <= Final_Grade:
    Remark = 2.25
elif 74 <= Final_Grade:
    Remark = 2.00
elif 71 <= Final_Grade:
    Remark = 1.75
elif 68 <= Final_Grade:
    Remark = 1.50
elif 64 <= Final_Grade:
    Remark = 1.25
elif 60 <= Final_Grade:
    Remark = 1.00
else:
    Remark = 0.00
# Display
print(f"Student Name = {Student_Name}")
print(f"Final Quizzes = {Final_Quizzes}")
print(f"Final Research and Assignment = {Final_Research_and_Assignment}")
print(f"Final Project = {Final_Project}")
print(f"Final Exam = {Final_Exam}")
print(f"Remark = {Remark}")
