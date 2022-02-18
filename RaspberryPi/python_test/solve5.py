import RPi.GPIO as GPIO

led_state = False
led_state_changed = False
def buttonPressed(channel):
  global led_state
  global led_state_changed
  led_state = True if not led_state else False
  led_state_changed = True

button_pin = 22
led_pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

GPIO.setup(button_pin, GPIO.IN)
GPIO.add_event_detect(button_pin, GPIO.RISING)
GPIO.add_event_callback(button_pin, buttonPressed)

try:
  while True:
    if led_state_changed == True:
      led_state_changed = False
      GPIO.output(led_pin, led_state)

except KeyboardInterrupt:
  pass

GPIO.cleanup()

# black 5 -> 6
# white 8 -> 15
# red 10 -> 1
# brown 14 -> 17
# yellow 18 -> 12
