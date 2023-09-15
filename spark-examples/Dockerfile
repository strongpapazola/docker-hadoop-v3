# FROM bde2020/spark-python-template:3.3.0-hadoop3.3
FROM strongpapazola/hadoop-base:3.3.4-java8
	  
COPY wordcount.py /app/

# ENV SPARK_MASTER_NAME 178.128.219.248
ENV SPARK_MASTER_NAME 117.53.45.158
ENV SPARK_MASTER_PORT 7077
# ENV SPARK_MASTER_PORT 8088
# ENV SPARK_LOCAL_IP 117.53.45.158

ENV SPARK_APPLICATION_PYTHON_LOCATION /app/wordcount.py
# ENV SPARK_APPLICATION_ARGS "/spark/README.md"
ENV SPARK_APPLICATION_ARGS "/input/mapreducedataset.txt"

ENV PYSPARK_PYTHON python3
CMD ["/spark/bin/spark-submit","--master","spark://117.53.45.158:7077","/app/wordcount.py","/input/mapreducedataset.txt"]