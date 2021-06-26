#!/bin/bash

id=192.168.1.22:5555

game(){
while true;do
  sleep 1
#adb -s $id shell input tap 71 497
#adb -s $id shell input tap 1034 384
#adb -s $id shell input tap 983 347
adb -s $id shell input tap 568 1574
adb -s $id shell input tap 531 1518
adb -s $id shell input tap 523 1049
adb -s $id shell input tap 994 1696
#adb -s $id shell input tap 1034 384

sleep 10
adb -s $id shell input tap 983 347
done
}

chifan(){
  while true;do
    adb -s $id shell input tap 526 668;
    sleep 4;
    adb -s $id shell input tap 534 1033;
  done
}

if [ $1 == chifan ];then
    chifan
elif [ $1 == game ]; then
    game
fi
