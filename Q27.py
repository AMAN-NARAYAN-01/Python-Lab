import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Student': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10'],
    'Mathematics': [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    'Physics': [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    'Chemistry': [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    'English': [80, 84, 72, 91, 76, 80, 70, 95, 77, 89]
}
df = pd.DataFrame(data)

subjects_data = df.drop('Student', axis=1)

plt.figure(figsize=(8, 5))
sns.boxplot(data=subjects_data, palette="Set2")
plt.title("Subject-wise Score Distributions")
plt.ylabel("Scores")
plt.show()

sns.pairplot(subjects_data, diag_kind='kde', markers='o')
plt.suptitle("Pairwise Relationships Between Subjects", y=1.02)
plt.show()

plt.figure(figsize=(6, 5))
correlation_matrix = subjects_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Subject Score Correlation Heatmap")
plt.show()
