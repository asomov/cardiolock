# Card IO lock

Made in/with/at [Revspace](http://revspace.nl)

Basic usage [video](https://youtu.be/0Dn9kWpbn1k)

### Hardware

- Mifare [RFID reader](https://github.com/asomov/cardiolock/blob/master/doc/RC522_1.jpg)
(with MFRC522 [chip](https://www.nxp.com/documents/data_sheet/MFRC522.pdf))
- Arduino [nano](https://www.arduino.cc/en/Main/arduinoBoardNano) (with USB-to-TTL)
- USB cabel

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
- Command line utility to unlock/lock computer (must be provided by user)

The project has:
- The Arduino program to read UIDs (mfrc522-cardiolock.ino)
- The Python 2 program to communicate with Arduino via USB (should also work with Python 3, but not tested)

### Usage

1. Install [Arduino library for MFRC522](https://github.com/miguelbalboa/rfid)
2. Upload provided mfrc522-cardiolock.ino to Arduino
3. Use your favorite text editor to configure cardiolock.py
  - check which USB port is used by Arduino and define it as USB_NAME (`ls /dev/tty*`)
  - find out the way to unlock your computer from the command line and
    define it as PROGRAM_UNLOCK
  - if you want to lock the computer with the card define also PROGRAM_LOCK,
    otherwise assign it to None and lock the computer manually
4. Launch `.run_cardiolock.sh`
5. Use you Mifare card as master card once
6. Use the same card to unlock (or lock) your computer
7. Enjoy having fun without typing your password.
8. If you are afraid to forget your password because you do not use it anymore
   just write it down and stick it to your monitor.

Your feedback is welcome !
