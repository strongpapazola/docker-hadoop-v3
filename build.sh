#!/bin/bash
docker build -t strongpapazola/hadoop-base:3.3.4-java8 base/.

docker build -t strongpapazola/hadoop-namenode:3.3.4-java8 namenode/.
docker build -t strongpapazola/hadoop-datanode:3.3.4-java8 datanode/.

docker build -t strongpapazola/hadoop-resourcemanager:3.3.4-java8 resourcemanager/.
docker build -t strongpapazola/hadoop-nodemanager:3.3.4-java8 nodemanager/.

docker build -t strongpapazola/hadoop-historyserver:3.3.4-java8 historyserver/.

docker build -t strongpapazola/hadoop-submit:3.3.4-java8 submit/.


