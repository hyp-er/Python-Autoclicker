import pynput
import time
from pynput.mouse import Button, Controller

mouse = Controller()

for x in range(50):
  mouse.press(Button.left)
  mouse.release(Button.left)

print('the autoclicker has run succesfully!')