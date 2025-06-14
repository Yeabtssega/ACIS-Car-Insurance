import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    path = r'C:\Users\HP\ACIS-Car-Insurance-EDA\cleaned_MachineLearningRating.csv'
    
    # Load data with low_memory=False to avoid dtype warning
    df = pd.read_csv(path, low_memory=False)
    
    print("=== First 5 rows ===")
    print(df.head())

    print("\n=== Data info ===")
    df.info()

    print("\n=== Missing values per column ===")
    print(df.isnull().sum())

    # Drop columns with all missing values
    cols_to_drop = ['CrossBorder', 'NumberOfVehiclesInFleet']
    df = df.drop(columns=cols_to_drop)
    print(f"\nDropped columns with all missing values: {cols_to_drop}")

    # Fill missing values in important categorical columns with 'Unknown'
    cat_cols_to_fill = ['Bank', 'AccountType', 'CustomValueEstimate', 'NewVehicle', 'WrittenOff']
    for col in cat_cols_to_fill:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')

    # Summary statistics for numeric columns
    print("\n=== Summary statistics for numeric columns ===")
    print(df.describe())

    # Plot histograms of TotalPremium and TotalClaims
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    sns.histplot(df['TotalPremium'], bins=50, kde=True)
    plt.title('Distribution of Total Premium')

    plt.subplot(1,2,2)
    sns.histplot(df['TotalClaims'], bins=50, kde=True)
    plt.title('Distribution of Total Claims')

    plt.tight_layout()
    plt.savefig(r'C:\Users\HP\ACIS-Car-Insurance-EDA\premium_claims_histograms.png')
    print("\nSaved histogram plot to premium_claims_histograms.png")
    plt.close()

    # Bar plot for missing value categories in 'Bank' (top 10)
    plt.figure(figsize=(10,5))
    sns.countplot(y='Bank', data=df[df['Bank'] != 'Unknown'], order=df['Bank'].value_counts().iloc[:10].index)
    plt.title('Top 10 Banks by Count (excluding Unknown)')
    plt.tight_layout()
    plt.savefig(r'C:\Users\HP\ACIS-Car-Insurance-EDA\top10_banks.png')
    print("Saved bar plot for top 10 banks to top10_banks.png")
    plt.close()

    # Save cleaned dataframe for next tasks
    cleaned_path = r'C:\Users\HP\ACIS-Car-Insurance-EDA\cleaned_data_task1.csv'
    df.to_csv(cleaned_path, index=False)
    print(f"\nSaved cleaned data to {cleaned_path}")

if __name__ == "__main__":
    main()
