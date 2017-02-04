# -*- coding: utf-8 -*-
import serial

class Connector(object):
    def __init__(self, port="/dev/ttyUSB0", baudrate = 57600, timeout=None):
        #initialization and open the port
        #possible timeout values:
        #    1. None: wait forever, block call
        #    2. 0: non-blocking mode, return immediately
        #    3. x, x is bigger than 0, float allowed, timeout block call
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = baudrate
        self.ser.timeout = timeout
        self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
        self.ser.parity = serial.PARITY_NONE #set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits
        self.ser.xonxoff = False    #disable software flow control
        self.ser.rtscts = False     #disable hardware (RTS/CTS) flow control
        self.ser.dsrdtr = False     #disable hardware (DSR/DTR) flow control
        self.ser.writeTimeout = 2   #timeout for write

        self.ser.open()

    def read_line(self):
        return self.ser.readline()

    def close(self):
        self.ser.close()
