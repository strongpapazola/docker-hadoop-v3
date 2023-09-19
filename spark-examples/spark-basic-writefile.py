from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("WriteToHDFS")
sc = SparkContext(conf=conf)

# Create an RDD or DataFrame with the data you want to write to HDFS
# For example, let's say you have a list of strings:
data_to_write = ["Line 1", "Line 2", "Line 3"]

# Convert the data to an RDD
rdd = sc.parallelize(data_to_write)

# Coalesce the RDD to a single partition
rdd = rdd.coalesce(1)

# Define the HDFS output path where you want to write the data
output_path = "hdfs://117.53.45.158:9000/testwrite.txt"

# Use the saveAsTextFile method to write the data to HDFS
rdd.saveAsTextFile(output_path)

# Stop the SparkContext when you're done
sc.stop()
