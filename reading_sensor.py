import serial
import time
import threading

def sensor():
    print('sensor function is loading')
    ser = serial.Serial('COM4', 9600)
    time.sleep(2)
    global data
    data = ['Sensor 1 OFF']
    while True:
        b = ser.readline()  # read a byte string
        string_n = b.decode()  # decode byte string into Unicode
        string = string_n.rstrip()  # remove \n and \r
        print(string)
        data.append(string)  # add to the end of data list

    ser.close()

def api_to_sensor():
    print('request function is loading')
    while True:
        x = input('enter 1 to get sensor data:')
        if x == '1':
            print('sensor data = ', data[-1])


threading.Thread(target=sensor).start()
threading.Thread(target=api_to_sensor).start()
