# 3軸ロボット制御　Pythonライブラリ

Gstreams社がTR-100R向けに開発したPLC制御プログラムをベースに、Pythonで3軸ロボットの制御やPLCの状態の確認を行うためのライブラリです。


## インストール方法

```bash
git clone https://github.com/kotai2003/PLC_KV_gstreams.git
```

## 使用方法

### 接続

```python
from Keyence_PLC_RIKAZAI import PLC_RIKAZAI
import time

kv = PLC_RIKAZAI.PLC_Kyenece(ip_address='192.168.0.1', port=8501)

# connect
kv.connect()
```

### 接続解除
```python
# disconnect
kv.disconnect()
```
## 初期設定

```python
 # Initial point
kv.move_initial_point()

# Speed and Acceleration
kv.set_x_speed(speed_x=100)
kv.set_x_acc(acc_x=0.1)
kv.set_y_speed(speed_y=100)
kv.set_y_acc(acc_y=0.1)
kv.set_z_speed(speed_z=100)
kv.set_z_acc(acc_z=0.1)

```

## 移動機能

### ポイント指定移動
```python
kv.move_x(pt=100)  # x = 100mm
kv.move_y(pt=150)  # y = 150mm
kv.move_z(pt=50)  #  z = 5mm
kv.move_xy(pt_x=250, pt_y=200) # (x, y) = (250,200)
```

### 繰り返し移動の例 

```python
for y in range(100, 200, 10):
    for x in range(100, 150, 10):
        kv.move_xy(pt_x=x, pt_y=y)
        time.sleep(1)
        data = kv.read_x_pos()
        data = kv.read_y_pos()
```

### JOG移動

```python
kv.move_x_jog_plus()
time.sleep(1) # wait by 1 sec
kv.stop_jog_move()

kv.move_x_jog_minus()
time.sleep(1) # wait by 1 sec
kv.stop_jog_move()


# Jog Move Y
kv.move_y_jog_plus()
time.sleep(1) # wait by 1 sec
kv.stop_jog_move()


kv.move_y_jog_minus()
time.sleep(1.2) # wait by 1.2 sec
kv.stop_jog_move()

# Jog Move Z
kv.move_z_jog_plus()
time.sleep(1.5) # wait by 1.5 sec
kv.stop_jog_move()

kv.move_z_jog_minus()
time.sleep(1.3)
kv.stop_jog_move()
```

## ロボットの位置確認

```python
data = kv.read_x_pos()
data = kv.read_y_pos()
data = kv.read_z_pos()
```

## PLCの状態確認

```python
data = kv.check_PLC_ready_state()
print(data)

data = kv.check_operation_state()
print(data)

data = kv.check_anomaly_state()
print(data)

data = kv.check_remote_state()
print(data)

data = kv.check_moveback_to_initial_point()
print(data)

data = kv.check_door_close()
print(data)

```


## ライセンス
このSWは、GPLライセンスの下でライセンスされています。

## 制作
(c) 2023 TOMOMI RESEARCH, INC.