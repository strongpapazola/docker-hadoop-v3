#!/bin/bash
docker rm -f zookeeper-server
docker build -t strongpapazola/hadoop-zookeeper:3.3.4-java8 .
docker run -d -p 2181:2181 -p 8082:8080 --hostname zookeeper-server --net development --name zookeeper-server strongpapazola/hadoop-zookeeper:3.3.4-java8
