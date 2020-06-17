#!/bin/bash

make
./Pfaults 180 &
pid=$!

sudo perf stat -e cache-misses,dTLB-load-misses,page-faults -p $pid sleep 0
free

i=0
while [ $i -le 6 ]
do
  sudo perf stat -e cache-misses,dTLB-load-misses,page-faults -p $pid sleep 60
  free
  ((i++))
done

make clean
