import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_data_task1.csv")

# Summary statistics
summary = df[['TotalPremium', 'TotalClaims', 'CustomValueEstimate']].describe()
with open("task1_eda_output.txt", "w") as f:
    f.write("Summary Statistics:\n")
    f.write(summary.to_string())
    f.write("\n\nMissing Values:\n")
    f.write(df.isnull().sum().to_string())

# Histogram: TotalPremium
plt.figure(figsize=(8, 5))
sns.histplot(df['TotalPremium'], bins=30, kde=True)
plt.title("Distribution of TotalPremium")
plt.xlabel("TotalPremium")
plt.savefig("totalpremium_distribution.png")
plt.close()

# Boxplot: TotalClaims
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['TotalClaims'])
plt.title("Boxplot of TotalClaims")
plt.savefig("totalclaims_boxplot.png")
plt.close()

# Barplot: Loss Ratio by Province
df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
province_loss = df.groupby('Province')['LossRatio'].mean().sort_values()
plt.figure(figsize=(10, 6))
province_loss.plot(kind='barh', color='skyblue')
plt.title("Average Loss Ratio by Province")
plt.xlabel("Loss Ratio")
plt.tight_layout()
plt.savefig("loss_ratio_by_province.png")
plt.close()
