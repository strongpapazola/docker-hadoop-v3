from hdfs import InsecureClient

# Create an HDFS client
client = InsecureClient('http://bigdata.bisa.ai:9870', user='root')

# Specify the local file path and the HDFS destination path
# local_file_path = '/root/docker-hadoop-v3/README.md'
local_file_path = '/root/diabetes.csv'
local_file_path = '/root/deepglobe-road-extraction-dataset.zip'
hdfs_destination_path = '/deepglobe-road-extraction-dataset.zip'  # Adjust the HDFS path as needed

# Upload the file to HDFS
client.upload(hdfs_destination_path, local_file_path)
