# Card IO lock

Made in/with/at [Revspace](http://revspace.nl)

Basic usage [video](https://youtu.be/0Dn9kWpbn1k)

Soldered [assembly](https://github.com/asomov/cardiolock/blob/master/doc/20170204_152847.jpg)

[Connected to computer](https://github.com/asomov/cardiolock/blob/master/doc/20170205_135643.jpg)

With the [box](https://github.com/asomov/cardiolock/blob/master/doc/20170205_135107.jpg)

### Hardware

- Mifare [RFID reader](https://github.com/asomov/cardiolock/blob/master/doc/RC522_1.jpg)
(with MFRC522 [chip](https://www.nxp.com/documents/data_sheet/MFRC522.pdf))
- Arduino [nano](https://www.arduino.cc/en/Main/arduinoBoardNano) (with USB-to-TTL)
- USB cabel

The doc folder contains the pictures of the hardware.

**MFRC522 -> Arduino Nano**

- 3.3 V -> 3.3 V
- RST   -> D9
- GND   -> GND
- IRQ   -> *not used*
- MISO  -> D12
- MOSI  -> D11
- SCK   -> D13 (SPI SCK)
- SDA   -> D10 (SPI SS)

### Software

Dependencies:
- [Arduino library for MFRC522](https://github.com/miguelbalboa/rfid)
- Python 2.7
- Command line utility to unlock/lock computer (must be provided by user)

The project has:
- The Arduino program to read UIDs (mfrc522-cardiolock.ino)
- The Python 2 program to communicate to Arduino via USB (should also work with Python 3, but not tested)

### Usage

1. Install [Arduino library for MFRC522](https://github.com/miguelbalboa/rfid)
2. Upload provided mfrc522-cardiolock.ino to Arduino
3. Configure [connection to USB without root privileges](http://askubuntu.com/a/210230)

  - `groups ${USER}`
  - `sudo gpasswd --add ${USER} dialout`
  
You then need to log out and log back in again for it to be effective. 

4. Use your favorite text editor to configure cardiolock.py
  - check which USB port is used by Arduino and define it as USB_NAME (`ls /dev/tty*`)
  - find out the way to unlock your computer from the command line and
    define it as PROGRAM_UNLOCK
  - if you want to lock the computer with the card define also PROGRAM_LOCK,
    otherwise assign it to None and lock the computer manually
5. Launch `.run_cardiolock.sh`
6. Use you Mifare card as master card once
7. Use the same card to unlock (or lock) your computer
8. Enjoy having fun without typing your password.
9. If you are afraid to forget your password because you do not use it anymore
   just write it down and stick it to your monitor.

Your feedback is welcome !
