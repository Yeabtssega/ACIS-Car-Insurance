import pandas as pd

# Load dataset
df = pd.read_csv('cleaned_MachineLearningRating.csv', low_memory=False)

print("Columns available for modeling:")
print(df.columns.tolist())

# Select columns related to claim severity that we want to convert safely
cols_to_convert = ['CustomValueEstimate', 'CapitalOutstanding', 'SumInsured', 'TotalClaims']

# Create a dataframe with only severity columns and safely convert them
df_severity = df[cols_to_convert].copy()

for col in cols_to_convert:
    # Find and print any non-numeric values in the column
    non_numeric = df_severity[~df_severity[col].astype(str).str.isnumeric()][col].unique()
    print(f"Non-numeric values in column '{col}': {non_numeric}")

    # Convert column to numeric, forcing errors to NaN, then fill NaN with 0 and convert to int
    df_severity[col] = pd.to_numeric(df_severity[col], errors='coerce').fillna(0).astype(int)

print("\nCleaned severity data types:")
print(df_severity.dtypes)

# Now you can continue with your modeling or analysis using df_severity safely converted

# Example: Simple stats summary
print("\nSeverity data summary:")
print(df_severity.describe())
