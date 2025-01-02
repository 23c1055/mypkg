#!/bin/bash
# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 1 ros2 launch mypkg prime_generator.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '[prime]: published prime:'
