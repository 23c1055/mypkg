#!/bin/bash
# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

set -e

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/install/setup.bash
echo "Launching ROS 2 node..."
timeout 10 ros2 launch mypkg prime_checker.launch.py &
launch_pid=$!


sleep 2


echo "Checking the /prime_check topic for valid messages..."
output=$(timeout 5 ros2 topic echo /prime_check --once)

expected_outputs=("1×" "2〇" "3〇" "4×" "5〇")

success=true
for expected in "${expected_outputs[@]}"; do
    if [[ "$output" == *"$expected"* ]]; then
        echo "Found expected output: $expected"
    else
        echo "Error: Expected output '$expected' not found in topic output"
        success=false
    fi
done

kill $launch_pid || true

if $success; then
    echo "All expected outputs were found. Test passed!"
    exit 0
else
    echo "Some expected outputs were missing. Test failed!"
    exit 1
fi
