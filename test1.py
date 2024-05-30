# Test 1
# - swing turn
# - sleep 0

import sys
import time
import RPi.GPIO as GPIO

sys.path.append('/home/user')

from motor_test import AlphaBot2 
from AlphaBot2.python.TRSensors import TRSensor

import RPi.GPIO as GPIO
import time

class AlphaBot2(object):
  def __init__(self,ain1=12,ain2=13,ena=6,bin1=20,bin2=21,enb=26):
    self.AIN1 = ain1    # backward signal of left wheel
    self.AIN2 = ain2    # forward signal of left wheel
    self.BIN1 = bin1    # backward signal of right wheel
    self.BIN2 = bin2    # forward signal of right wheel
    self.ENA = ena      # enable signal of left wheel
    self.ENB = enb      # enable signal of right wheel
    self.PA  = 20   # speed of left wheel
    self.PB  = 20   # speed of right wheel
  
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(self.AIN1,GPIO.OUT)
    GPIO.setup(self.AIN2,GPIO.OUT)
    GPIO.setup(self.BIN1,GPIO.OUT)
    GPIO.setup(self.BIN2,GPIO.OUT)
    GPIO.setup(self.ENA,GPIO.OUT)
    GPIO.setup(self.ENB,GPIO.OUT)
    self.PWMA = GPIO.PWM(self.ENA,500)
    self.PWMB = GPIO.PWM(self.ENB,500)
    self.PWMA.start(self.PA)
    self.PWMB.start(self.PB)
    self.stop()
  
  def forward(self):
    self.PWMA.ChangeDutyCycle(self.PA)
    self.PWMB.ChangeDutyCycle(self.PB)
    GPIO.output(self.AIN1,GPIO.LOW)
    GPIO.output(self.AIN2,GPIO.HIGH)
    GPIO.output(self.BIN1,GPIO.LOW)
    GPIO.output(self.BIN2,GPIO.HIGH)
  
  def stop(self):
    self.PWMA.ChangeDutyCycle(0)
    self.PWMB.ChangeDutyCycle(0)
    GPIO.output(self.AIN1,GPIO.LOW)
    GPIO.output(self.AIN2,GPIO.LOW)
    GPIO.output(self.BIN1,GPIO.LOW)
    GPIO.output(self.BIN2,GPIO.LOW)
  
  def backward(self):
    self.PWMA.ChangeDutyCycle(self.PA)
    self.PWMB.ChangeDutyCycle(self.PB)
    GPIO.output(self.AIN1,GPIO.HIGH)
    GPIO.output(self.AIN2,GPIO.LOW)
    GPIO.output(self.BIN1,GPIO.HIGH)
    GPIO.output(self.BIN2,GPIO.LOW)
  
  def left(self):
    self.PWMA.ChangeDutyCycle(25)
    self.PWMB.ChangeDutyCycle(25)
    GPIO.output(self.AIN1,GPIO.HIGH)
    GPIO.output(self.AIN2,GPIO.LOW)
    GPIO.output(self.BIN1,GPIO.LOW)
    GPIO.output(self.BIN2,GPIO.HIGH)
  
  def right(self):
    self.PWMA.ChangeDutyCycle(25)
    self.PWMB.ChangeDutyCycle(25)
    GPIO.output(self.AIN1,GPIO.LOW)
    GPIO.output(self.AIN2,GPIO.HIGH)
    GPIO.output(self.BIN1,GPIO.HIGH)
    GPIO.output(self.BIN2,GPIO.LOW)
  
  def swing_left(self):
    self.PWMA.ChangeDutyCycle(0)
    self.PWMB.ChangeDutyCycle(25)
    GPIO.output(self.AIN1,GPIO.HIGH)
    GPIO.output(self.AIN2,GPIO.LOW)
    GPIO.output(self.BIN1,GPIO.LOW)
    GPIO.output(self.BIN2,GPIO.HIGH)
  
  def swing_right(self):
    self.PWMA.ChangeDutyCycle(25)
    self.PWMB.ChangeDutyCycle(0)
    GPIO.output(self.AIN1,GPIO.LOW)
    GPIO.output(self.AIN2,GPIO.HIGH)
    GPIO.output(self.BIN1,GPIO.HIGH)
    GPIO.output(self.BIN2,GPIO.LOW)
  
  def curve_left(self):
    self.PWMA.ChangeDutyCycle(self.PA * 0.5)
    self.PWMB.ChangeDutyCycle(self.PB)
    GPIO.output(self.AIN1,GPIO.HIGH)
    GPIO.output(self.AIN2,GPIO.LOW)
    GPIO.output(self.BIN1,GPIO.LOW)
    GPIO.output(self.BIN2,GPIO.HIGH)
  
  def curve_right(self):
    self.PWMA.ChangeDutyCycle(self.PA)
    self.PWMB.ChangeDutyCycle(self.PB * 0.5)
    GPIO.output(self.AIN1,GPIO.LOW)
    GPIO.output(self.AIN2,GPIO.HIGH)
    GPIO.output(self.BIN1,GPIO.HIGH)
    GPIO.output(self.BIN2,GPIO.LOW)
  
  
  def setPWMA(self,value):
    self.PA = value
    self.PWMA.ChangeDutyCycle(self.PA)
  
  def setPWMB(self,value):
    self.PB = value
    self.PWMB.ChangeDutyCycle(self.PB)
        
        
if __name__=='__main__':
  # Wheel setup
  whl = AlphaBot2()
  
  # Button setup
  Button = 7
  
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(Button,GPIO.IN,GPIO.PUD_UP)
  
  print("Press button to start")
  
  # Sensor
  TR = TRSensor()
  while (GPIO.input(Button) != 0):
    time.sleep(0.05)
  
  while (GPIO.input(Button) != 0):
    time.sleep(0.05)
  
  try:
    while True:
      sensors = TR.AnalogRead()
      middle_sensor = sensors[2]      
      print(middle_sensor)
      
      whl.forward()
      
      if middle_sensor > 500:
        # move left slightly
        whl.swing_left()
        #time.sleep(0.05)
      else:
        # move right slightly
        whl.swing_right()
        #time.sleep(0.05)
  except:
    print("except")
    GPIO.cleanup()
