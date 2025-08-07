from datetime import datetime, timedelta
import pandas as pd
import matplotlib as plt

df = pd.read_csv("work_hours.csv")  
print(df) 

today = datetime.now()
weekday = today.weekday()
monday = today - timedelta(days=weekday)

week_str = monday.date().isoformat()
new_hour = float(input("hours worked today: "))


if week_str in df["week_start"].values:
    df.loc[df["week_start"] == week_str, "hours"] += new_hours
else:
        new_row = pd.DataFrame({
        "week_start": [week_str],
        "hours":      [new_hours]
    })
        df = pd.concat([df, new_row], ignore_index=True)

df.to_csv("Work_hours.csv", index=False)


plt.bar(df["week_start"],df['hours'])
plt.xticks(rotation= 45)# This makes the labels easier to read when they're long 
plt.title('Weekly Work hours')
plt.tight_layout()
plt.show()


