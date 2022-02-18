import RPi.GPIO as GPIO

led_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 100)
pwm.start(0.0)

try:
  while True:
    userInput = input()
    print(userInput)
    if userInput == "0":
      pwm.ChangeDutyCycle(0)
    if userInput == "5":
      pwm.ChangeDutyCycle(50.0)
    if userInput == "t" or userInput == "T":
      pwm.ChangeDutyCycle(100.0)

except KeyboardInterrupt:
  pass

pwm.stop()
GPIO.cleanup()