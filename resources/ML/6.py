import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn import metrics  
import seaborn as sns  
from sklearn.datasets import load_iris  
from sklearn.model_selection import train_test_split  
from sklearn.tree import DecisionTreeClassifier  
from sklearn import tree  

# Loading the dataset  
iris = load_iris()  

# Converting the data to a pandas dataframe  
data = pd.DataFrame(data = iris.data, columns = iris.feature_names)  

# Creating a separate column for the target variable of iris dataset   
data['Species'] = iris.target  

# Replacing the categories of target variable with the actual names of the species  
target_dict = dict(zip(np.unique(iris.target), iris.target_names))  
data['Species'] = data['Species'].replace(target_dict)  

# Separating the independent and dependent variables of the dataset  
X = data.drop(columns="Species")  
y = data["Species"]  

# Splitting the dataset into training and testing datasets  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=93)  

# Creating an instance of the Decision Tree classifier class  
dtc = DecisionTreeClassifier(max_depth=3, random_state=93)  

# Fitting the training dataset to the model  
dtc.fit(X_train, y_train)  

# Plotting the Decision Tree with modern colors and a clean look  
plt.figure(figsize=(18, 10))  
tree.plot_tree(dtc, feature_names=X.columns, class_names=y.unique(), rounded=True, filled=True, fontsize=12)  
plt.title('Decision Tree Visualization', fontsize=16)  
plt.show()  

# Predicting with the test data  
y_pred = dtc.predict(X_test)  

# Finding the confusion matrix  
conf_matrix = metrics.confusion_matrix(y_test, y_pred)  
conf_matrix_df = pd.DataFrame(conf_matrix, index=y.unique(), columns=y.unique())  

# Plotting the confusion matrix as a heatmap  
plt.figure(figsize=(8, 6))  
sns.heatmap(conf_matrix_df, annot=True, fmt="g", cmap="coolwarm", cbar=True, linewidths=1, linecolor='gray')  
plt.title('Confusion Matrix', fontsize=16)  
plt.xlabel('Predicted Labels', fontsize=12)  
plt.ylabel('True Labels', fontsize=12)  
plt.xticks(rotation=45)  
plt.yticks(rotation=0)  
plt.show()  
