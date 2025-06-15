import pandas as pd
from scipy.stats import ttest_ind

# Load data
df = pd.read_csv('cleaned_MachineLearningRating.csv', low_memory=False)

print("Columns available in dataset:")
print(df.columns.tolist())

# Check unique values in 'CoverGroup'
print("\nUnique groups in 'CoverGroup':")
print(df['CoverGroup'].unique())

# Define your two groups exactly as they appear in your data
group_a_name = 'Comprehensive - Taxi'
group_b_name = 'Third Party Only'

# Filter groups
group_a = df[df['CoverGroup'] == group_a_name]
group_b = df[df['CoverGroup'] == group_b_name]

print(f"\nGroup A ({group_a_name}) size: {len(group_a)}")
print(f"Group B ({group_b_name}) size: {len(group_b)}")

# Summary stats for TotalPremium
print("\nSummary stats for TotalPremium:")
print(f"Group A mean: {group_a['TotalPremium'].mean()}, std: {group_a['TotalPremium'].std()}")
print(f"Group B mean: {group_b['TotalPremium'].mean()}, std: {group_b['TotalPremium'].std()}")

# Perform independent t-test (assuming independent samples)
t_stat, p_value = ttest_ind(group_a['TotalPremium'].dropna(), group_b['TotalPremium'].dropna(), equal_var=False)

print(f"\nT-test results: t-statistic = {t_stat:.4f}, p-value = {p_value:.4f}")

if p_value < 0.05:
    print("Result: Statistically significant difference between groups (reject null hypothesis)")
else:
    print("Result: No statistically significant difference between groups (fail to reject null hypothesis)")
