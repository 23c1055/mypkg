#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 1 ros2 launch mypkg prime_generator.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'published prime'
