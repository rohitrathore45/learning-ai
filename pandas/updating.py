import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Rohit", "Aditi", "Rohan", "Vikas", "Raj", "Simran"],
    "Age": [23, 20, 24, 30, 34, 28, 23, 34],
    "Salary": [50000, 60000, 45000, 52000, 55000, 35000, 40000, 75000],
    "Performance Score": [85, 90, 92, 95, 88, 94, 99, 72]
}

df = pd.DataFrame(data)
print(df)

# .loc[] -> method to access specific cell and modify them
# df.loc[row_index, "Column_Name"] = new_value

df.loc[0, "Salary"] = 55000
print(df)

