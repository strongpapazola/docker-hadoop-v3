from pyspark.sql import SparkSession
import time
from os import system

# Initialize a SparkSession
#spark-submit --master spark://117.53.45.158:7077 spark-template-jobs.py
spark = SparkSession.builder.appName("AnalisisSayaDeepLearning").getOrCreate()

# Define a sample function to process data (replace with your actual processing logic)
def process_data(data):
    # Simulate data processing
    return data * 2

try:
    # Start your while loop with a 10-second timeout
    start_time = time.time()
    while True:
        # Replace this with your data source or generation logic
        data = [1, 2, 3, 4, 5]

        # Process the data
        processed_data = process_data(data)

        # Replace this with your data sink logic (e.g., writing to a file or database)
        print(processed_data)

        # Check if 10 seconds have elapsed
        if time.time() - start_time >= 5:
            break

finally:
    # Stop the SparkSession when you're done
    spark.stop()
