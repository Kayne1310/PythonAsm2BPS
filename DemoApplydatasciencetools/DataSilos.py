import pandas as pd

# Absolute paths to the CSV files
sales_data_path = r'C:\Users\PC\PycharmProjects\tesst\.venv\DemoFileCsv\sales_data.csv'
inventory_data_path = r'C:\Users\PC\PycharmProjects\tesst\.venv\DemoFileCsv\inventory_data.csv'
production_data_path = r'C:\Users\PC\PycharmProjects\tesst\.venv\DemoFileCsv\production_data.csv'

# Reading data from different sources
sales_data = pd.read_csv(sales_data_path)
inventory_data = pd.read_csv(inventory_data_path)
production_data = pd.read_csv(production_data_path)

# Merging data from different departments
integrated_data = pd.merge(sales_data, inventory_data, on='product_id')
integrated_data = pd.merge(integrated_data, production_data, on='product_id')

# Save integrated data to a new CSV file
integrated_data.to_csv(r'C:\Users\PC\PycharmProjects\tesst\.venv\DemoFileCsv\integrated_data.csv', index=False)

print(integrated_data)
