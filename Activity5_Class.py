
class Student:
    def __init__(self, name, student_number, academic_year, course):
        self.name = name
        self.student_number = student_number
        self.academic_year = academic_year
        self.course = course

    def display_student_details(self):
        print(f"Name: {self.name}")
        print(f"Student Number: {self.student_number}")
        print(f"Academic Year: {self.academic_year}")
        print(f"Course: {self.course}")

class Enrollment:
    def __init__(self, subjects, total_units, fees, downpayment):
        self.subjects = subjects
        self.total_units = total_units
        self.fees = fees
        self.downpayment = downpayment

        self.fees["Tuition Fee Lecture"] = total_units * 1551

    def display_enrollment_details(self):
        print("Subjects Enrolled:")
        for subject in self.subjects:
            print(f"  Section: {subject['section']}, Subject: {subject['name']}, Units: {subject['units']}")
        print(f"Total Units: {self.total_units}")

        print("Assessment of Fees:")
        for fee_name, fee_amount in self.fees.items():
            print(f"  {fee_name}: {fee_amount}")

        print(f"Downpayment: {self.downpayment}")
        assessment_amount = self.calculate_total_fees()
        print(f"Assessment Amount: {assessment_amount:.2f}")

        total_due = assessment_amount - float(self.downpayment)
        print(f"Total Due: {total_due:.2f}")

        prelims = midterms = finals = total_due / 3
        print(f"PRELIMS: {prelims:.2f}")
        print(f"MIDTERMS: {midterms:.2f}")
        print(f"FINALS: {finals:.2f}")

    def calculate_total_fees(self):
        total_fees = sum(float(fee) for fee in self.fees.values())
        return total_fees
