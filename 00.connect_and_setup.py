from Keyence_PLC_RIKAZAI import PLC_RIKAZAI
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
