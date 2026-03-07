import pandas as pd

data = {
    "Name": ["Ram", None, "Rohit", "Aditi", "Rohan", "Vikas", "Raj", "Simran"],
    "Age": [23, None, 24, 30, 34, 28, 23, 34],
    "Salary": [50000, None, 45000, 52000, 55000, 35000, 40000, 75000],
    "Performance Score": [85, None, 92, 95, 88, 94, 99, 72]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull().sum())