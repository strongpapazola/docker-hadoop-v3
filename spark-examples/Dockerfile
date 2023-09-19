FROM strongpapazola/hadoop-base:3.3.4-java8
	  
COPY . /app/

ENV SPARK_MASTER_NAME 117.53.45.158
ENV SPARK_MASTER_PORT 7077

# ENV SPARK_APPLICATION_PYTHON_LOCATION /app/wordcount.py
# ENV SPARK_APPLICATION_PYTHON_LOCATION /app/wordcount.py
# ENV SPARK_APPLICATION_ARGS "/input/mapreducedataset.txt"

#RUN pip install -q findspark
#RUN pip install hdfs pandas matplotlib seaborn numpy


ENV PYSPARK_PYTHON python3
# CMD ["/spark/bin/spark-submit","--master","spark://117.53.45.158:7077","/app/wordcount.py","/input/mapreducedataset.txt"]
CMD ["/spark/bin/spark-submit","--master","spark://117.53.45.158:7077","/app/upload.py"]
# CMD ["/spark/bin/spark-submit","--master","spark://117.53.45.158:7077","/app/spark-sample-notif.py"]
