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


## 使用方法

- 以下の手順で、プロジェクトをローカルレポジトリにクローンをした後に実行をします。


リポジトリをクローン
```bash
$ git clone https://github.com/23c1055/pkgs.git
```
ディレクトリに移動
```bash
$ cd pkgs
```
実行例
```bash
$ ros2 run mypkg prime_generator
```

### 実行結果
```bash
$[INFO] [1735827869.098587044] [published_prime]: 2
$[INFO] [1735827870.076844307] [published_prime]: 3
$[INFO] [1735827871.076998369] [published_prime]: 5
$[INFO] [1735827872.077272675] [published_prime]: 7
$[INFO] [1735827873.076894356] [published_prime]: 11
$[INFO] [1735827874.077199469] [published_prime]: 13
```

## ライセンス

- このソフトウェアパッケージは3条項BSDライセンスの下、再頒布および使用が許可されています。

©2025 Goto Shingo

