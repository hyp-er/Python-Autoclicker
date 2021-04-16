import pynput
import time
from pynput.mouse import Button, Controller

mouse = Controller()

for x in range(50):
  time.sleep(0.1)
  mouse.press(Button.left)
  mouse.release(Button.left)

print('the autoclicker has run succesfully!')
