#display digit on single digit  7 segment led display
import time
import board
import digitalio

ledA = digitalio.DigitalInOut(board.D6)
ledA.direction = digitalio.Direction.OUTPUT

ledB = digitalio.DigitalInOut(board.D5)
ledB.direction = digitalio.Direction.OUTPUT

ledC = digitalio.DigitalInOut(board.D15)
ledC.direction = digitalio.Direction.OUTPUT

ledD = digitalio.DigitalInOut(board.D18)
ledD.direction = digitalio.Direction.OUTPUT

ledE = digitalio.DigitalInOut(board.D23)
ledE.direction = digitalio.Direction.OUTPUT

ledF = digitalio.DigitalInOut(board.D19)
ledF.direction = digitalio.Direction.OUTPUT

ledG = digitalio.DigitalInOut(board.D26)
ledG.direction = digitalio.Direction.OUTPUT

def display_black():
  ledA.value = False
  ledB.value = False
  ledC.value = False
  ledD.value = False
  ledE.value = False
  ledF.value = False
  ledG.value = False

def display_init():
  t = 0.1
  for i in range(5):
    ledA.value = False
    ledB.value = False
    ledC.value = False
    ledD.value = False
    ledE.value = False
    ledF.value = False
    ledG.value = False
    ledA.value = True
    time.sleep(t)
    ledA.value = False
    ledB.value = True
    time.sleep(t)
    ledB.value = False
    ledC.value = True
    time.sleep(t)
    ledC.value = False
    ledD.value = True
    time.sleep(t)
    ledD.value = False
    ledE.value = True
    time.sleep(t)
    ledE.value = False
    ledF.value = True
    time.sleep(0.05)
    ledF.value = False

def display_test():
  display_black()
  for i in range(9):
    display_nb(i)
    time.sleep(0.2)
  display_black()

def display_nb(x):
  display_black()
  if x == 0:
    ledA.value = True
    ledB.value = True
    ledC.value = True
    ledD.value = True
    ledE.value = True
    ledF.value = True
    ledG.value = False
  elif x == 1:
    ledA.value = False
    ledB.value = True
    ledC.value = True
    ledD.value = False
    ledE.value = False
    ledF.value = False
    ledG.value = False
  elif x == 2:
    ledA.value = True
    ledB.value = True
    ledC.value = False
    ledD.value = True
    ledE.value = True
    ledF.value = False
    ledG.value = True
  elif x == 3:
    ledA.value = True
    ledB.value = True
    ledC.value = True
    ledD.value = True
    ledE.value = False
    ledF.value = False
    ledG.value = True
  elif x == 4:
    ledA.value = False
    ledB.value = True
    ledC.value = True
    ledD.value = False
    ledE.value = False
    ledF.value = True
    ledG.value = True
  elif x == 5:
    ledA.value = True
    ledB.value = False
    ledC.value = True
    ledD.value = True
    ledE.value = False
    ledF.value = True
    ledG.value = True
  elif x == 6:
    ledA.value = True
    ledB.value = False
    ledC.value = True
    ledD.value = True
    ledE.value = True
    ledF.value = True
    ledG.value = True
  elif x == 7:
    ledA.value = True
    ledB.value = True
    ledC.value = True
    ledD.value = False
    ledE.value = False
    ledF.value = False
    ledG.value = False
  elif x == 8:
    ledA.value = True
    ledB.value = True
    ledC.value = True
    ledD.value = True
    ledE.value = True
    ledF.value = True
    ledG.value = True
  elif x == 9:
    ledA.value = True
    ledB.value = True
    ledC.value = True
    ledD.value = True
    ledE.value = False
    ledF.value = True
    ledG.value = True
  else:
    ledA.value = False
    ledB.value = False
    ledC.value = False
    ledD.value = False
    ledE.value = False
    ledF.value = False
    ledG.value = True
