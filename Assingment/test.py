import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the dataset
data_path = "D:\\Projects\\Python\\Python-Series\\Dataset_for_Class5_Exercise\\Boston - Boston.csv"
data_frame = pd.read_csv(data_path)

# Define independent variables (features) and dependent variable (target)
x = data_frame[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'LSTAT']]
y = data_frame['MEDV']

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(x_train, y_train)
print("Model training completed")

# Predicting the MEDV based on the independent variables
predictions = model.predict(x_test)
print("Prediction completed")

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
plt.xlabel("Index")
plt.ylabel("MEDV")
plt.title("Actual vs Predicted values")
plt.legend()
plt.show()

# Function to take user input and make predictions
def predict_medv():
    print("Enter the following values for prediction:")
    CRIM = float(input("CRIM (per capita crime rate by town): "))
    ZN = float(input("ZN (proportion of residential land zoned for lots over 25,000 sq. ft.): "))
    INDUS = float(input("INDUS (proportion of non-retail business acres per town): "))
    CHAS = int(input("CHAS (Charles River dummy variable (1 if tract bounds river; 0 otherwise)): "))
    NOX = float(input("NOX (nitric oxides concentration (parts per 10 million)): "))
    RM = float(input("RM (average number of rooms per dwelling): "))
    AGE = float(input("AGE (proportion of owner-occupied units built prior to 1940): "))
    DIS = float(input("DIS (weighted distances to five Boston employment centres): "))
    RAD = int(input("RAD (index of accessibility to radial highways): "))
    TAX = float(input("TAX (full-value property tax rate per $10,000): "))
    PTRATIO = float(input("PTRATIO (pupil-teacher ratio by town): "))
    LSTAT = float(input("LSTAT (percentage lower status of the population): "))

    user_input = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, LSTAT]])
    prediction = model.predict(user_input)
    print(f"Predicted MEDV: {prediction[0]}")

# Call the prediction function to get user input
predict_medv()
