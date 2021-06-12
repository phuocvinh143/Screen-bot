from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

# http://www.aimbooster.com/
# 661, 339
# 1259, 757

def click(x, y): 
  win32api.SetCursorPos((x, y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
  pic = pyautogui.screenshot(region=(661, 339, 600, 400))
  width, height = pic.size
  for x in range(0, width, 5):
    for y in range(0, height, 5):
      r, g, b = pic.getpixel((x, y))
      if b == 195 and g == 219:
        click(x + 661, y + 339)
        time.sleep(0.05)
        break