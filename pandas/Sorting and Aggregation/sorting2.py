# sorting data in multiple column sort_values()
# df.sort_values(by=["Column_Name1", "Column_Name2"], True / False, inplace=True)


import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Rohit"],
    "Age": [23, 20, 24],
    "Salary": [50000, 60000, 45000],
}

df = pd.DataFrame(data)

df.sort_values(by=["Age", "Salary"], ascending=[True, True], inplace=True)
print("Sorted Age by descending")
print(df)