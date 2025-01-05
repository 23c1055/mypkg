#!/bin/bash
# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

set -e 
ROS2_WS=~/ros2_ws
echo "Launching Prime_Generator node..."
cd $ROS2_WS
source install/setup.bash
ros2 run mypkg prime_generator &  
NODE_PID=$!

echo "Waiting for the node to start..."
sleep 8

echo "Subscribing to the /countup topic..."
output=$(timeout 5 ros2 topic echo /countup --once)

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

echo "Stopping the Prime_Generator node..."
kill $NODE_PID || true

if $success; then
    echo "All expected primes were found. Test passed!"
    exit 0
else
    echo "Some expected primes were missing. Test failed!"
    exit 1
fi
