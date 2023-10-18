import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    while True:
        print("Hold a card near the reader")
        id, text = reader.read()
        print("ID: ", id)
        print("Text: ", text)
finally:
    GPIO.cleanup()
