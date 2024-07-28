from pyspark.streaming import StreamingContext

# Initializing Spark Streaming context
ssc = StreamingContext(spark.sparkContext, 10)  # Batch interval of 10 seconds

# Creating a DStream from real-time data source
lines = ssc.socketTextStream('localhost', 9999)

# Processing real-time data
def process_rdd(time, rdd):
    # Convert RDD to DataFrame
    df = spark.read.json(rdd)
    df.show()

lines.foreachRDD(process_rdd)
ssc.start()
ssc.awaitTermination()
