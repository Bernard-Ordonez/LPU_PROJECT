#import from "MidtermQuiz_BASE0.1"
from MidtermQuiz_BASE@ import Personal_info

#Input For Personal Info
Name = input(f"Enter Name: ")
Service_address = input(f"Enter Service Address: ")
print(f"______________________________________________________")
KWH_Rate = input(f"Enter Rate per KWH: ")
Total_KWH = input(f"Enter Total KWH: ")
Previous_billing = input(f"Enter Previous Billing: ")
Amount_due = input(f"Enter Amount Due: ")

Personal_info = Personal_info(
Name=Name,
Service_address=Service_address,
KWH_Rate=KWH_Rate,
Total_KWH=Total_KWH,
Previous_billing=Previous_billing,
Amount_due=Amount_due,
)

Customer_account_number = input(f"Enter Customer Account Number (CAN): ")
Due_date = input(f"Enter Due Date: ")
print(f"______________________________________________________")
Service_ID_number = input(f"Enter Service ID Number: ")
Rate = input(f"Enter Rate: ")
print(f"______________________________________________________")
Bill_date = input(f"Enter Bill Date: ")
Meter_reading_date = input(f"Enter Meter Reading Date: ")
Bill_period = input(f"Enter Bill Period: ")
Total_current_amount = input(f"Enter Total Current Amount: ")
Next_meter_reading = input(f"Enter Next Meter Reading: ")