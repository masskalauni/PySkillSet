# Predict MEDV based on other independent variables given on the following dataset.

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the dataset
data_path = "D:\\Projects\\Python\\Python-Series\\Dataset_for_Class5_Exercise\\Boston - Boston.csv"
data_frame = pd.read_csv(data_path)

# print(data_frame.head())
# COLUMNS OF DATA SET
# print(data_frame.columns)

x=data_frame[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'LSTAT']]  # Independent variables
y=data_frame.MEDV  # Target variable (Dependent variable)

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)


# Create and train the model
model = LinearRegression() # Linear Regression model
model.fit(x_train, y_train) # Train the model
print("Model training completed") # Print the message

# Predicting the MEDV based on the independent variables

predictions = model.predict(x_test)  # Predict the values
print("Prediction completed") # Print the message

# Calculating the error metrics
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print("Mean Squared Error: ", mse)
print("Mean Absolute Error: ", mae)
print("R2 Score: ", r2)


# Plotting the actual vs predicted values

plt.scatter(range(len(y_test)), y_test, color='blue', label='Actual values')
plt.scatter(range(len(predictions)), predictions, color='red', label='Predicted values')
plt.title("Actual vs Predicted values")
plt.show()
