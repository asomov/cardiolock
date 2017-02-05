# Card IO lock

Made in/with/at [Revspace](http://revspace.nl)

Basic usage [video](https://youtu.be/0Dn9kWpbn1k)

### Hardware

- Mifare RFID reader (with MFRC522 [chip](https://www.nxp.com/documents/data_sheet/MFRC522.pdf))
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
