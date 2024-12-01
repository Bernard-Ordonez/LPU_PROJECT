
from Activity5_Class import Student, Enrollment

num_subjects = int(input("Enter number of subjects: "))
subjects = []

for i in range(num_subjects):
    print(f"Enter details for Subject {i+1}:")
    section = input("  Enter Section: ")
    subject_name = input("  Enter Subject Name: ")
    units = int(input("  Enter Units: "))
    subjects.append({"section": section, "name": subject_name, "units": units})

print("Subjects Enrolled:")
for subject in subjects:
    print(f"  Section: {subject['section']}, Subject: {subject['name']}, Units: {subject['units']}")
