import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load data
df = pd.read_csv('cleaned_MachineLearningRating.csv', low_memory=False)

print("Columns available in dataset:")
print(df.columns.tolist())

# Define groups
group_a_name = 'Comprehensive - Taxi'
group_b_name = 'Third Party Only'

print("\nUnique groups in 'CoverGroup':")
print(df['CoverGroup'].unique())

group_a = df[df['CoverGroup'] == group_a_name]['TotalPremium'].dropna()
group_b = df[df['CoverGroup'] == group_b_name]['TotalPremium'].dropna()

print(f"\nGroup A ({group_a_name}) size: {len(group_a)}")
print(f"Group B ({group_b_name}) size: {len(group_b)}")

print("\nSummary stats for TotalPremium:")
print(f"Group A mean: {group_a.mean()}, std: {group_a.std()}")
print(f"Group B mean: {group_b.mean()}, std: {group_b.std()}")

# T-test
t_stat, p_val = ttest_ind(group_a, group_b, equal_var=False)
print(f"\nT-test results: t-statistic = {t_stat:.4f}, p-value = {p_val:.4f}")

if p_val < 0.05:
    print("Result: Statistically significant difference between groups (reject null hypothesis)")
else:
    print("Result: No statistically significant difference (fail to reject null hypothesis)")

# Plot Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='CoverGroup', y='TotalPremium', data=df[df['CoverGroup'].isin([group_a_name, group_b_name])])
plt.title('Total Premium Distribution by Cover Group')
plt.ylabel('Total Premium')
plt.xlabel('Cover Group')
plt.show()

# Plot Histogram
plt.figure(figsize=(10, 6))
sns.histplot(group_a, color='blue', label=group_a_name, kde=True, stat="density", bins=50)
sns.histplot(group_b, color='orange', label=group_b_name, kde=True, stat="density", bins=50)
plt.title('Total Premium Histogram by Cover Group')
plt.xlabel('Total Premium')
plt.ylabel('Density')
plt.legend()
plt.show()
