#!/bin/bash
docker rm -f sqoop
docker build -t strongpapazola/hadoop-sqoop:3.3.4-java8 .
docker run -it --rm --hostname sqoop --net development --name sqoop strongpapazola/hadoop-sqoop:3.3.4-java8
