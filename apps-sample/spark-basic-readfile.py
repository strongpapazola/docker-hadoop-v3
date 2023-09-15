from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("ReadHDFS")
sc = SparkContext(conf=conf)
data = sc.textFile("hdfs://bisa.ai:9000/input/lunak.id2.txt")

num_lines = data.count()
print(f"Number of lines: {num_lines}")

first_lines = data.take(5)
for line in first_lines:
    print(line)

sc.stop()
# hdfs dfs -put file /home
