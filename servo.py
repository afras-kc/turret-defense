import pyfirmata
import time

port = "/dev/tty.usbmodem101"
board = pyfirmata.Arduino(port)
servo_pinX = board.get_pin('d:9:s') #pin 9 Arduino
servo_pinY = board.get_pin('d:10:s') #pin 10 Arduino
led_pin = board.get_pin('d:12:o') #pin 13 Arduino
led2_pin = board.get_pin('d:13:o') #pin 13 Arduino

servoPos = [90, 90] # initial servo position

while True:
  # rotate servo motor
  for i in range(0, 180):
    servo_pinX.write(i)
    time.sleep(0.01)
