import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
cleaned_file_path = 'C:/Users/PC/PycharmProjects/tesst/.venv/DemoFileCsv/cleaned_Product.csv'
cleaned_data = pd.read_csv(cleaned_file_path)

# Strip spaces from column names if not done already
cleaned_data.columns = cleaned_data.columns.str.strip()

# Convert DateAdded to datetime
cleaned_data['DateAdded'] = pd.to_datetime(cleaned_data['DateAdded'])

# Bar Chart for Product Rating Distribution
plt.figure(figsize=(10, 6))
cleaned_data['ProductRating'].value_counts().sort_index().plot(kind='bar')
plt.title('Product Rating Distribution')
plt.xlabel('Product Rating')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# Histogram for Price Distribution
plt.figure(figsize=(10, 6))
plt.hist(cleaned_data['price'], bins=20, edgecolor='k')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

