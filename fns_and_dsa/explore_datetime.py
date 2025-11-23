import datetime
def display_current_datetime() :
        current_date =datetime.date.today()
        now = datetime.datetime.now()
        formatted = now.strftime("%Y-%M-%D %H:%M:%S")
        print("Current date and time: ",formatted)
display_current_datetime()