import pymysql  # Use the appropriate library for your database

# Database connection parameters
db_params = {
    'host': '117.53.45.158',
    'user': 'root',
    'password': 'passwordaman',
    'database': 'barang',
}

# Establish a database connection
conn = pymysql.connect(**db_params)

import pandas as pd

# SQL query to fetch data (replace with your query)
sql_query = "SELECT * FROM barang"

# Execute the query and fetch data into a DataFrame
data_df = pd.read_sql(sql_query, conn)

print(data_df)

# exit()
# Export data to a CSV file
csv_file = 'barang.csv'
data_df.to_csv(csv_file, index=False)  # Specify the desired file name

# Close the database connection
conn.close()


from hdfs import InsecureClient

# Create an HDFS client
client = InsecureClient('http://bigdata.bisa.ai:9870', user='root')

# Specify the local file path and the HDFS destination path
local_file_path = csv_file
hdfs_destination_path = '/'+csv_file  # Adjust the HDFS path as needed

# Upload the file to HDFS
client.upload(hdfs_destination_path, local_file_path)
