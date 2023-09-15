from hdfs import InsecureClient

# Create an HDFS client
client = InsecureClient('http://bigdata.bisa.ai:9870', user='root')

# Specify the local file path and the HDFS destination path
hdfs_destination_path = '/README.md'  # Adjust the HDFS path as needed
local_file_path = '/root/docker-hadoop-v3/README.md'

# Upload the file to HDFS
client.download(hdfs_destination_path, local_file_path)
