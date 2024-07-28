import pandas as pd

# Load the data
file_path = 'Product.csv'
data = pd.read_csv(file_path)

# Strip spaces from column names
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
# Convert DateAdded to datetime if it exists
if 'DateAdded' in cleaned_data.columns:
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

# Save cleaned data to a new CSV file
cleaned_file_path = 'C:/Users/PC/PycharmProjects/tesst/.venv/DemoFileCsv/cleaned_Product.csv'
cleaned_data.to_csv(cleaned_file_path, index=False)

# Display cleaned data
print("\nCleaned Data:")
print(cleaned_data.head())
