"""
Assignment-01 - Programming Question 1
Linear Regression on Study Hours vs Performance
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample dataset (Hours vs Performance)
# You can replace this with the actual study_vs_perf dataset from class
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
performance = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(hours, performance)

# Predict performance for a student who studies 20 hours
prediction = model.predict([[20]])

print("Predicted performance for 20 hours of study:", round(prediction[0], 2))
print("Model slope (m):", round(model.coef_[0], 2))
print("Model intercept (b):", round(model.intercept_, 2))