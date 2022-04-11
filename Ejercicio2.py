import serial 
import numpy as np
from matplotlib import pyplot as plt
from asyncore import write

ser = serial.Serial('COM4',9600)

ydata = [30] * 50

while True:
    data = ser.readline().rstrip()
    print(data)
    len(data.split(b".")) == 2
    ydata.append(data)
