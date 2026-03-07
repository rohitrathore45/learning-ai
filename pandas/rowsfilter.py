import pandas as pd
data = {
    "Name": ["Ram", "Shyam", "Rohit", "Aditi", "Rohan", "Vikas", "Raj", "Simran"],
    "Age": [23, 20, 24, 30, 34, 28, 23, 34],
    "Salary": [50000, 60000, 45000, 52000, 55000, 35000, 40000, 75000],
    "Performance Score": [85, 90, 92, 95, 88, 94, 99, 72]
}

df = pd.DataFrame(data)

high_salary = df[df["Salary"] > 50000]
print("Employees with salary greater than 50000 : ", high_salary)

# filtering rows salary > 50000 and age > 30
filtered = df[(df["Salary"] > 50000) & (df["Age"] > 30)]
print("Employees with salary > 50000 and age greater than 30 ")
print(filtered)

# using or condition
filtered_or =  df[(df["Age"] > 35) | (df["Performance Score"] > 95)]
print("Employees with age greater than 30 or performance score > 95 ")
print(filtered_or)