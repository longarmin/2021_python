#!/bin/bash
#arg1 = day number
#arg2 = session value -  Go to https://adventofcode.com/2021/day/3/input, right-click, inspect, tab over to network, click refresh, click input, click cookies, and grab the value for session.
echo 'Day'$1
DIR='Day'$1
echo $DIR
cd $DIR
curl https://adventofcode.com/2021/day/$1/input --cookie "session=$2" > in.txt
