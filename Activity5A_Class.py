
from Activity5_Class import Student, Enrollment

name = input("Enter Student Name: ")
student_number = input("Enter Student Number: ")
academic_year = input("Enter Academic Year: ")
course = input("Enter Course: ")

student = Student(
    name=name,
    student_number=student_number,
    academic_year=academic_year,
    course=course
)

num_subjects = int(input("Enter number of subjects: "))
subjects = []

for i in range(num_subjects):
    print(f"Enter details for Subject {i+1}:")
    section = input("  Enter Section: ")
    subject_name = input("  Enter Subject Name: ")
    units = int(input("  Enter Units: "))
    subjects.append({"section": section, "name": subject_name, "units": units})

total_units = sum(subject['units'] for subject in subjects)

print("Enter other fees breakdown:")
fees = {}
fee_names = [
    "AdU Chronicle", "Athletic", "Audio-Visual Library", "AUSG", "Cultural Fee",
    "Energy Cost, Aircon Classroom", "Guidance", "Insurance Fee", "Learning Management System", 
    "Library Fee", "Medical and Dental", "Registration", "RSO", "Student Activities Fee", 
    "Student Nurturance Fee", "Technology Fee", "Test Papers"
]

for fee_name in fee_names:
    fee_amount = input(f"  Enter {fee_name} amount: ")
    fees[fee_name] = fee_amount

downpayment = input("Enter Downpayment: ")

# Create an enrollment object
enrollment = Enrollment(
    subjects=subjects,
    total_units=total_units,
    fees=fees,
    downpayment=downpayment
)

student.display_student_details()
enrollment.display_enrollment_details()
