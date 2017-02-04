/*
 * Card IO Lock
 * TODO:
 * - watchdog: reset Arduino if it does not send N
 */

#include <SPI.h>
#include <MFRC522.h>

#define LED_PIN  8
#define RST_PIN  9
#define SS_PIN   10

MFRC522 mfrc522(SS_PIN, RST_PIN);	// Create MFRC522 instance

void setup() {
    Serial.begin(115200);	    // Initialize serial communications with the PC
    while (!Serial);		    // Do nothing if no serial port is opened
    SPI.begin();			    // Init SPI bus
    mfrc522.PCD_Init();	        // Init MFRC522
    report_reader();            // Show details of PCD - MFRC522 Card Reader details
    pinMode(LED_PIN, OUTPUT);   // configure indicator LED
    digitalWrite(LED_PIN, LOW); // indicator off
    Serial.println(F("READY")); // report that setup is Ok
}

void loop() {
    // Look for new cards
    if ( ! mfrc522.PICC_IsNewCardPresent()) {
        Serial.println("N");
        delay(250);
        return;
    }
    //new card detected

    // Select one of the cards
    if ( ! mfrc522.PICC_ReadCardSerial()) {
        Serial.println("NOT_SELECTED");
        return;
    }
    // Dump debug info about the card; PICC_HaltA() is automatically called
    dumpDetailsToSerial(&(mfrc522.uid));

    indicate(2);
}

void indicate(int count) {
    while (count--) {
        digitalWrite(LED_PIN, HIGH);
        delay(250);
        digitalWrite(LED_PIN, LOW);
        delay(200);
    }
}

void report_reader() {
    // Get the MFRC522 software version
    byte v = mfrc522.PCD_ReadRegister(mfrc522.VersionReg);
    Serial.print(F("MFRC522 Software Version: 0x"));
    Serial.print(v, HEX);
    if (v == 0x91) {
        Serial.print(F(" = v1.0"));
    } else if (v == 0x92) {
        Serial.print(F(" = v2.0"));
    } else {
        Serial.print(F(" (unknown)"));
    }
    Serial.println("");
    // When 0x00 or 0xFF is returned, communication probably failed
    if ((v == 0x00) || (v == 0xFF)) {
        Serial.println(F("WARNING: Communication failure, is the MFRC522 properly connected?"));
    }
}

/**
 * Dumps card info (UID,SAK) about the selected PICC to Serial.
 */
void dumpDetailsToSerial(MFRC522::Uid *uid) {
  // UID
  Serial.print(F("UID:"));
  for (byte i = 0; i < uid->size; i++) {
    if(uid->uidByte[i] < 0x10) {
      Serial.print(F("0"));
    } else {
      Serial.print(F(""));
    }
    Serial.print(uid->uidByte[i], HEX);
  } 
  // SAK
  Serial.print(F(":SAK:"));
  if(uid->sak < 0x10) {
    Serial.print(F("0"));
  }
  Serial.println(uid->sak, HEX);
} 


