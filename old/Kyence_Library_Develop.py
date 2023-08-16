# keyence libray
# 2023 (c) TOMOMI RESEARCH, INC.

from kvhostlink import kvhostlink
import time


class PLC_Kyenece():
    def __init__(self, ip_address='192.168.0.1', port=8501, speed_x=100, speed_y=100, speed_z=100,
                 acc_x=0.3, acc_y=0.3, acc_z=0.3):
        '''
        Initialization of PLC_Kyence()
        :param ip_address: '192.168.0.1' default, IP Address of PLC controller
        :param port: 8501 default
        :param speed_x: 100 [mm/sec]
        :param speed_y: 100 [mm/sec]
        :param speed_z: 100 [mm/sec]
        :param acc_x: 0.3 [G]
        :param acc_y: 0.3 [G]
        :param acc_z: 0.3 [G]
        '''
        '''
      
        :param ip_address: IP Address of PLC controller
        :param port: 
        '''

        self.ip_address = ip_address
        self.port = port

        # speed of each state (need to input value and unit)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z

        # accleration of each state (need to input value and unit)
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.acc_z = acc_z

        # initialize the connection
        self.kv = kvhostlink.kvHostLink(self.ip_address)

        # 0: PROGRAMモード
        # 1: RUNモード
        self.kv.mode('1')

        # Setting of the speed
        self.set_x_speed(self.speed_x)
        self.set_y_speed(self.speed_y)
        self.set_z_speed(self.speed_z)

        # Setting of the Acc
        self.set_x_acc(self.acc_x)
        self.set_y_acc(self.acc_y)
        self.set_z_acc(self.acc_z)

    # -----------------------------------------------------------
    # コマンド実行指令 ON
    def _command_execute_on(self):
        data = self.kv.write('W1000', str(1))
        return data

    # コマンド実行指令 OFF
    def _command_execute_off(self):
        data = self.kv.write('W1000', str(0))
        return data

    # コマンド実行状態のONを確認する
    def _check_command_execute_state_is_on(self):
        while True:
            data = self.kv.read('W1100')
            decoded_data = data.decode('utf-8')  # Decoding the byte string into a regular string
            clean_data = decoded_data.strip(
                '\r\n')  # Removing the unnecessary characters and extracting the desired string
            # print(f'1st**check command state, {clean_data}')
            if clean_data == '00001':
                break

        print('Checked Command Execute State is ON.')

    # コマンド実行状態のOFFを確認する
    def _check_command_execute_state_is_off(self):
        while True:
            data = self.kv.read('W1100')
            decoded_data = data.decode('utf-8')  # Decoding the byte string into a regular string
            clean_data = decoded_data.strip(
                '\r\n')  # Removing the unnecessary characters and extracting the dired string
            # print(f'1st**check command state, {clean_data}')
            if clean_data == '00000':
                break

        print('Checked Command Execute State is OFF.')

    # JOG実行指令 ON
    def _jog_command_execute_on(self):
        data = self.kv.write('W1004', str(1))
        return data

    # JOG実行指令 OFF
    def jog_command_execute_off(self):
        data = self.kv.write('W1004', str(0))
        return data

    # JOG実行状態のONを確認する
    def _check_jog_command_execute_state_is_on(self):
        while True:
            data = self.kv.read('W1104')
            decoded_data = data.decode('utf-8')  # Decoding the byte string into a regular string
            clean_data = decoded_data.strip(
                '\r\n')  # Removing the unnecessary characters and extracting the desired string
            # print(f'1st**check command state, {clean_data}')
            if clean_data == '00001':
                break

    def _check_jog_command_execute_state_is_off(self):
        while True:
            data = self.kv.read('W1104')
            decoded_data = data.decode('utf-8')  # Decoding the byte string into a regular string
            clean_data = decoded_data.strip(
                '\r\n')  # Removing the unnecessary characters and extracting the desired string
            # print(f'1st**check command state, {clean_data}')
            if clean_data == '00000':
                break

    # -----------------------------------------------------------

    # 全原点移動
    def move_initial_point(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()

        # 1.コマンド No.指定
        self.kv.write('W1002', str(1))

        # 3.コマンド実行指令 ON
        self._command_execute_on()

        # 3.5 コマンド実行状態のONを確認する
        self._check_command_execute_state_is_on()

        # 4.コマンド実行指令OFF
        self._command_execute_off()

        print('Move All Robot to Initial Point')

    # 異常リセット
    def reset_anomal_state(self):
        pass

    # X軸ポイント移動
    def move_x(self, pt):
        # unit of pt [mm]
        pt = int(pt * 100)

        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()

        # 1.コマンド No.指定
        self.kv.write('W1002', str(10))  # 10: カメラX軸データ移動
        # 1.5.目標位置データ入力
        self.kv.write('W1010', str(pt))  # W1010 : Axis X:目標位置データ

        # 3.コマンド実行指令 ON
        self._command_execute_on()
        # 3.5 コマンド実行状態のONを確認する
        self._check_command_execute_state_is_on()
        # 4.コマンド実行指令OFF
        self._command_execute_off()
        print('Move X-axis robot to the desired point')

    # Y軸ポイント移動
    def move_y(self, pt):
        # unit of pt [mm]
        pt = int(pt * 100)

        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()

        # 1.コマンド No.指定
        self.kv.write('W1002', str(20))  # 20: カメラY軸データ移動
        # 1.5.目標位置データ入力
        self.kv.write('W1020', str(pt))  # W1020 : Axis Y:目標位置データ

        # 3.コマンド実行指令 ON
        self._command_execute_on()
        # 3.5 コマンド実行状態のONを確認する
        self._check_command_execute_state_is_on()
        # 4.コマンド実行指令OFF
        self._command_execute_off()
        print('Move Y-axis robot to the desired point')

    # Z軸ポイント移動
    def move_z(self, pt):
        # unit of pt [mm]
        pt = int(pt * 100)

        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()

        # 1.コマンド No.指定
        self.kv.write('W1002', str(30))  # 30: カメラZ軸データ移動
        # 1.5.目標位置データ入力
        self.kv.write('W1030', str(pt))  # W1030 : Axis Z:目標位置データ

        # 3.コマンド実行指令 ON
        self._command_execute_on()
        # 3.5 コマンド実行状態のONを確認する
        self._check_command_execute_state_is_on()
        # 4.コマンド実行指令OFF
        self._command_execute_off()
        print('Move Z-axis robot to the desired point')

    # XY軸ポイント移動
    def move_xy(self, pt_x, pt_y):
        # unit of pt [mm]
        pt_x = int(pt_x * 100)
        pt_y = int(pt_y * 100)

        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()

        # 1.コマンド No.指定
        self.kv.write('W1002', str(40))  # 40: カメラ XY軸データ移動
        # 1.5.目標位置データ入力 : 2か所入力に注意
        self.kv.write('W1010', str(pt_x))  # W1010 : Axis X:目標位置データ
        self.kv.write('W1020', str(pt_y))  # W1020 : Axis Z:目標位置データ

        # 3.コマンド実行指令 ON
        self._command_execute_on()
        # 3.5 コマンド実行状態のONを確認する
        self._check_command_execute_state_is_on()
        # 4.コマンド実行指令OFF
        self._command_execute_off()
        print('Move Z-axis robot to the desired point')

    # X軸JOG移動
    def move_x_jog_plus(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_jog_command_execute_state_is_off()
        # 1.コマンド No.指定
        self.kv.write('W1002', str(12))  # 12: :カメラX軸 JOG+移動
        # 3.コマンド実行指令 ON
        self._jog_command_execute_on()
        print('Jog Moving')
        # 3.5 コマンド実行状態のONを確認する
        self._check_jog_command_execute_state_is_on()
        # 関数の外に、# 4.コマンド実行指令OFFを入れること。
        # self._jog_command_execute_off()

    def move_x_jog_minus(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_jog_command_execute_state_is_off()
        # 1.コマンド No.指定
        self.kv.write('W1002', str(13))  # 12: :カメラX軸 JOG-移動
        # 3.コマンド実行指令 ON
        self._jog_command_execute_on()
        print('Jog Moving')
        # 3.5 コマンド実行状態のONを確認する
        self._check_jog_command_execute_state_is_on()
        # 関数の外に、# 4.コマンド実行指令OFFを入れること。
        # self._jog_command_execute_off()


    # Y軸JOG移動
    def move_y_jog_plus(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_jog_command_execute_state_is_off()
        # 1.コマンド No.指定
        self.kv.write('W1002', str(22))  # 22: :カメラY軸 JOG+移動
        # 3.コマンド実行指令 ON
        self._jog_command_execute_on()
        print('Jog Moving')
        # 3.5 コマンド実行状態のONを確認する
        self._check_jog_command_execute_state_is_on()
        # 関数の外に、# 4.コマンド実行指令OFFを入れること。
        # self._jog_command_execute_off()

    def move_y_jog_minus(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_jog_command_execute_state_is_off()
        # 1.コマンド No.指定
        self.kv.write('W1002', str(23))  # 23: :カメラY軸 JOG-移動
        # 3.コマンド実行指令 ON
        self._jog_command_execute_on()
        print('Jog Moving')
        # 3.5 コマンド実行状態のONを確認する
        self._check_jog_command_execute_state_is_on()
        # 関数の外に、# 4.コマンド実行指令OFFを入れること。
        # self._jog_command_execute_off()

    # Z軸JOG移動
    def move_z_jog_plus(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_jog_command_execute_state_is_off()
        # 1.コマンド No.指定
        self.kv.write('W1002', str(32))  # 32: :カメラZ軸 JOG+移動
        # 3.コマンド実行指令 ON
        self._jog_command_execute_on()
        print('Jog Moving')
        # 3.5 コマンド実行状態のONを確認する
        self._check_jog_command_execute_state_is_on()
        # 関数の外に、# 4.コマンド実行指令OFFを入れること。
        # self._jog_command_execute_off()

    def move_z_jog_minus(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_jog_command_execute_state_is_off()
        # 1.コマンド No.指定
        self.kv.write('W1002', str(33))  # 33: :カメラz軸 JOG+移動
        # 3.コマンド実行指令 ON
        self._jog_command_execute_on()
        print('Jog Moving')
        # 3.5 コマンド実行状態のONを確認する
        self._check_jog_command_execute_state_is_on()
        # 関数の外に、# 4.コマンド実行指令OFFを入れること。
        # self._jog_command_execute_off()

    # Setting Speed of X-axis Robot
    def set_x_speed(self, speed_x):
        speed = int(speed_x * 10)  # unit of speed_x [mm/sec]
        # 1.コマンド No.指定, speed値をPLC書き込み
        data = self.kv.write('W1012', str(speed))  # X axis
        print(f'Speed of X axis stage is set to be {0.1 * speed} [mm/sec].')
        return data

    # Setting Speed of Y-axis Robot
    def set_y_speed(self, speed_y):
        speed = int(speed_y * 10)  # unit of speed_z [mm/sec]
        # 1.コマンド No.指定, speed値をPLC書き込み
        data = self.kv.write('W1022', str(speed))  # X axis
        print(f'Speed of Y axis stage is set to be {0.1 * speed} [mm/sec].')
        return data

    # Setting Speed of Z-axis Robot
    def set_z_speed(self, speed_z):
        speed = int(speed_z * 10)  # unit of speed_z [mm/sec]
        # 1.コマンド No.指定, speed値をPLC書き込み
        data = self.kv.write('W1032', str(speed))  # X axis
        print(f'Speed of Z axis stage is set to be {0.1 * speed} [mm/sec].')
        return data

    # Setting Acceleration of X-axis Robot
    def set_x_acc(self, acc_x):
        acc = int(acc_x * 100)  # unit of acc_x [G]
        # 1.コマンド No.指定, speed値をPLC書き込み
        data = self.kv.write('W1014', str(acc))  # X axis
        print(f'Speed of X axis stage is set to be {0.01 * acc} [G].')
        return data

    # Setting Acceleration of Y-axis Robot
    def set_y_acc(self, acc_y):
        acc = int(acc_y * 100)  # unit of acc_x [G]
        # 1.コマンド No.指定, speed値をPLC書き込み
        data = self.kv.write('W1024', str(acc))  # Y axis
        print(f'Speed of Y axis stage is set to be {0.01 * acc} [G].')
        return data

    # Setting Acceleration of Z-axis Robot
    def set_z_acc(self, acc_z):
        acc = int(acc_z * 100)  # unit of acc_x [G]
        # 1.コマンド No.指定, speed値をPLC書き込み
        data = self.kv.write('W1034', str(acc))  # Z axis
        print(f'Speed of Z axis stage is set to be {0.01 * acc} [G].')
        return data

    # ------------------------------------------------------------
    # Check the state of PLC and Robots
    # ------------------------------------------------------------

    # Read the position of X-axis Robot
    def read_x_pos(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()
        #
        data = self.kv.read('W1110')  # X軸の現在位置をモニター# Decoding the byte string into a regular string
        # decode
        decoded_data = data.decode('utf-8')
        clean_data = decoded_data.strip('\r\n')
        clean_data = 0.01 * float(clean_data)
        print(f'X-axis coordinate :  {clean_data} [mm]')
        return clean_data

    # Read the position of Y-axis Robot
    def read_y_pos(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()
        #
        data = self.kv.read('W1120')  # Y軸の現在位置をモニター# Decoding the byte string into a regular string
        # decode
        decoded_data = data.decode('utf-8')
        clean_data = decoded_data.strip('\r\n')
        clean_data = 0.01 * float(clean_data)
        print(f'Y-axis position :  {clean_data} [mm]')
        return clean_data

    # Read the position of Z-axis Robot
    def read_z_pos(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()
        #
        data = self.kv.read('W1130')  # Y軸の現在位置をモニター# Decoding the byte string into a regular string
        # decode
        decoded_data = data.decode('utf-8')
        clean_data = decoded_data.strip('\r\n')
        clean_data = 0.01 * float(clean_data)
        print(f'Z-axis position :  {clean_data} [mm]')
        return clean_data

    # PLCレディ状態を確認
    def check_PLC_ready_state(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()
        #
        data = self.kv.read('W1140')  # PLC Ready State
        # decode
        decoded_data = data.decode('utf-8')
        clean_data = decoded_data.strip('\r\n')
        clean_data = int(clean_data)
        print(f'PLC Ready State :  {clean_data} ')
        print(f'0: Ready OFF, 1: Ready ON')
        return clean_data

    # 運転準備状態を確認
    def check_operation_state(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()
        #
        data = self.kv.read('W1142')  # 運転状態
        # decode
        decoded_data = data.decode('utf-8')
        clean_data = decoded_data.strip('\r\n')
        clean_data = int(clean_data)
        print(f' Operation Ready State :  {clean_data} ')
        print(f'0: 運転準備未完了, 1: 運転準備未完了')
        return clean_data

    # 異常状態を確認
    def check_anomaly_state(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()
        #
        data = self.kv.read('W1144')  # 異常状態
        # decode
        decoded_data = data.decode('utf-8')
        clean_data = decoded_data.strip('\r\n')
        clean_data = int(clean_data)
        print(f' Anomaly State :  {clean_data} ')
        print(f'0: 異常なし, 1: 異常あり')
        return clean_data

    # リモート状態を確認
    def check_remote_state(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()
        #
        data = self.kv.read('W1146')  # リモート状態
        # decode
        decoded_data = data.decode('utf-8')
        clean_data = decoded_data.strip('\r\n')
        clean_data = int(clean_data)
        print(f' Remote State :  {clean_data} ')
        print(f'0: PLC制御, 1: リモート（PC制御)')
        return clean_data

    # 原点未完了を確認
    def check_moveback_to_initial_point(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()
        #
        data = self.kv.read('W1148')  # 原点未完了
        # decode
        decoded_data = data.decode('utf-8')
        clean_data = decoded_data.strip('\r\n')
        clean_data = int(clean_data)
        print(f' moveback to initial point State :  {clean_data} ')
        print(f'0: 原点未完了状態, 1: 原点完了状態')
        return clean_data

    # 前面扉のオープン状態を確認
    def check_door_close(self):
        # 0 コマンド実行状態のOFFを確認する
        self._check_command_execute_state_is_off()
        #
        data = self.kv.read('W1150')  # 扉オープン状態
        # decode
        decoded_data = data.decode('utf-8')
        clean_data = decoded_data.strip('\r\n')
        clean_data = int(clean_data)
        print(f' door open/close State :  {clean_data} ')
        print(f'0: 扉オープン, 1: 扉クローズ')
        return clean_data


if __name__ == "__main__":
    kv = PLC_Kyenece(ip_address='192.168.0.1', port=8501)

    # move initial point
    kv.move_initial_point()

    # settting
    kv.set_x_speed(speed_x=100)
    kv.set_x_acc(acc_x=0.1)
    kv.set_y_speed(speed_y=100)
    kv.set_y_acc(acc_y=0.1)

    # move X point
    # kv.move_x(pt=100)

    # move Y point
    # kv.move_y(pt=100)
    #
    # move Z point
    # kv.move_z(pt=100)
    #
    # # move XY point
    # kv.move_xy(pt_x=50, pt_y=45)
    # kv.move_xy(pt_x=50, pt_y=50)
    # kv.move_xy(pt_x=200.5, pt_y=45)
    start = time.time()

    for y in range(100,200, 10):
        for x in range(100,160, 10):
            kv.move_xy(pt_x=x, pt_y=y)
            time.sleep(1)
            data = kv.read_x_pos()
            data = kv.read_y_pos()

    # # Jog Move X
    # kv.move_x_jog_plus()
    # time.sleep(2)
    # kv.jog_command_execute_off()
    #
    # kv.move_x_jog_minus()
    # time.sleep(1)
    # kv.jog_command_execute_off()
    #
    # # Jog Move Y
    # kv.move_y_jog_plus()
    # time.sleep(1.5)
    # kv.jog_command_execute_off()
    #
    # kv.move_y_jog_minus()
    # time.sleep(1.2)
    # kv.jog_command_execute_off()
    #
    # # Jog Move Z
    # kv.move_z_jog_plus()
    # time.sleep(1.5)
    # kv.jog_command_execute_off()
    #
    # kv.move_z_jog_minus()
    # time.sleep(1.3)
    # kv.jog_command_execute_off()

    end = time.time()
    print(end - start)

    # move initial point
    kv.move_initial_point()

    # Read X point
    data = kv.read_x_pos()
    data = kv.read_y_pos()
    data = kv.read_z_pos()

    # Check PLC Ready State
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

    data = kv.read_x_pos()
    print(data)
    data = kv.read_y_pos()
    print(data)
    data = kv.read_z_pos()
    print(data)
