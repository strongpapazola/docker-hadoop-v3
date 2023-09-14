#!/bin/bash

$HADOOP_HOME/bin/hadoop dfs -mkdir /input
$HADOOP_HOME/bin/hadoop dfs -put mapreducedataset.txt /input/
$HADOOP_HOME/bin/hadoop dfs -rm -r /output
$HADOOP_HOME/bin/hadoop jar $JAR_FILEPATH $CLASS_TO_RUN $PARAMS
