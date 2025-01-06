#!/bin/bash
# SPDX-FileCopyrightText: 2025 Riku Kinjo
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

ng () {
    echo "${1}行目に問題有"
    res=1
}

res=0

cd $dir/ros2_ws || exit 1
colcon build || exit 1
source $dir/.bashrc || exit 1
timeout 15 ros2 run mypkg prime_generator > /tmp/prime_generator.log &  
NODE_PID=$!


timeout 11 ros2 topic echo /countup > /tmp/countup.log
echo "[/countup topic output]"
cat /tmp/countup.log
echo "====================="

prime1=$(awk 'NR==1 {print $2}' /tmp/countup.log)
prime2=$(awk 'NR==3 {print $2}' /tmp/countup.log)
prime3=$(awk 'NR==5 {print $2}' /tmp/countup.log)

expected_primes=(2 3 5)

[ "${prime1}" = "${expected_primes[0]}" ] || ng "$LINENO"
[ "${prime2}" = "${expected_primes[1]}" ] || ng "$LINENO"
[ "${prime3}" = "${expected_primes[2]}" ] || ng "$LINENO"


kill $NODE_PID || true

if [ $res -eq 0 ]; then
    echo "すべてのテストが成功しました。"
    exit 0
else
    echo "一部のテストに失敗しました。"
    exit 1
fi
