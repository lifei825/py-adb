#!/bin/bash
mix2s () {
python3 main.py -d mix2s -t round_all
}

huawei() {
python3 main.py -d huawei -t round_all
}

redmi() {
python3 main.py -d redmi -t round_all
}

if [ $1 == 'mix2s' ];then
 mix2s
elif [ $1 == 'redmi' ];then
 redmi
elif [ $1 == 'huawei' ];then
 huawei
fi
