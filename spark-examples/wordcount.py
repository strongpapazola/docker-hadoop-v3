import sys
from operator import add

from pyspark.sql import SparkSession

# Function to split lines into words
def split_line(line):
    return line.split(' ')

# Function to create key-value pairs with a count of 1 for each word
def create_key_value_pairs(word):
    return (word, 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    # Read the input file and convert it into an RDD of lines
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    
    # Split lines into words
    words = lines.flatMap(split_line)

    # Create key-value pairs with a count of 1 for each word
    word_count_pairs = words.map(create_key_value_pairs)

    # Reduce by key to count the occurrences of each word
    counts = word_count_pairs.reduceByKey(add)

    # Collect the results and print them
    output = counts.collect()
    write = []
    for (word, count) in output:
        print("%s: %i" % (word, count))    
        write.append("%s: %i" % (word, count))


    # from pyspark import SparkConf, SparkContext
    sc = spark.sparkContext

    # # Convert the data to an RDD
    rdd = sc.parallelize(write)

    # Coalesce the RDD to a single partition
    output = rdd.coalesce(1)

    # Define the HDFS output path where you want to write the data
    output_path = "hdfs://117.53.45.158:9000/testwrite"

    # Use the saveAsTextFile method to write the data to HDFS
    output.saveAsTextFile(output_path)

    spark.stop()
