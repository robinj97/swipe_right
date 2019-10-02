from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)

while True:
    keyboard.press(Key.right)
    keyboard.release(Key.right)
