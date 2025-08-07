from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


try:
    df = pd.read_csv("work_hours.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["date", "hours"])


today_str = datetime.now().date().isoformat()

new_hours = float(input("Hours worked today: "))

if today_str in df["date"].values:
    # Add to today's existing hours
    df.loc[df["date"] == today_str, "hours"] += new_hours
else:
    new_row = pd.DataFrame({
        "date": [today_str],
        "hours": [new_hours]
    })
    df = pd.concat([df, new_row], ignore_index=True)

df.to_csv("work_hours.csv", index=False)

# Plot daily hours
plt.bar(df["date"], df["hours"])
plt.xticks(rotation=45)# This makes the labels easier to read when they're long 
plt.title("Daily Work Hours")
plt.tight_layout()# automatically adjusts everything
plt.show()


