#!/bin/sh

 echo “Testando o comando seq”
 
 for i in $(seq 0 9);
  do
   echo "i: $i"
   mv 'dataset-no-drone-perfect 00'$i'.jpg' 00$i.jpg
 done

  for i in $(seq 10 99);
  do
   echo "i: $i"
   mv 'dataset-no-drone-perfect 0'$i'.jpg' 0$i.jpg
 done

 for i in $(seq 100 375);
  do
   echo "i: $i"
   mv 'dataset-no-drone-perfect '$i'.jpg' $i.jpg
 done

