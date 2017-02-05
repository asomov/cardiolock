# -*- coding: utf-8 -*-
from __future__ import print_function
from .connector import Connector
from subprocess import call

# Define the location of the USB port (ls /dev/tty*)
USB_NAME="/dev/ttyUSB0"

# Define arguments for subprocess.call() to unlock
# Linux Mint => cinnamon-screensaver-command -d
PROGRAM_UNLOCK=["cinnamon-screensaver-command", "-d"]

# Define arguments for subprocess.call() to lock
# or assign it to None to only unlock
# Linux Mint => cinnamon-screensaver-command -l
# PROGRAM_LOCK=["cinnamon-screensaver-command", "-l"]
PROGRAM_LOCK=None

class CardComm(object):

    def __init__(self, port):
        self.port = port
        self.connector = Connector(port, baudrate = 115200, timeout = None)
        self.uid = None
        self.locked = False

    def start(self):
        resp = self.connector.read_line().strip()
        if resp != "MFRC522 Software Version: 0x92 = v2.0":
            raise Exception("Unexpected chip: " + resp)
        resp = self.connector.read_line().strip()
        if resp != "READY":
            raise Exception("Unexpected Arduino setup: " + resp)

    def set_uid(self):
        while (not self.uid):
            resp = self.connector.read_line()
            if(resp.startswith("UID:")): #UID:00112233:SAK:08
                self.uid = resp
                print('Detected the card {}######'.format(resp[:6]))

    def listen(self):
        while True:
            resp = self.connector.read_line()
            if resp == self.uid:
                print("Identity card detected")
                self.trigger()
        #self.connector.close()

    def trigger(self):
        if PROGRAM_LOCK:
            if self.locked:
                print("Unlock")
                call(PROGRAM_UNLOCK)
            else:
                print("Lock")
                call(PROGRAM_LOCK)
        else:
            print("Unlock")
            call(PROGRAM_UNLOCK)

        self.locked = not self.locked


def main():
    card = CardComm(USB_NAME)
    card.start()
    print("Use your identity card...")
    card.set_uid()
    card.listen()
    print("Finished.")

if __name__ == '__main__':
    main()
