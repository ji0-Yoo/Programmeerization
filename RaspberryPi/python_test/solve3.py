import RPi.GPIO as GPIO
import time

buzzer_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 1.0)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
key = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k']

try:
  while True:
    userInput = input()

    # userInput = input() # for string
		# print(userInput)
		# for note in range(0,len(keys)):
		# 	if userInput == keys[note]:
		# 		pwm.ChangeFrequency(melody[note])
		# 		pwm.ChangeDutyCycle(50.0)
		# 		time.sleep(0.5)
		# 		pwm.ChangeDutyCycle(0.0)
		# 		break


    pwm.start(50.0)
    if userInput == key[0]:
      pwm.ChangeFrequency(melody[0])
      time.sleep(0.5)
    if userInput == key[1]:
      pwm.ChangeFrequency(melody[1])
      time.sleep(0.5)
    if userInput == key[2]:
      pwm.ChangeFrequency(melody[2])
      time.sleep(0.5)
    if userInput == key[3]:
      pwm.ChangeFrequency(melody[3])
      time.sleep(0.5)
    if userInput == key[4]:
      pwm.ChangeFrequency(melody[4])
      time.sleep(0.5)
    if userInput == key[5]:
      pwm.ChangeFrequency(melody[5])
      time.sleep(0.5)
    if userInput == key[6]:
      pwm.ChangeFrequency(melody[6])
      time.sleep(0.5)
    if userInput == key[7]:
      pwm.ChangeFrequency(melody[7])
      time.sleep(0.5)
    pwm.stop()


except KeyboardInterrupt:
  pass

GPIO.cleanup()