#!/bin/bash
mix2s () {
#/usr/bin/python3 main.py -d mix2s -t round_all
/usr/bin/nohup /usr/bin/python3 -u  /root/py-adb/main.py -d mix2s -t round_all > mix2s.out 2>&1 &
}

huawei() {
/usr/bin/python3 main.py -d huawei -t round_all
}

redmi() {
/usr/bin/nohup /usr/bin/python3 -u  /root/py-adb/main.py -d redmi -t round_all > redmi.out 2>&1 &
}


#if ! /usr/bin/ps -ef | grep $1 | grep -v grep &>/dev/null;then 
if ! /usr/bin/ps -ef | /usr/bin/grep "$1 -t round_all" | /usr/bin/grep -v grep;then 
	if [ $1 == 'mix2s' ];then
	 mix2s
	elif [ $1 == 'redmi' ];then
	 redmi
	elif [ $1 == 'huawei' ];then
	 huawei
	fi
else
	/usr/bin/echo $1 already running
fi
