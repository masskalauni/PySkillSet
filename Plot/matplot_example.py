# Add the required libraries
import matplotlib.pyplot as plt

# Create the data
x = [1,3,5,7,9,11]
y = [10,25,35,33,41,59]

# Let's plot the data
plt.plot(x, y,label='Series-1', color='blue')


# Create the data
x = [2,4,6,8,10,12]
y = [15,29,32,33,38,55]

# Plot the data
plt.plot(x, y, label='Series-2', color='red')


# Add X Label on X-axis
plt.xlabel("X-label")

# Add X Label on X-axis
plt.ylabel("Y-label")

# Append the title to graph
plt.title("Multiple Python Line Graph")

# Add legend to graph
plt.legend()

# Display the plot
plt.show()



import numpy as np
import pandas as pd
from sklearn.model_selection train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Create the data
x = np.array([1,3,5,7,9,11]).reshape(-1,1)