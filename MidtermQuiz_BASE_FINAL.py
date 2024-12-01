# Set Class for Name & Address
class Meralco_Personal_Info:

    def __init__(self, Name, Service_Address):
        self.Name = Name
        self.Service_Address = Service_Address
    def display_Meralco_Personal_Info(self):
        print("|________________________________________________________________________________________________________|")
        print(f"{self.Name}")
        print(f"{self.Service_Address}")

# Set Class for Customer Account Summary
class Customer_Account_Summary:

    def __init__(self, Customer_Account_Number, Previous_Balance, Amount_Due, Due_Date, KWH_Rate, Total_KWH, Total_Amount_Due):
        self.Customer_Account_Number = Customer_Account_Number
        self.Previous_Balance = Previous_Balance
        self.Balance_Response = ""
# Set Variable Response
        if self.Previous_Balance <= 0.00:
            self.Balance_Response = "Thank you"
        else:
            self.Balance_Response = "Kindly Pay Your Fees"
        self.Amount_Due = Amount_Due
        self.Due_Date = Due_Date

# Set Values for Total Amount Calculation
        self.KWH_Rate = KWH_Rate
        self.Total_KWH = Total_KWH
        self.Total_Amount_Due = Total_Amount_Due

    def display_Customer_Account_Summary(self):
        print("|________________________________________________________________________________________________________|")
        print("| CUSTOMER TIN                           ELECTRIC BILL                                                   |")
        print("|________________________________________________________________________________________________________|")
        print(f"|Summary for Customer Account Number (CAN) {self.Customer_Account_Number}                                                    |")
        print("|________________________________________________________________________________________________________|")
        print("|            Balance                 |              Current Charges          |                           |")
        print("|      From Previous Billing         |     Amount Due      |     Due Date    |     Total Amount Due      |")
        print("|________________________________________________________________________________________________________|")
        print(f"     ₱ {self.Previous_Balance}  {self.Balance_Response} ₱ {self.Amount_Due} {self.Due_Date}  ₱ {self.Total_Amount_Due} ")
        print("|________________________________________________________________________________________________________|")