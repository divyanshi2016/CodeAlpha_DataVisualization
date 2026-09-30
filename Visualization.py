import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset.csv")

# Show data
print("Dataset:")
print(df)

# 1. Bar Chart
plt.figure(figsize=(8, 5))
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Student Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x="StudyHours", y="Marks", data=df)
plt.title("Study Hours vs Marks")
plt.tight_layout()
plt.show()

# 3. Histogram
plt.figure(figsize=(8, 5))
sns.histplot(df["Marks"], bins=5, kde=True)
plt.title("Distribution of Marks")
plt.tight_layout()
plt.show()

# 4. Box Plot
plt.figure(figsize=(6, 5))
sns.boxplot(y=df["Marks"])
plt.title("Marks Box Plot")
plt.tight_layout()
plt.show()

print("Data Visualization Completed Successfully!")
