from sklearn.datasets import load_iris # Importing the dataset
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
# iris=load_iris()
# x,y=iris.data, iris.target
data_path="D:\\Projects\\Python\\Python-Series\\Dataset_for_Class5_Exercise\\diabetes.csv"

# print(x.shape ,y.shape)
# print(x)

df=pd.read_csv(data_path)

# x=df[['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']] # Independent variables
x=df.drop('label', axis=1) 
y=df.label # Target variable (Dependent variable)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42) 
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Support Vector Machine (SVM) Classifier

# Create and train the model
model = SVC(kernel='linear') # Support Vector Machine (SVM) Classifier model
model.fit(x_train, y_train) # Train the model
print("Model training completed using Support Vector Machine (SVM) Classifier....") # Print the message

# Predicting the values
predictions = model.predict(x_test)  # Predict the values
print("Prediction completed using Support Vector Machine (SVM) Classifier.....") # Print the message

# Calculating the error metrics
print("Confusion Matrix using Support Vector Machine (SVM) Classifier: ")
# print(confusion_matrix(y_test, predictions))
ConfusionMatrixDisplay.from_estimator(model,x_test,y_test)

print("Classification Report: ")
print(classification_report(y_test, predictions))
print("Accuracy Score using SVM: ")
print(accuracy_score(y_test, predictions))


# # Random Forest Classifier

# # Create and train the model
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
print("Accuracy Score using RFT: ")

print(accuracy_score(y_test, predictions))

# # Decision Tree Classifier

# # Create and train the model

model = DecisionTreeClassifier() # Decision Tree Classifier model
model.fit(x_train, y_train) # Train the model
print("Model training completed using Decision Tree Classifier....") # Print the message

# Predicting the values

predictions = model.predict(x_test)  # Predict the values
print("Prediction completed using Decision Tree Classifier.....") # Print the message

# Calculating the error metrics

print("Confusion Matrix using Decision Tree Classifier: ")
# print(confusion_matrix(y_test, predictions))
ConfusionMatrixDisplay.from_estimator(model,x_test,y_test)
print("Classification Report: ")
print(classification_report(y_test, predictions))
print("Accuracy Score using DTC : ")
print(accuracy_score(y_test, predictions))