import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV
file_path = 'CustomerTable_VN.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(data.head())

# Convert TrendDate to datetime
data['TrendDate'] = pd.to_datetime(data['TrendDate'], format='%m/%d/%Y')

# Create a line plot
plt.figure(figsize=(12, 6))
sns.lineplot(x='TrendDate', y='SalesVolume', data=data)
plt.xlabel('Date')
plt.ylabel('Sales Volume')
plt.title('Sales Volume Over Time')
plt.grid(True)
plt.show()
