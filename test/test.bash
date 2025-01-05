#!/bin/bash
# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

set -e  # スクリプトエラー時に終了

# ROS2ワークスペースのパスを指定（必要に応じて変更）
ROS2_WS=~/ros2_ws

# ROS 2環境をセットアップ
source /opt/ros/humble/setup.bash  # 使用中のROS 2ディストリビューション名に変更
source $ROS2_WS/install/setup.bash

# Prime_Generatorノードを起動
echo "Launching Prime_Generator node..."
ros2 run mypkg prime_generator &  # バックグラウンドでノードを実行
NODE_PID=$!

# ノードが起動するのを待機（Prime_Generator内に5秒遅延があるため、少し長めに待つ）
echo "Waiting for the node to start..."
sleep 10

# トピックを購読して結果を確認
echo "Subscribing to the /countup topic..."
output=$(timeout 10 ros2 topic echo /countup --once)

# 期待する値を定義（初めの数個の素数）
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

# 実行中のノードを停止
echo "Stopping the Prime_Generator node..."
kill $NODE_PID || true

# テスト結果を出力
if $success; then
    echo "All expected primes were found. Test passed!"
    exit 0
else
    echo "Some expected primes were missing. Test failed!"
    exit 1
fi
