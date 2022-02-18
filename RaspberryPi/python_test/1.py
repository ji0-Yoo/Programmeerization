import threading
import time

flag_exit = False
def t1_main():
  while True:
    print("\tt1")
    time.sleep(0.5)
    # 0.5초 쉬면서 t1이라는 메세지 찍어라 
    if flag_exit: break
  
t1 = threading.Thread(target=t1_main)
t1.start()

try:
  while True:
    print("main")
    time.sleep(1.0)
    # 1초 마다 main이라는 메세지 찍어라 

except KeyboardInterrupt:
  pass

flag_exit = True
t1.join()