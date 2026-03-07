import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Rohit"],
    "Age": [23, 20, 24],
    "Salary": [50000, 60000, 45000],
}

df = pd.DataFrame(data)

avg_salary = df["Salary"].mean()
print(avg_salary)