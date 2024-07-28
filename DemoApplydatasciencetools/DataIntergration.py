from pyspark.sql import SparkSession

# Initializing Spark session
spark = SparkSession.builder.appName('ABC Manufacturing').getOrCreate()

# Absolute paths to the CSV files
sales_data_path = r'C:\Users\PC\PycharmProjects\tesst\.venv\DemoFileCsv\sales_data.csv'
inventory_data_path = r'C:\Users\PC\PycharmProjects\tesst\.venv\DemoFileCsv\inventory_data.csv'
production_data_path = r'C:\Users\PC\PycharmProjects\tesst\.venv\DemoFileCsv\production_data.csv'

# Reading data from various sources
sales_df = spark.read.csv(sales_data_path, header=True, inferSchema=True)
inventory_df = spark.read.csv(inventory_data_path, header=True, inferSchema=True)
production_df = spark.read.csv(production_data_path, header=True, inferSchema=True)

# Merging data
integrated_df = sales_df.join(inventory_df, on='product_id').join(production_df, on='product_id')

# Show integrated data
integrated_df.show()
