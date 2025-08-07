from datetime import datetime, timedelta
import pandas as pd

df = pd.read_csv("work_hours.csv")  
print(df) 

today = datetime.now()
weekday = today.weekday()
monday = today - timedelta(days=weekday)

week_str = monday.date().isoformat()
new_hour = float(input("hours worked today: "))

