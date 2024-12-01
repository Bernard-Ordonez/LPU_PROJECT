# this program is designed to compute the payroll salary of an employee

class Employee:
    hdmf = 100.00

# initialization or constructor method of
    def __init__(self):

# Class employee

      self.hdmf_contribution = 100.00
      self.company_name = input("Enter Company Name: ")
      self.employee_department = input("Enter Employee Department: ")
      self.employee_name = input("Enter Employee Name: ")
      self.employee_code = input("Enter Employee Code: ")
      self.salary_cut_off = input("Enter Cut-Off Date: ")
# input for salary computation
      self.emp_rate_per_hour = float(input("Employee Rate Per Hour: "))
      self.emp_num_of_hours_per_payday = int(input("Employee's number of hours worked per payday: "))
      self.emp_hour_overtime = float(input("Employee Overtime: "))
      self.honorarium_pay = float(input("Employee Honorarium pay: "))
      self.emp_num_of_absences = int(input("Employee absences: "))
      self.emp_num_tardiness = int(input("Employee Tardiness: "))

# Compute
    def emp_salary_computation(self):
      self.basic_pay = (self.emp_rate_per_hour*self.emp_num_of_hours_per_payday)
      self.overtime = (self.emp_rate_per_hour*self.emp_hour_overtime)
      self.emp_absences = (self.emp_rate_per_hour*self.emp_num_of_absences)
      self.emp_tardiness = (self.emp_rate_per_hour*self.emp_num_tardiness)

      self.emp_gross_earnings = (self.basic_pay+self.overtime+self.honorarium_pay)

    def emp_sss_contribution(self):
      self.emp_gross_earnings = self.emp_gross_earnings
      self.sss_contribution = 0.00


    def emp_sss_contribution(self):
     earnings_limit = 4250
     increment = 500
     contribution = 180.00
     max_contribution = 900.00

    # Use a while loop to determine the appropriate contribution
     while earnings_limit < 19750:
        if self.emp_gross_earnings < earnings_limit:
            self.sss_contribution = contribution
            return  # Exit the function once the contribution is set
        earnings_limit += increment
        contribution += 22.50

    # If no match is found or the gross earnings exceed all ranges, default to the highest contribution
     self.sss_contribution = max_contribution

# Philhealth contribution
    def emp_philhealth_contribution(self):
# Setting conditions in getting Philhealth Contribution
     if self.emp_gross_earnings < 10000:
            self.philhealth_contribution = 0.00
     else:
            self.philhealth_contribution = self.emp_gross_earnings * 0.0450

# Tax contribution
    def emp_tax_contribution(self):
# Setting conditions in getting Tax Contribution
     if self.emp_gross_earnings < 10417:
        self.tax_contribution = 0.00
     elif self.emp_gross_earnings >= 10417 and self.emp_gross_earnings <= 16666:
         self.tax_contribution = ((self.emp_gross_earnings - 10417) * 0.15 + 0.00)
     elif self.emp_gross_earnings >= 16667 and self.emp_gross_earnings <= 33332:
         self.tax_contribution = ((self.emp_gross_earnings - 16667) * 0.20 + 937.50)
     elif self.emp_gross_earnings >= 33333 and self.emp_gross_earnings <= 83332:
         self.tax_contribution = ((self.emp_gross_earnings - 33333) * 0.25 + 4270.70)
     elif self.emp_gross_earnings >= 83333:
         self.tax_contribution = ((self.emp_gross_earnings - 83333) * 0.30 + 16770.70)
     else:
         self.tax_contribution = ((self.emp_gross_earnings - 333333) * 0.35 + 91770.70)

    def emp_total_deduction(self):
        self.deduction = self.emp_absences + self.emp_tardiness + self.tax_contribution + self.sss_contribution + self.philhealth_contribution + self.hdmf_contribution
    def emp_employee_net_pay(self):
        self.net_pay = self.emp_gross_earnings - self.deduction
    def emp_displayEmployee(self):
        print("Company Name : ", self.company_name)
        print("Employee Department: ", self.employee_department)
        print("Employee Name: ", self.employee_name)
        print("Employee Code: ", self.employee_code)
        print("Cut-Off Date: ", self.salary_cut_off)
        print("Basic Pay: %.2f " % self.basic_pay)
        print("Overtime Pay: %.2f " % self.overtime)
        print("Gross Income: %.2f " % self.emp_gross_earnings)
        print("Absences: %.2f " % self.emp_absences)
        print("Tardiness: %.2f " % self.emp_tardiness)
        print("SSS Contribution: %.2f " % self.sss_contribution)
        print("Tax Contribution: %.2f " % self.tax_contribution)
        print("Philhealth Contribution: %.2f " % self.philhealth_contribution)
        print("Total Deduction: %.2f " % self.deduction)
        print("Net Income: %.2f " % self.net_pay)

emp1 = Employee()
emp1.emp_salary_computation()
emp1.emp_sss_contribution()
emp1.emp_philhealth_contribution()
emp1.emp_tax_contribution()
emp1.emp_total_deduction()
emp1.emp_employee_net_pay()
emp1.emp_displayEmployee()
