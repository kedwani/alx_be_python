import datetime
from datetime import timedelta
def display_current_datetime() :
        current_date =datetime.date.today()
        now = datetime.datetime.now()
        formatted = now.strftime("%Y-%m-%d %H:%M:%S")
        print("Current date and time: ",formatted)
def calculate_future_date():
    NUM_OF_DAYES= int(input("Enter the number of days to add to the current date:")) 
    future_date= datetime.date.today() + timedelta(days=NUM_OF_DAYES)
    FORMATED = future_date.strftime("%Y-%m-%d")
    print("Future date: ",FORMATED)



display_current_datetime()  
calculate_future_date()