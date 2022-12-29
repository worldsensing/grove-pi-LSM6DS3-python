from LSM6DS3 import LSM6DS3

if __name__ == "__main__":
    print("Starting up code...")

    lsm6ds3 = LSM6DS3()

    try:
        acc_x = lsm6ds3.read_acceleration_x()
        acc_y = lsm6ds3.read_acceleration_y()
        acc_z = lsm6ds3.read_acceleration_z()
    except IOError as e:
        print("Unable to read from accelerometer, check the setup and try again. Error is: ")
        print(e)
