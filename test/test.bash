#!/bin/bash
# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || { echo "ディレクトリが見つかりません: $dir/ros2_ws"; exit 1; }
colcon build || { echo "ビルドに失敗しました"; exit 1; }
source install/setup.bash
timeout 10 ros2 launch mypkg prime_checker.launch.py > /tmp/mypkg.log 2>&1 &
LAUNCH_PID=$!

echo "トピックを確認中..."
sleep 5

TOPIC_OUTPUT=$(timeout 5 ros2 topic echo /prime_check 2>/dev/null)

kill $LAUNCH_PID 2>/dev/null

if [[ -z "$TOPIC_OUTPUT" ]]; then
    echo "エラー: トピック /prime_check からデータを受信できませんでした。"
    exit 1
else
    echo "トピック /prime_check から以下のデータを受信しました:"
    echo "$TOPIC_OUTPUT" | head -n 10  # 受信データの先頭10行を表示
fi
