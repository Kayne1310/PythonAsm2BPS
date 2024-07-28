import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
file_path_product = 'Product.csv'
product_data = pd.read_csv(file_path_product)

# Display the first few rows and columns of the dataframe
print(product_data.head())
print(product_data.columns)  # Verify column names

# Strip leading/trailing spaces from column names if any
product_data.columns = product_data.columns.str.strip()

# Verify data types
print(product_data.dtypes)

# Convert DateAdded to datetime
if 'DateAdded' in product_data.columns:
    product_data['DateAdded'] = pd.to_datetime(product_data['DateAdded'], format='%m/%d/%Y')

    # Create a line chart for Price over DateAdded
    plt.figure(figsize=(12, 6))
    plt.plot(product_data['DateAdded'], product_data['price'], marker='o', linestyle='-', color='r')
    plt.xlabel('Date Added')
    plt.ylabel('Price')
    plt.title('Price of Products Over Time')
    plt.grid(True)
    plt.show()
else:
    print("Column 'DateAdded' is missing from the DataFrame.")
