"""
vertically(row-wise)
horizontally(column-wise)

pd.concatenate([df1, df2], axis=0, ignore_index=True)
"""
import pandas as pd

df_Region1 = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Ramesh", "Suresh", "Mahesh"]
})

df_Region2 = pd.DataFrame({
    "CustomerID": [4, 5, 6],
    "Name": ["Ramu", "Shyam", "RamaRao"]
})

# concatenate
df_concat = pd.concat([df_Region1, df_Region2], axis=1, ignore_index=True)
print(df_concat)