from kvhostlink import kvHostLink
import time

# https://qiita.com/OkitaSystemDesign/items/b8c19c313b7010e69ddf
# https://github.com/kotai2003/kvHostLink/blob/main/kvhostlink.py

def set_robot(axis=1, vel=0, acc=0):
    vel = int(vel*10)
    acc = acc
    if axis == 1:
        # 2.コマンド組み立て、書き込み
        # X軸速度　[mm/sec]
        data = kv.write('W1012', str(vel))
        # X軸加速度　[G]
        data = kv.write('W1014', str(acc))

    elif axis == 2:
        # 2.コマンド組み立て、書き込み
        # Y軸速度　[mm/sec]
        data = kv.write('W1022', str(vel))
        # Y軸加速度　[G]
        data = kv.write('W1024', str(acc))

    elif axis == 3:
        # 2.コマンド組み立て、書き込み
        # X軸速度　[mm/sec]
        data = kv.write('W1032', str(vel))
        # X軸加速度　[G]
        data = kv.write('W1034', str(acc))



    return data


def move_xy(x_loc , y_loc ):
    x_loc = int(x_loc*100)
    y_loc = int(y_loc*100)

    #X軸座標の書き込み
    data = kv.write('W1010', str(x_loc))
    # Y軸座標の書き込み
    data = kv.write('W1020', str(x_loc))

    # 1.コマンド No.指定
    # XY軸
    data = kv.write('W1002', '40')

    # 3.コマンド実行指令 ON
    data = kv.write('W1000', str(1))

    # 6. コマンド実行指令 OFF
    data = kv.write('W1000', str(0))


def move_point_x():
    pass

def move_robot(axis=1, loc=0.0):
    loc = int(loc*100)

    if axis == 1:
        #1.コマンド No.指定
        # X軸
        data = kv.write('W1002', '10')

        #2.コマンド組み立て、書き込み
        # X軸
        data = kv.write('W1010', str(loc))

        #3.コマンド実行指令 ON
        data = kv.write('W1000', str(1))

        #4. Check the location is reached.
        data = kv.read('W1110')
        # Decoding the byte string into a regular string
        decoded_data = data.decode('utf-8')
        # Removing the unnecessary characters and extracting the desired string
        clean_data = decoded_data.strip('\r\n')

        print(f'X coord:  {data}')
        print(f'cleaned_data_x:  {clean_data}')

        #5.Check the command state
        while True:
            data = kv.read('W1100')
            # Decoding the byte string into a regular string
            decoded_data = data.decode('utf-8')
            # Removing the unnecessary characters and extracting the desired string
            clean_data = decoded_data.strip('\r\n')
            print(f'**check command state, {clean_data}')
            # if clean_data == '00010':
            #     continue
            # else:
            #     break
        #6. コマンド実行指令 OFF
        data = kv.write('W1000', str(0))

    elif axis == 2:
        # 1.コマンド No.指定
        # Y軸
        data = kv.write('W1002', '20')

        # 2.コマンド組み立て、書き込み
        # Y軸
        data = kv.write('W1020', str(loc))

        # 3.コマンド実行指令 ON/OFF
        data = kv.write('W1000', str(1))

        # 5.Check the command state
        while True:
            data = kv.read('W1100')
            # Decoding the byte string into a regular string
            decoded_data = data.decode('utf-8')
            # Removing the unnecessary characters and extracting the desired string
            clean_data = decoded_data.strip('\r\n')
            print(f'check command state, {clean_data}')

            if clean_data == '00001':
                break
        data = kv.write('W1000', str(0))

        return data


    print('move test ended.')


def move_reset():
    # 1.コマンド No.指定
    data = kv.write('W1002', '1') # 全軸原点移動



    # 3.コマンド実行指令 ON
    data = kv.write('W1000', str(1))
    # 4.コマンド実行指令OFF
    data = kv.write('W1000', str(0))




if __name__ == "__main__":

    kv = kvHostLink('192.168.0.1')

    # 引数には0か1を入れて動作状態を切り替えます
    # 0: PROGRAMモード
    # 1: RUNモード
    data = kv.mode('1')

    data = kv.read('W1146')
    print('remote state')
    print(data)

    set_robot(axis=1, vel=30, acc=30)
    set_robot(axis=2, vel=30, acc=30)
    set_robot(axis=3, vel=20, acc=30)

    # data= move_robot(axis=1, loc=100)

    data = move_xy(x_loc=10, y_loc=10)
    print(data)
    print('command state2')
    print(kv.read('W1100'))

    # time.sleep(1)
    #
    # data2 = move_robot(axis=2, loc=100)
    #
    # print(f'data2 :{data2}')
    #
    # # data = move_reset()
    # print(data)

