import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the dataset
data_path = "D:\\Projects\\Python\\Python-Series\\Dataset_for_Class5_Exercise\\HR_comma_sep - HR_comma_sep.csv"
data_frame = pd.read_csv(data_path)

# Encode categorical variables
data_frame['salary'] = LabelEncoder().fit_transform(data_frame['salary'])
data_frame = pd.get_dummies(data_frame, columns=['Departments'])

# Define independent and dependent variables
x = data_frame[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours',
                'time_spend_company', 'Work_accident', 'left', 'promotion_last_5years',] + 
               [col for col in data_frame.columns if 'Departments_' in col]]
y = data_frame.salary

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Create and train the model
model = LinearRegression()
model.fit(x_train, y_train)
print("Model training completed")

# Predicting the salary based on the independent variables
predictions = model.predict(x_test)
print("Prediction completed")

# Calculating the error metrics
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print("Mean Squared Error: ", mse)
print("Mean Absolute Error: ", mae)
print("R2 Score: ", r2)
