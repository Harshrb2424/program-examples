import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic data
np.random.seed(0)
data = {
    'Age': np.random.randint(20, 80, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Blood Pressure': np.random.choice(['Normal', 'Elevated', 'High'], 100),
    'Cholesterol Level': np.random.randint(150, 300, 100),
    'Diabetes': np.random.choice(['Yes', 'No'], 100),
    'Heart Disease': np.random.choice(['Yes', 'No'], 100)
}
df = pd.DataFrame(data)

# Descriptive statistics
print("Descriptive Statistics:\n", df.describe())

# Visualizations
plt.figure(figsize=(12, 6))
sns.countplot(x='Gender', hue='Heart Disease', data=df)
plt.title('Gender vs Heart Disease')

plt.figure(figsize=(12, 6))
sns.boxplot(x='Blood Pressure', y='Age', data=df)
plt.title('Blood Pressure vs Age')
plt.show()