from Keyence_PLC_RIKAZAI import PLC_RIKAZAI
import time

import time

# This program was created by TOMOMI RESEARCH,INC.



if __name__ == '__main__':
    # ----------------------------------------------------
    # Connect
    # ----------------------------------------------------

    kv = PLC_RIKAZAI.PLC_Kyenece(ip_address='192.168.0.1', port=8501)

    #connect
    kv.connect()

    # ----------------------------------------------------
    # Initial Setup
    # ----------------------------------------------------

    #Initial point
    kv.move_initial_point()

    # Speed and Acceleration
    kv.set_x_speed(speed_x=100)
    kv.set_x_acc(acc_x=0.1)
    kv.set_y_speed(speed_y=100)
    kv.set_y_acc(acc_y=0.1)
    kv.set_z_speed(speed_z=100)
    kv.set_z_acc(acc_z=0.1)

    # ----------------------------------------------------
    # Move by point
    # ----------------------------------------------------
    kv.move_x(pt=100)  # x = 100mm
    kv.move_y(pt=150)  # y = 150mm
    kv.move_z(pt=50)  #  z = 5mm

    kv.move_xy(pt_x=250, pt_y=200) # (x, y) = (250,200)


    # ----------------------------------------------------
    # Move : Matrix Style
    # ----------------------------------------------------
    start = time.time()

    for y in range(100, 200, 10):
        for x in range(100, 150, 10):
            kv.move_xy(pt_x=x, pt_y=y)
            time.sleep(1)
            data = kv.read_x_pos()
            data = kv.read_y_pos()

    end = time.time()
    print(end - start)

    # Initial point
    kv.move_initial_point()


    # Read X point
    data = kv.read_x_pos()
    data = kv.read_y_pos()
    data = kv.read_z_pos()

    # Initial point
    kv.move_initial_point()

    #----------------------------------------------------
    # Check PLC Ready State
    # ----------------------------------------------------

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

    # ----------------------------------------------------
    # Read X, Y, Z point
    # ----------------------------------------------------

    data = kv.read_x_pos()
    print(data)
    data = kv.read_y_pos()
    print(data)
    data = kv.read_z_pos()
    print(data)

    # ----------------------------------------------------
    # Disconnect
    # ----------------------------------------------------

    # disconnect
    kv.disconnect()
