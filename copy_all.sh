#!/bin/bash

docker cp map.py hadoop-master:/root
docker cp reduce.py hadoop-master:/root

docker cp map2.py hadoop-master:/root
docker cp sort.py hadoop-master:/root

docker cp csv_files hadoop-master:/root

docker cp start.sh hadoop-master:/root
