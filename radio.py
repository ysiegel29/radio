#!/usr/bin/env python
# Bare bones simple internet radio
# www.suppertime.co.uk/blogmywiki
# http://direct.franceinter.fr/live/franceinter-midfi.mp3
# http://direct.franceinfo.fr/live/franceinfo-midfi.mp3
# http://direct.fipradio.fr/live/fip-midfi.mp3
# https://github.com/nstansby/rpi-rotary-encoder-python

import time
import os
import board
import pulseio
import digitalio
import RPi.GPIO as GPIO
from encoder import Encoder
import subprocess
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# intial states
currentStation = 2
stationList = ["France Inter", "France Info", "FIP"]
os.system("mpc clear")
os.system("mpc add http://direct.franceinter.fr/live/franceinter-midfi.mp3")
os.system("mpc add http://direct.franceinfo.fr/live/franceinfo-midfi.mp3")
os.system("mpc add http://direct.fipradio.fr/live/fip-midfi.mp3")

# define button
button = digitalio.DigitalInOut(board.D25) #D9 for tactile
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
#led = pulseio.PWMOut(board.D21)
#led.duty_cycle = 2 ** 15

led = digitalio.DigitalInOut(board.D21)
led.direction = digitalio.Direction.OUTPUT

###### PI OLED DISPLAY ######
i2c = busio.I2C(SCL, SDA) # Create the I2C interface.
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c) # Create the SSD1306 OLED class.

disp.fill(0) # Clear display.
disp.rotation = 0
disp.show()
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
padding = -2
top = padding
bottom = height - padding
x = 10
font = ImageFont.truetype('/home/pi/BebasNeue-Regular.ttf',24) 
font2 = ImageFont.load_default()

# functions
def blink(x):
  for i in range(x):
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)

def changeStation(unboundvalue, boundvalue):
  # os.system("aplay button-19.wav &") 
  print("unbound: ", unboundvalue)
  print("bound: ", boundvalue)
  global currentStation
  OLED_display(stationList[boundvalue - 1],"IP: " + IP)
  if boundvalue != currentStation:
    print("changing to station to ", stationList[boundvalue - 1])
    os.system("mpc play " + str(boundvalue))
    currentStation = boundvalue
    print("been here")
  time.sleep(0.1)

def OLED_display(text1, text2):
  global last_OLED_update
  draw.rectangle((0, 0, width, height), outline=0, fill=0) #clear
  draw.text((x, top + 0), text1, font=font, fill=255)
  draw.text((x, top + 25), text2, font=font2, fill=255)
  last_OLED_update = time.monotonic()
  disp.image(image)
  disp.show()


# initialisation
blink(5)
led.value = True

onoff = 1
cmd = "hostname -I | cut -d' ' -f1"
IP = subprocess.check_output(cmd, shell=True).decode("utf-8")

os.system("mpc play 2")
print("playing track 2")
OLED_display("WELCOME!","IP: " + IP)
time.sleep(2)
OLED_display(stationList[1],"IP: " + IP)

# create encoder
e1 = Encoder(7, 8, 1, 3, changeStation)

while True:

  toggle = button.value

  if (not toggle): # button was pressed
    blink(2)
    if onoff: # it was on, turn off
      print("TURN OFF")
      OLED_display("Bye...","")
      led.value = False
      os.system("mpc stop")
      onoff = 0
    elif not onoff: # it was off, turn on
      print("TURN ON")
      OLED_display("WELCOME!","IP: " + IP)
      led.value = True
      os.system("mpc play 2")
      currentStation = 2
      boundvalue = 2
      OLED_display(stationList[boundvalue - 1],"IP: " + IP)
      onoff = 1

  
  if time.monotonic() > last_OLED_update + 5:
    draw.rectangle((0, 0, width, height), outline=0, fill=0) #clear
    disp.image(image)
    disp.show()

#  print("getvalue: ",e1.getValue())
  time.sleep(0.05)


