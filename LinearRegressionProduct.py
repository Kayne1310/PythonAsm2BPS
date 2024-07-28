import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the data
file_path = 'Product.csv'
data = pd.read_csv(file_path)

# Strip trailing spaces from column names
data.columns = data.columns.str.strip()

# Display initial data
print("Initial Data:")
print(data.head())

# Handling missing values
# Drop rows with any missing values
cleaned_data = data.dropna()

# Removing duplicates
# Drop duplicate rows
cleaned_data = cleaned_data.drop_duplicates()

# Correcting data types
# Convert DateAdded to datetime
cleaned_data['DateAdded'] = pd.to_datetime(cleaned_data['DateAdded'])

# Ensure other columns have appropriate data types
cleaned_data['ProductID'] = cleaned_data['ProductID'].astype(int)
cleaned_data['ProductGroupID'] = cleaned_data['ProductGroupID'].astype(int)
cleaned_data['SupplierID'] = cleaned_data['SupplierID'].astype(int)
cleaned_data['price'] = cleaned_data['price'].astype(float)
cleaned_data['Cost'] = cleaned_data['Cost'].astype(float)
cleaned_data['StockQuantity'] = cleaned_data['StockQuantity'].astype(int)
cleaned_data['ProductRating'] = cleaned_data['ProductRating'].astype(int)
cleaned_data['ReorderLevel'] = cleaned_data['ReorderLevel'].astype(int)

# Feature engineering: Extract year and month from DateAdded
cleaned_data['YearAdded'] = cleaned_data['DateAdded'].dt.year
cleaned_data['MonthAdded'] = cleaned_data['DateAdded'].dt.month

# Define target and features
# Assuming 'Sales' is a column in the data
# Since 'Sales' is not provided in the sample data, let's assume 'StockQuantity' as a proxy for demonstration
target = 'StockQuantity'
features = ['price', 'ProductRating', 'YearAdded', 'MonthAdded']

# Prepare data for modeling
X = cleaned_data[features]
y = cleaned_data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluate the model
mae_train = mean_absolute_error(y_train, y_pred_train)
mse_train = mean_squared_error(y_train, y_pred_train)
r2_train = r2_score(y_train, y_pred_train)

mae_test = mean_absolute_error(y_test, y_pred_test)
mse_test = mean_squared_error(y_test, y_pred_test)
r2_test = r2_score(y_test, y_pred_test)

print(f"Training MAE: {mae_train}, MSE: {mse_train}, R2: {r2_train}")
print(f"Testing MAE: {mae_test}, MSE: {mse_test}, R2: {r2_test}")

# Use the model to make predictions on new data
new_data = pd.DataFrame({
    'price': [7000],
    'ProductRating': [4],
    'YearAdded': [2024],
    'MonthAdded': [7]
})
predicted_stock_quantity = model.predict(new_data)
print(f"Predicted Stock Quantity: {predicted_stock_quantity[0]}")
