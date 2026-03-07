import pandas as pd

# head() tail()
# head(n) = provide first n rows or by default give the first 5 rows
# tail(n) = provide last n rows or by default give the last 5 rows

df = pd.read_json("sample_Data.json")

print("Display first 10 rows", df.head())
print("Display last 10 rows", df.tail())