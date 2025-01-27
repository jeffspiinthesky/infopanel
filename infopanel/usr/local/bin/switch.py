import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
refresh_pin=20
reboot_pin=21
next_pin=16
prev_pin=12
GPIO.setup(refresh_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(reboot_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(next_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(prev_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#initialise a previous input variable to 0 (assume button not pressed last)
prev_refresh = 0
prev_reboot = 0
prev_next = 0
prev_prev = 0
while True:
  #take a reading
  refresh_key = GPIO.input(refresh_pin)
  reboot_key = GPIO.input(reboot_pin)
  next_key = GPIO.input(next_pin)
  prev_key = GPIO.input(prev_pin)
  #if the last reading was low and this one high, print
  if ((not prev_refresh) and refresh_key):
    os.system("/usr/bin/xdotool key F5")
    #print("refresh")
  #update previous input
  prev_refresh = refresh_key
  if ((not prev_reboot) and reboot_key):
    os.system('sudo -S /sbin/shutdown -r 0')
    #print("reboot")
  #update previous input
  prev_reboot = reboot_key
  if ((not prev_next) and next_key):
    os.system("/usr/bin/xdotool key n")
    print("next")
  #update previous input
  prev_next = next_key
  if ((not prev_prev) and prev_key):
    os.system("/usr/bin/xdotool key p")
    print("prev")
  #update previous input
  prev_prev = prev_key
  #slight pause to debounce
  time.sleep(0.05)
