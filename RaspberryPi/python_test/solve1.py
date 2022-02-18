import RPi.GPIO as GPIO

led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, False)

try:
  while True:
    userInput = input()
    print(userInput)
    if userInput == "n" or userInput == "N":
      GPIO.output(led_pin, True)
    if userInput == "f" or userInput == "F":
      GPIO.output(led_pin, False)

    # if led_state_changed == True:
    #   led_state_changed = False
    #   GPIO.output(led_pin, led_state)

except KeyboardInterrupt:
  pass

GPIO.cleanup()