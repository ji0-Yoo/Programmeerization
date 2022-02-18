import RPi.GPIO as GPIO
import time

A_IA_pwm = 19
A_IB = 16
B_IA_pwm = 18
B_IB = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(A_IA_pwm, GPIO.OUT)
GPIO.setup(A_IB, GPIO.OUT)
GPIO.setup(B_IA_pwm, GPIO.OUT)
GPIO.setup(B_IB, GPIO.OUT)

pwm = GPIO.PWM(A_IA_pwm, 1000.0)
pwm2 = GPIO.PWM(B_IA_pwm, 1000.0)
pwm.start(0.0)
pwm2.start(0.0)

try:
  while True:
    GPIO.output(A_IB, False)
    GPIO.output(B_IB, False)
    pwm.ChangeDutyCycle(0.0)
    pwm2.ChangeDutyCycle(0.0)
    time.sleep(1.0)
    GPIO.output(A_IB, True)
    GPIO.output(B_IB, True)
    pwm.ChangeDutyCycle(0.0)
    pwm2.ChangeDutyCycle(0.0)
    time.sleep(1.0)
    GPIO.output(A_IB, True)
    GPIO.output(B_IB, True)
    pwm.ChangeDutyCycle(100.0)
    pwm2.ChangeDutyCycle(100.0)
    time.sleep(1.0)
    GPIO.output(A_IB, False)
    GPIO.output(B_IB, False)
    pwm.ChangeDutyCycle(100.0)
    pwm2.ChangeDutyCycle(100.0)
    time.sleep(1.0)

except KeyboardInterrupt:
  pass

pwm.ChangeDutyCycle(0.0)
pwm2.ChangeDutyCycle(0.0)

pwm.stop()
pwm2.stop()
GPIO.cleanup()