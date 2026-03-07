# sorting data in 1 column sort_values()
# df.sort_values(by="Column_Name", True / False, inplace=True)

import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Rohit"],
    "Age": [23, 20, 24],
    "Salary": [50000, 60000, 45000],
}

df = pd.DataFrame(data)

df.sort_values(by="Age", ascending=True, inplace=True)
print("Sorted by Age")
print(df)