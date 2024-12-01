# Initialize
Year = ""
Basic_Pay = 0
Overtime = 0
Absences = 0
Tardiness = 0
WithHolding_Tax = 0
SSS_Contribution = 0
PhilHealth_Contribution = 0
HDMF_Contribution = 100.00
Gross_Earnings = 0
Deductions = 0
Net_Pay = 0

# Input
Company_Name = str(input("Enter Company Name = "))
Department_Name = str(input("Enter Department Name = "))
Employee_Code = float(input("Enter Employee Code = "))
Employee_Name = str(input("Enter Employee Name = "))
Salary_Cut_off_Date = str(input("Enter Cut-Off Month-Day-Year (e.g. 12-30-2024) = "))
Pay_Period = Salary_Cut_off_Date
Rate_per_hour = float(input("Enter Rate per hour = "))
Number_of_hours_per_payday = float(input("Enter Number of hours per Payday = "))
Number_of_hours_overtime_per_payday = float(input("Enter Number of hours Overtime per Payday = "))
Number_of_Absences_in_hours = float(input("Enter Number of Absences in hour(s) = "))
Number_of_Tardiness_in_hours = float(input("Enter Number of Tardiness in hour(s) = "))
Honorarium = float(input("Enter Honorarium = "))

# Split Dates for Data Precision
Month,Day,Year = Salary_Cut_off_Date.split('-')
Year = int(Year)

# Compute
Basic_Pay = (Rate_per_hour*Number_of_hours_per_payday)
Overtime = (Rate_per_hour*Number_of_hours_overtime_per_payday)
Absences = (Rate_per_hour*Number_of_Absences_in_hours)
Tardiness = (Rate_per_hour*Number_of_Tardiness_in_hours)

Gross_Earnings = (Basic_Pay+Overtime+Honorarium)

# Decision (WithHolding_Tax)
if 333333 <= Gross_Earnings:
    WithHolding_Tax = (91770.70+(Gross_Earnings*0.35))/333333
if 83333 <= Gross_Earnings:
    WithHolding_Tax = (16770.70+(Gross_Earnings*0.30))/83333
if 33333 <= Gross_Earnings:
    WithHolding_Tax = (4270.70+(Gross_Earnings*0.25))/33333
if 16667 <= Gross_Earnings:
    WithHolding_Tax = (937.50+(Gross_Earnings*0.20))/16667
if 10417 <= Gross_Earnings:
    WithHolding_Tax = (0.00+(Gross_Earnings*0.15))/10417
else:
    WithHolding_Tax = 0.00

# Decision (SSS_Contribution)
if 19750 <= Gross_Earnings:
    SSS_Contribution = 900.00
elif 19250 <= Gross_Earnings:
    SSS_Contribution = 877.50
elif 18750 <= Gross_Earnings:
    SSS_Contribution = 855.00
elif 18250 <= Gross_Earnings:
    SSS_Contribution = 832.50
elif 17750 <= Gross_Earnings:
    SSS_Contribution = 810.00
elif 17250 <= Gross_Earnings:
    SSS_Contribution = 787.50
elif 16750 <= Gross_Earnings:
    SSS_Contribution = 765.00
elif 16250 <= Gross_Earnings:
    SSS_Contribution = 742.50
elif 15750 <= Gross_Earnings:
    SSS_Contribution = 720.00
elif 15250 <= Gross_Earnings:
    SSS_Contribution = 697.50
elif 14750 <= Gross_Earnings:
    SSS_Contribution = 675.00
elif 14250 <= Gross_Earnings:
    SSS_Contribution = 652.50
elif 13750 <= Gross_Earnings:
    SSS_Contribution = 630.00
elif 13250 <= Gross_Earnings:
    SSS_Contribution = 607.50
elif 12750 <= Gross_Earnings:
    SSS_Contribution = 585.00
elif 12250 <= Gross_Earnings:
    SSS_Contribution = 562.50
elif 11750 <= Gross_Earnings:
    SSS_Contribution = 540.00
elif 11250 <= Gross_Earnings:
    SSS_Contribution = 517.50
elif 10750 <= Gross_Earnings:
    SSS_Contribution = 495.00
elif 10250 <= Gross_Earnings:
    SSS_Contribution = 472.50
elif 9750 <= Gross_Earnings:
    SSS_Contribution = 450.00
elif 9250 <= Gross_Earnings:
    SSS_Contribution = 427.50
