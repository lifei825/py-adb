#!/bin/bash

id=BTFDU17318000996

game(){
while true;do
  sleep 1
adb -s $id shell input tap 904 1392
sleep 3
adb -s $id shell input tap 538 1457
adb -s $id shell input tap 917 1250
done
}

chifan(){
  while true;do
    adb -s $id shell input tap 526 668;
    sleep 4;
    adb -s $id shell input tap 534 1033;
  done
}

sp(){
  while true; do
    adb -s $id shell input tap 928 1034
    sleep 3
    adb -s $id shell input tap 558 1287
    sleep 35
    adb -s $id shell input tap 960 96
    sleep 2
    adb -s $id shell input tap 525 1283
    sleep 35
    adb -s $id shell input tap 960 96
    sleep 2
    adb -s $id shell input tap 903 553
    sleep 3
  done

}

if [ $1 == chifan ];then
    chifan
elif [ $1 == game ]; then
    game
elif [ $1 == sp ]; then
    sp
fi
