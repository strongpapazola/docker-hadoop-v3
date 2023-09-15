#!/bin/bash
docker build -t spark-examples-spark-master .
docker run -it --rm --hostname sample --net development --name sample spark-examples-spark-master
# docker run -it --rm --hostname sample --net development --name sample spark-examples-spark-master bash
# PYSPARK_PYTHON=python3 /spark/bin/spark-submit --master spark://117.53.45.158:7077 /app/wordcount.py "/input/mapreducedataset.txt"
