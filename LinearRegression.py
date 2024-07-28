import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

file_path = 'CustomerTable_VN.csv'
data = pd.read_csv(file_path)

print(data.head())

# Step1: Forward fill NaN values
data.ffill(inplace=True)

# Step2: Convert categorical variables into dummy/indicator variables
data = pd.get_dummies(data)

# Step3: Define target variable
target_variable = 'SalesGrowthRate'

if target_variable not in data.columns:
    raise KeyError(f"{target_variable} is not in data: {data.columns}")

X = data.drop(target_variable, axis=1)
Y = data[target_variable]

# Step4: Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Step5: Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define and Train Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, y_pred)
r2 = r2_score(Y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Save model and scaler
joblib.dump(model, 'Linear_regression_model.joblib')
joblib.dump(scaler, 'scaler.joblib')

# Plotting the result
plt.figure(figsize=(10,6))
plt.scatter(Y_test, y_pred, color='blue', edgecolor='k', alpha=0.7)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'k--', lw=3)

plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Linear Regression: Actual vs Predicted')
plt.grid(True)
plt.show()
