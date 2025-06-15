# task3_hypothesis_testing.py

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind

# Load data
df = pd.read_csv('cleaned_MachineLearningRating.csv')

# Inspect columns (optional)
print("Columns in dataset:", df.columns)

# Define Claim Frequency: proportion of policies with at least one claim
df['ClaimOccurred'] = np.where(df['TotalClaims'] > 0, 1, 0)
claim_frequency = df.groupby('Province')['ClaimOccurred'].mean()
print("\nClaim Frequency by Province:")
print(claim_frequency)

# Define Claim Severity: average claim amount given a claim occurred
claim_severity = df[df['ClaimOccurred'] == 1].groupby('Province')['TotalClaims'].mean()
print("\nClaim Severity by Province:")
print(claim_severity)

# Define Margin = TotalPremium - TotalClaims
df['Margin'] = df['TotalPremium'] - df['TotalClaims']

# --- Hypothesis Testing ---

print("\n=== Hypothesis Testing ===")

# 1) Are there risk differences across Provinces?
# We'll use Claim Frequency here - compare provinces pairwise or do an overall test.

# Create contingency table of ClaimOccurred vs Province
contingency_province = pd.crosstab(df['Province'], df['ClaimOccurred'])
chi2, p_province, dof, expected = chi2_contingency(contingency_province)
print(f"\nH0: No risk difference across provinces")
print(f"Chi-square test p-value: {p_province:.4f}")
if p_province < 0.05:
    print("=> Reject H0: Significant risk differences across provinces.\n")
else:
    print("=> Fail to reject H0: No significant risk differences across provinces.\n")

# 2) Are there risk differences between zip codes? (PostalCode)
contingency_zip = pd.crosstab(df['PostalCode'], df['ClaimOccurred'])
chi2_zip, p_zip, dof_zip, expected_zip = chi2_contingency(contingency_zip)
print(f"H0: No risk difference between zip codes")
print(f"Chi-square test p-value: {p_zip:.4f}")
if p_zip < 0.05:
    print("=> Reject H0: Significant risk differences between zip codes.\n")
else:
    print("=> Fail to reject H0: No significant risk differences between zip codes.\n")

# 3) Are there significant margin (profit) differences between zip codes?
# Use t-test between two zip codes with most data points

zip_counts = df['PostalCode'].value_counts()
top2_zip = zip_counts.index[:2].tolist()

group1_margin = df[df['PostalCode'] == top2_zip[0]]['Margin']
group2_margin = df[df['PostalCode'] == top2_zip[1]]['Margin']

t_stat, p_margin = ttest_ind(group1_margin, group2_margin, equal_var=False)
print(f"H0: No margin difference between zip codes {top2_zip[0]} and {top2_zip[1]}")
print(f"T-test p-value: {p_margin:.4f}")
if p_margin < 0.05:
    print("=> Reject H0: Significant margin differences between these zip codes.\n")
else:
    print("=> Fail to reject H0: No significant margin differences between these zip codes.\n")

# 4) Are there risk differences between Women and Men?
contingency_gender = pd.crosstab(df['Gender'], df['ClaimOccurred'])
chi2_gender, p_gender, dof_gender, expected_gender = chi2_contingency(contingency_gender)
print(f"H0: No risk difference between women and men")
print(f"Chi-square test p-value: {p_gender:.4f}")
if p_gender < 0.05:
    print("=> Reject H0: Significant risk differences between women and men.\n")
else:
    print("=> Fail to reject H0: No significant risk differences between women and men.\n")

# Optional: Summary
print("Task 3 hypothesis testing complete.")
