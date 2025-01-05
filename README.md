# Prime_Generator

![status](https://github.com/23c1055/task/actions/workflows/test.yml/badge.svg)
## 概要

- このレポジトリは、ROS 2のパッケージです。このノードは、2から始まる昇順の素数を1秒ごとにパブリッシュします。

## 必要なソフトウェア・ミドルウェア
- python

    - テスト済み: 3.7 ~ 3.11
- ROS2

## テスト環境

 - Ubuntu 22.04.5 LTS


## 実行手順

- 以下の手順で、プロジェクトをローカルレポジトリにクローンをした後に実行をします。


リポジトリをクローン
```bash
$ git clone https://github.com/23c1055/pkgs.git
```
ディレクトリに移動
```bash
$ cd pkgs
```
端末1で次を入力
```bash
$ ros2 run mypkg prime_generator
```
端末2（端末1とは別の端末）に移動し、次を入力
```bash
$ topic echo /countup
```

### 実行結果
端末2で以下の様に出力されます
```bash
data: 2
---
data: 3
---
data: 5
---
data: 7
---
```

## ライセンス

- このソフトウェアパッケージは3条項BSDライセンスの下、再頒布および使用が許可されています。

©2025 Goto Shingo

