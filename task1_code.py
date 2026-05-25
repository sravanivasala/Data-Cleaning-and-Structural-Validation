import pandas as pd


df = pd.read_csv("raw_data.csv")

df = df.drop_duplicates()

df["Name"] = df["Name"].fillna("Unknown").str.title()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Not Available").str.title()

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df.to_csv("cleaned_data.csv", index=False)

print("Data Cleaning Completed Successfully!")
