import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Rohit", "Aditi", "Rohan", "Vikas", "Raj", "Simran"],
    "Age": [23, 20, 24, 30, 34, 28, 23, 34],
    "Salary": [50000, 60000, 45000, 52000, 55000, 35000, 40000, 75000],
    "Performance Score": [85, 90, 92, 95, 88, 94, 99, 72]
}

df = pd.DataFrame(data)

# adding a new column via assignment
# square brackets df["New_Column_Name"] = some_data
print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)

# using insert method
# df.insert(loc, "New_Column_Name", some_data)
df.insert(0, "Employee ID", [10, 20, 30, 40, 50, 60, 70, 80])
print(df)

