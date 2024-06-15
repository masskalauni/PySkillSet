#Solve the diabetes classification problem using Decision Tree and Random Forest Algorithm. The dataset is already provided in the classroom (diabetes.csv).

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,ConfusionMatrixDisplay

# Importing the dataset
data_path="D:\\Projects\\Python\\Python-Series\\Dataset_for_Class5_Exercise\\diabetes.csv"

df=pd.read_csv(data_path)

# print(df.head())
# print(df.columns)
# print(df.shape)
# print(df.tail())

# x=df.iloc[:, :-1].values
x=df[['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']] # Independent variables
y=df.label # Target variable (Dependent variable)

# print(x.shape, y.shape)

# Splitting the dataset into the Training set and Test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)


# Decision Tree Classifier

# Create and train the model
model = DecisionTreeClassifier() # Decision Tree Classifier model
model.fit(x_train, y_train) # Train the model
print("Model training completed using Decision Tree Classifier....") # Print the message

# Predicting the values
predictions = model.predict(x_test)  # Predict the values
print("Prediction completed using Decision Tree Classifier.....") # Print the message

# Calculating the error metrics
print("Confusion Matrix using Decision Tree Classifier: ")
# print(confusion_matrix(y_test, predictions
ConfusionMatrixDisplay.from_estimator(model,x_test,y_test)

print("Classification Report: ")
print(classification_report(y_test, predictions))
print("Accuracy Score: ")
print(accuracy_score(y_test, predictions))

# Random Forest Classifier

# Create and train the model
model = RandomForestClassifier(n_estimators=100) # Here, n_estimators=100 means that the random forest will consist of 100 individual decision trees.
model.fit(x_train, y_train) # Train the model
print("Model training completed using Random Forest Classifier....") # Print the message

# Predicting the values
predictions = model.predict(x_test)  # Predict the values
print("Prediction completed using Random Forest Classifier.....") # Print the message

# Calculating the error metrics
print("Confusion Matrix using Random Forest Classifier: ")
# print(confusion_matrix(y_test, predictions))
ConfusionMatrixDisplay.from_estimator(model,x_test,y_test)
print("Classification Report: ")
print(classification_report(y_test, predictions))
print("Accuracy Score: ")
print(accuracy_score(y_test, predictions))



