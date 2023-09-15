#!/bin/bash
docker build -t strongpapazola/hadoop-base:3.3.4-java8 base/.

docker build -t strongpapazola/hadoop-namenode:3.3.4-java8 namenode/.
docker build -t strongpapazola/hadoop-datanode:3.3.4-java8 datanode/.

docker build -t strongpapazola/hadoop-resourcemanager:3.3.4-java8 resourcemanager/.
docker build -t strongpapazola/hadoop-nodemanager:3.3.4-java8 nodemanager/.

docker build -t strongpapazola/hadoop-historyserver:3.3.4-java8 historyserver/.

docker build -t strongpapazola/hadoop-submit:3.3.4-java8 submit/.
# USINGCOMPOSEEE docker run -it --rm --name submit strongpapazola/hadoop-submit:3.3.4-java8 

docker build -t strongpapazola/hadoop-sqoop:3.3.4-java8 sqoop/.
# USINGCOMPOSEEE docker run -it --rm --name sqoop strongpapazola/hadoop-sqoop:3.3.4-java8 

docker build -t strongpapazola/hadoop-flume:3.3.4-java8 flume/.
# USINGCOMPOSEEE docker run -it --rm --name flume strongpapazola/hadoop-flume:3.3.4-java8 

docker build -t strongpapazola/hadoop-zookeeper:3.3.4-java8 zookeeper/.
# USINGCOMPOSEEE docker run -it --rm --name zookeeper strongpapazola/hadoop-zookeeper:3.3.4-java8 


docker build -t strongpapazola/hadoop-spark-master:3.3.4-java8 spark-master/.
docker build -t strongpapazola/hadoop-spark-worker:3.3.4-java8 spark-worker/.