from pyspark.sql import SparkSession
import zipfile

# Initialize a SparkSession
#spark-submit --master spark://117.53.45.158:7077 spark-template-jobs.py
spark = SparkSession.builder.appName("SparkJobEkstrak").getOrCreate()

def extract_zip(contents):
    import io
    import zipfile

    with zipfile.ZipFile(io.BytesIO(contents), 'r') as zip_ref:
        zip_ref.extractall("/globeextracted")

zip_file_path = "hdfs:///deepglobe-road-extraction-dataset.zip"
zip_rdd = spark.sparkContext.binaryFiles(zip_file_path).values()

zip_rdd.foreach(extract_zip)

spark.stop()
