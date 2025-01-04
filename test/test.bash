#!/bin/bash
# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

set -e
dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws
colcon build
source install/setup.py
echo "Launching ROS 2 node..."
timeout 5 ros2 launch mypkg prime_checker.launch.py &
launch_pid=$!  

sleep 2


echo "Checking the /prime_check topic for valid messages..."
output=$(timeout 3 ros2 topic echo /prime_check --once)


expected_primes=(2 3 5 7 11)
success=true
for prime in "${expected_primes[@]}"; do
    if [[ "$output" == *"$prime"* ]]; then
        echo "Found expected prime: $prime"
    else
        echo "Error: Expected prime $prime not found in topic output"
        success=false
    fi
done

kill $launch_pid || true

if $success; then
    echo "All expected primes were found. Test passed!"
    exit 0
else
    echo "Some expected primes were missing. Test failed!"
    exit 1
fi
