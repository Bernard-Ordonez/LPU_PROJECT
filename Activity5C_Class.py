
from Activity5_Class import Enrollment

total_units = int(input("Enter Total Units: "))
print("Enter other fees assessment:")
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

downpayment = float(input("Enter Downpayment: "))

# Create an enrollment object
enrollment = Enrollment(
    subjects=[],
    total_units=total_units,
    fees=fees,
    downpayment=downpayment
)

enrollment.display_enrollment_details()

assessment_amount = enrollment.calculate_total_fees()
total_due = assessment_amount - downpayment
print(f"Total Due: {total_due:.2f}")

prelims = total_due / 3
midterms = total_due / 3
finals = total_due / 3