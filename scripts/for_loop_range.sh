#!/bin/bash

read -p "start of the range: " r1
read -p "end of the range: " r2

sum=0

for i in $(seq $r1 $r2);
do
sum=$(( $sum + $i ))
done

echo $sum
