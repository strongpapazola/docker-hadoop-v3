import subprocess

# Define the database connection parameters
db_params = {
    'host': '117.53.45.158',
    'user': 'root',
    'password': 'passwordaman',
    'database': 'barang',
}

# Define the path where you want to save the SQL dump file
dump_file_path = 'dump.sql'

# Construct the mysqldump command
mysqldump_cmd = [
    'mysqldump',
    f'--host={db_params["host"]}',
    f'--user={db_params["user"]}',
    f'--password={db_params["password"]}',
    db_params['database'],
]

# Run the mysqldump command and save the output to the dump file
try:
    with open(dump_file_path, 'w') as dump_file:
        subprocess.run(mysqldump_cmd, stdout=dump_file, stderr=subprocess.PIPE, check=True)
    print(f'Successfully exported SQL data to {dump_file_path}')
except subprocess.CalledProcessError as e:
    print(f'Error: {e.stderr.decode()}')

from hdfs import InsecureClient

# Create an HDFS client
client = InsecureClient('http://bigdata.bisa.ai:9870', user='root')

# Specify the local file path and the HDFS destination path
local_file_path = dump_file_path
hdfs_destination_path = '/user/root/'+dump_file_path  # Adjust the HDFS path as needed

# Upload the file to HDFS
client.upload(hdfs_destination_path, local_file_path)