elif 8750 <= Gross_Earnings:
    SSS_Contribution = 405.00
elif 8250 <= Gross_Earnings:
    SSS_Contribution = 382.50
elif 7750 <= Gross_Earnings:
    SSS_Contribution = 360.00
elif 7250 <= Gross_Earnings:
    SSS_Contribution = 337.50
elif 6750 <= Gross_Earnings:
    SSS_Contribution = 315.00
elif 6250 <= Gross_Earnings:
    SSS_Contribution = 292.50
elif 5750 <= Gross_Earnings:
    SSS_Contribution = 270.00
elif 5250 <= Gross_Earnings:
    SSS_Contribution = 247.50
elif 4750 <= Gross_Earnings:
    SSS_Contribution = 225.00
elif 4250 <= Gross_Earnings:
    SSS_Contribution = 202.50
else:
    SSS_Contribution = 180.00

# Decision (PhilHealth_Contribution)
if Year == 2019:
    if Gross_Earnings >= 50000:
        PhilHealth_Contribution = 1375.00
    elif Gross_Earnings >= 10000.01:
        PhilHealth_Contribution = (Gross_Earnings*0.0275)
    else:
        PhilHealth_Contribution = 275.00
elif Year == 2020:
    if Gross_Earnings >= 60000:
        PhilHealth_Contribution = 1800.00
    elif Gross_Earnings >= 10000.01:
        PhilHealth_Contribution = (Gross_Earnings*0.03)
    else:
        PhilHealth_Contribution = 300.00
elif Year == 2021:
    if Gross_Earnings >= 70000:
        PhilHealth_Contribution = 2450.00
    elif Gross_Earnings >= 10000.01:
        PhilHealth_Contribution = (Gross_Earnings*0.035)
    else:
        PhilHealth_Contribution = 350.00
elif Year == 2022:
    if Gross_Earnings >= 80000:
        PhilHealth_Contribution = 3200.00
    elif Gross_Earnings >= 10000.01:
        PhilHealth_Contribution = (Gross_Earnings*0.04)
    else:
        PhilHealth_Contribution = 400.00
elif Year == 2023:
    if Gross_Earnings >= 90000:
        PhilHealth_Contribution = 4050.00
    elif Gross_Earnings >= 10000.01:
        PhilHealth_Contribution = (Gross_Earnings*0.045)
    else:
        PhilHealth_Contribution = 450.00
elif Year == 2024 or Year == 2025:
    if Gross_Earnings >= 100000:
        PhilHealth_Contribution = 5000.00
    elif Gross_Earnings >= 10000.01:
        PhilHealth_Contribution = (Gross_Earnings*0.05)
    else:
        PhilHealth_Contribution = 500.00

# Compute
Deductions = (Absences+Tardiness+WithHolding_Tax+SSS_Contribution+PhilHealth_Contribution+HDMF_Contribution)
Net_Pay = (Gross_Earnings-Deductions)

# Display
print("********************************")
print("________________________________")
print(f"Company Name:  {Company_Name}")
print(f"Employee Code: {Employee_Code}")
print(f"Employee Name: {Employee_Name}")
print("________________________________")
print(f"Department: {Department_Name}")
print(f"Cut-Off:    {Salary_Cut_off_Date}")
print(f"Pay Period: {Salary_Cut_off_Date}")
print("________________________________")
print(f"===EARNINGS===")
print(f"Basic Pay:  {Basic_Pay}")
print(f"Overtime:   {Overtime}")
print(f"Absences:   {Absences}")
print(f"Honorarium: {Honorarium}")
print(f"Tardiness:  {Tardiness}")
print("********************************")
print(f"    EARNINGS: {Gross_Earnings}")
print("********************************")
print("________________________________")
print(f"===DEDUCTIONS===")
print(f"WithHolding Tax:          {WithHolding_Tax}")
print(f"SSS Contributions:        {SSS_Contribution}")
print(f"HDMF Contributions:       {HDMF_Contribution}")
print(f"PhilHealth Contributions: {PhilHealth_Contribution}")
print("********************************")
print(f"    DEDUCTIONS: {Deductions}")
print("********************************")
print("________________________________")
print(f"GROSS EARNINGS          {Gross_Earnings}")
print(f"DEDUCTIONS              {Deductions}")
print(f"NET PAY                 {Net_Pay}")
