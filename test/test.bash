#!/bin/bash
# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause
#!/bin/bash
# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/install/setup.bash

# ノードの起動
timeout 5 ros2 launch mypkg prime_checker.launch.py &

# 少し待機してノードが起動するのを待つ
sleep 2

# トピックのメッセージを確認
# 'prime_check' トピックからデータを受信し、5行だけ確認して表示
ros2 topic echo /prime_check --once | head -n 5

# 終了メッセージ
echo "トピックのチェックが完了しました。"

if [[ -z "$TOPIC_OUTPUT" ]]; then
    echo "エラー: トピック /prime_check からデータを受信できませんでした。"
    exit 1
else
    echo "トピック /prime_check から以下のデータを受信しました:"
    echo "$TOPIC_OUTPUT" | head -n 10  # 受信データの先頭10行を表示
fi
