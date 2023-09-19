from hdfs import InsecureClient

# Create an HDFS client
client = InsecureClient('http://bigdata.bisa.ai:9870', user='root')

# Specify the local file path and the HDFS destination path
hdfs_destination_path = '/deepglobe-road-extraction-dataset.zip'  # Adjust the HDFS path as needed
local_file_path = '/root/deepglobe-road-extraction-dataset.zip.2'

# Upload the file to HDFS
client.download(hdfs_destination_path, local_file_path)
