#!/bin/bash
#grep "device$"查找以device结尾的行
for i in $(adb devices | grep "device$" | awk '{print $1}')
do
  echo "start:{$i}"
  #&为放在后台执行，相当于并行。如果不加&相当于串行
  udid=$i pytest test_grid.py &
done