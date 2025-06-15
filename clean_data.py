import pandas as pd

# Use the full path with raw string notation
raw_csv = r"C:\Users\HP\ACIS-Car-Insurance-EDA\cleaned_MachineLearningRating.csv"

# Load the CSV
df = pd.read_csv(raw_csv)

# Show the first few rows to check it loaded correctly
print(df.head())

# (Add any cleaning steps here if needed)

# Save cleaned data (optional)
cleaned_csv = r"C:\Users\HP\ACIS-Car-Insurance-EDA\cleaned_MachineLearningRating_cleaned.csv"
df.to_csv(cleaned_csv, index=False)
print(f"Saved cleaned data to {cleaned_csv}")
