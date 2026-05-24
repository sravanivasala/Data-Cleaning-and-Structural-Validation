import pandas as pd

# Load dataset
df = pd.read_csv("raw_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["Name"] = df["Name"].fillna("Unknown").str.title()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Not Available").str.title()

# Standardize date format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Data Cleaning Completed Successfully!")
