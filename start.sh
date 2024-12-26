#!/bin/bash

hadoop fs -mkdir -p input
# hdfs dfs -put ./csv_files/* input
hdfs dfs -put ./csv_files/0.csv input/0.csv
# hdfs dfs -put ./csv_files/1.csv input/1.csv
# hadoop fs -rmr output

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-input input \
-output output/res \
-mapper "python map.py" \
-reducer "python reduce.py" \
-file map.py \
-file reduce.py

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-input output/res \
-output output/res_sort \
-mapper "python map.py" \
-reducer "python sort.py" \
-file map.py \
-file sort.py


hdfs dfs -cat output/res_sort/part-*
