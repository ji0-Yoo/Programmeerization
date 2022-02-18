import time
import RPi.GPIO as GPIO

button_pin =27
led_pin =22

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 1000.0)
pwm.start(0.0) # 0.0~100.0

buttonInputPrev = False
cnt = 0

try:
	while True:
		buttonInput = GPIO.input(button_pin);
    
		# print(buttonInput)
				
		if buttonInput and not buttonInputPrev:
      
			cnt = cnt + 1
			if cnt == 3: 
				cnt = 0
			
			print(cnt)
			time.sleep(0.3)
			if cnt == 0:
				pwm.ChangeDutyCycle(0)
			elif cnt == 1:
				pwm.ChangeDutyCycle(50)
			elif cnt == 2:
				pwm.ChangeDutyCycle(100)
		  
		buttonInputPrev = buttonInput
		
except KeyboardInterrupt:
	pass
	
pwm.stop()	
GPIO.cleanup()

