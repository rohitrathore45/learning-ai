import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Rohit"],
    "Age": [10, 20, 24],
    "City": ["Nagpur", "Mumbai", "Indore"]
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
# df.to_excel("test.xlsx", index=False)
df.to_json("output.json")