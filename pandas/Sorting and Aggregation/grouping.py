import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Rohit", "Aditi", "Rohan", "Vikas", "Raj", "Simran"],
    "Age": [23, 20, 24, 30, 34, 28, 23, 34],
    "Salary": [50000, 60000, 45000, 52000, 55000, 35000, 40000, 75000]
}

df = pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

