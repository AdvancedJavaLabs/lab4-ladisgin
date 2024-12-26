#!/bin/bash

# hadoop fs -mkdir -p input
# hdfs dfs -put ./csv_files/0.csv input/0.csv

hadoop fs -mkdir -p input
hdfs dfs -put ./csv_files/* input
hadoop fs -rmr output

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-input input/0.csv \
-output output/res \
-mapper "python map.py" \
-reducer "python reduce.py" \
-file map.py \
-file reduce.py


hdfs dfs -cat output/res/part-* | python3 sort.py > result.txt
