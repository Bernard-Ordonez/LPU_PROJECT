
class Personal_info:
#Set Personal Info
    def __init__(self, Name, Service_address):
        self.Name = Name
        self.Service_Address = Service_address

    def display_Personal_info(self):
        print(f"{self.Name}")
        print(f"{self.Service_Address}")
        print("________________________________________________")
        print("________________________________________________")
#Set Total Due Data
    def Total_Due(self, KWH_Rate, Total_KWH, Previous_billing, Amount_due):
        self.KWH_Rate = KWH_Rate
        self.Total_KWH = Total_KWH
        self.Previous_Billing = Previous_billing
        self.Amount_due = Amount_due
        self.Total_amount_due = (self.Total_KWH * self.Rate)
#Set Billings Data
    def Previous_billing(self, Customer_account_number, Due_date, Bill_response):
        self.Customer_account_number = Customer_account_number
        self.Due_date = Due_date
        self.Bill_response = Bill_response

    def display_Previous_Billing(self):
        if self.Previous_Billing <= 0.00:
            self.Bill_response = print(f"Thank You")
        else:
            self.Bill_response = print(f"Kindly Pay Your Fees")
#Set Summary
    def display_Summary_of_bills(self):
        print(f"ELECTRIC BILL")
        print("__________________________________________________________________________________________________________________________________")
        print(f"Summary for Customer Account Number (CAN) {self.Customer_account_number}")
        print("__________________________________________________________________________________________________________________________________")
        print(f"       |        --Balance From Previous Billing--          |           --Current Charges--         |   --Total Amount Due--   |")
        print(f"       |                                                   |   --Amount Due--      --Due Date--    |                          |")
        print("__________________________________________________________________________________________________________________________________")
        print(f"        ₱ {self.Previous_Billing} | {self.Bill_response}")
        print(f"                                                              {self.Amount_due}   {self.Due_date}     {self.Total_amount_due}")
#Set Service Info
    def Service_Info(self, Service_ID_number, Rate,):
        self.Service_ID_Number = Service_ID_number
        self.Rate = Rate
        self.Name2 = self.Name
        self.Service_address2 = self.Service_address

    def display_Service_info(self):
        print(f"Service Info")
        print("___________________________________________________")
        print(f"Service ID Number:      {self.Service_ID_Number}")
        print(f"Rate:                   {self.Rate}")
        print(f"Contact in the name of: {self.Name2}")
        print(f"Service Address:        {self.Service_address2}")
        print("___________________________________________________")
#Set Billing Info
    def Billing_info(self, Bill_date, Meter_reading_date, Bill_period, Due_date, Total_current_amount, Next_meter_reading):
        self.Bill_date = Bill_date
        self.Meter_reading_date = Meter_reading_date
        self.Bill_period = Bill_period
        self.Due_date = Due_date
        self.Total_KWH2 = self.Total_KWH
        self.Total_current_amount = Total_current_amount
        self.Next_meter_reading = Next_meter_reading

    def display_Billing_info(self):
        print(f"Billing Info")
        print(f"_________________________________________________")
        print(f"Bill Date:             {self.Bill_date}")
        print(f"Meter reading Date:    {self.Meter_reading_date}")
        print(f"Bill Period:           {self.Bill_period}")
        print(f"Due Date:              {self.Due_date}")
        print(f"Total KWH:             {self.Total_KWH}")
        print(f"Total Current Amount:  {self.Total_current_amount}")
        print(f"Next Meter Reading:    {self.Next_meter_reading}")
        print(f"_________________________________________________")