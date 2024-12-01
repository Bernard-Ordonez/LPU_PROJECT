# Import from MidtermQuiz_BASE_FINAL
from MidtermQuiz_BASE_FINAL import Meralco_Personal_Info, Customer_Account_Summary

Name = input("Enter Name: ")
Service_Address = str(input("Enter Address: "))

# Create personal Info object
Personal_Info = Meralco_Personal_Info(
    Name = Name,
    Service_Address = Service_Address
)

print("______________________________________________________________")
Customer_Account_Number = input("Enter Customer Service Number: ")
Previous_Balance = float(input("Enter balance from previous billing: "))
Amount_Due = float(input("Enter Amount Due: "))
Due_Date = str(input("Enter Due Date (DD/MM/YY): "))
print("______________________________________________________________")
KWH_Rate = int(input("Enter KWH Rate: "))
Total_KWH = int(input("Enter Total KWH: "))
Total_Amount_Due = int(KWH_Rate*Total_KWH)

# Create Customer Account Summary object
Account_Summary = Customer_Account_Summary(
    Customer_Account_Number = Customer_Account_Number,
    Previous_Balance = Previous_Balance,
    Amount_Due = Amount_Due,
    Due_Date = Due_Date,
    KWH_Rate = KWH_Rate,
    Total_KWH = Total_KWH,
    Total_Amount_Due = Total_Amount_Due,
)

Personal_Info.display_Meralco_Personal_Info()
Account_Summary.display_Customer_Account_Summary()