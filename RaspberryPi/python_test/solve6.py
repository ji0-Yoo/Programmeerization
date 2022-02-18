import RPi.GPIO as GPIO

button_pin = 22
led_pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 100)
pwm.start(0.0)

buttonInputPrev = False
button_count = 0
# led_state_changed = [0, 50.0, 100.0]

try:
  while True:
      # for note in range(0, button_count):
      #   pwm.ChangeDutyCycle(led_state_changed[note])
      #   GPIO.output(led_pin, led_state)
      buttonInput = GPIO.input(button_pin)
      if buttonInput and not buttonInputPrev:

        button_count = button_count + 1
        if button_count == 3: 
          button_count = 0
          
        print(button_count)
        if button_count == 0:
          pwm.ChangeDutyCycle(0)
        elif button_count == 1:
          pwm.ChangeDutyCycle(50)
        elif button_count == 2:
          pwm.ChangeDutyCycle(100)

      buttonInputPrev = buttonInput
s

except KeyboardInterrupt:
  pass

pwm.stop()	
GPIO.cleanup()

# black 5 -> 6
# white 8 -> 15
# red 10 -> 1
# brown 14 -> 17
# yellow 18 -> 12
