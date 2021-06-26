#!/bin/bash

id=192.168.1.26:5554


sp(){
  while true; do
    adb -s $id shell input tap 619 685
    sleep 3
    adb -s $id shell input tap 368 1066
    sleep 35
    adb -s $id shell input tap 642 122
    sleep 2
    adb -s $id shell input tap 600 490
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
