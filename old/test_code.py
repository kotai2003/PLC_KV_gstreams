from old.PLC_RIKAZAI import PLC_Kyenece
import time



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    kv = PLC_Kyenece(ip_address='192.168.0.1', port=8501)

    #Initial point
    kv.move_initial_point()

    # settting
    kv.set_x_speed(speed_x=100)
    kv.set_x_acc(acc_x=0.1)
    kv.set_y_speed(speed_y=100)
    kv.set_y_acc(acc_y=0.1)

    # ----------------------------------------------------
    # Move Test 1 : RIKAZAI
    # ----------------------------------------------------
    kv.move_z(pt=189.72) #189.72
    # ----------------------------------------------------
    #Move Test 1 : MASS
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

    # ----------------------------------------------------
    # Move Test 2 : JOG
    # ----------------------------------------------------
    kv.move_x_jog_plus()
    time.sleep(2)
    kv.jog_command_execute_off()

    kv.move_x_jog_minus()
    time.sleep(1)
    kv.jog_command_execute_off()

    # Jog Move Y
    kv.move_y_jog_plus()
    time.sleep(1.5)
    kv.jog_command_execute_off()

    kv.move_y_jog_minus()
    time.sleep(1.2)
    kv.jog_command_execute_off()

    # # Jog Move Z
    # kv.move_z_jog_plus()
    # time.sleep(1.5)
    # kv.jog_command_execute_off()
    #
    # kv.move_z_jog_minus()
    # time.sleep(1.3)
    # kv.jog_command_execute_off()

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

    data = kv.read_x_pos()
    print(data)
    data = kv.read_y_pos()
    print(data)
    data = kv.read_z_pos()
    print(data)

