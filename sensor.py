import serial
import time



# set up the serial line
ser = serial.Serial('COM4', 9600)
time.sleep(2)

# Read and record the data
data =[]                       # empty list to store the data
for i in range(50):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip() # remove \n and \r
    #flt = float(string)        # convert string to float
    print(string)
    data.append(string)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()

# show the data

for line in data:
    print(line)

"""
ser = serial.Serial('COM3', 9600, timeout=1)
for i in range(10):

    time.sleep(0.5)
    ser.write(b'1')   # send the pyte string 'H'
    time.sleep(0.5)   # wait 0.5 seconds
    ser.write(b'q')   # send the byte string 'L'

ser.close()
"""