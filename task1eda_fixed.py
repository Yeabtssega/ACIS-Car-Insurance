# task1eda_fixed.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = "cleaned_MachineLearningRating.csv"
df = pd.read_csv(file_path, low_memory=False)

# Basic Overview
print("Basic Information:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Check for missing values
missing = df.isnull().sum()
print("\nMissing Values:")
print(missing[missing > 0])

# Distribution of TotalPremium
plt.figure(figsize=(10, 6))
sns.histplot(df['TotalPremium'].dropna(), bins=50, kde=True)
plt.title('Distribution of Total Premium')
plt.xlabel('Total Premium')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('fig_totalpremium_dist.png')
plt.close()

# Correlation heatmap for numeric features
plt.figure(figsize=(12, 8))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('fig_correlation_heatmap.png')
plt.close()

# Count of CoverGroup
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='CoverGroup', order=df['CoverGroup'].value_counts().index)
plt.title('CoverGroup Distribution')
plt.xlabel('Count')
plt.tight_layout()
plt.savefig('fig_covergroup_distribution.png')
plt.close()

print("EDA figures saved. Script completed.")
