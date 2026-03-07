# pd.merge(df1, df2, on="Column_Name", how="type of join")

import pandas as pd

df_customer = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Ramesh", "Suresh", "Mahesh"]
})

df_order = pd.DataFrame({
    "CustomerID": [1, 2, 4],
    "OrderAmount": [250, 450, 500]
})

# merge
df_merge = pd.merge(df_customer, df_order, on="CustomerID", how="right")
print("Right Join ")
print(df_merge)
