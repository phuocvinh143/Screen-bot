from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# https://www.agame.com/game/magic-piano-tiles
# column 1: X = 589, Y = 525
# column 2: X = 689, Y = 525
# column 3: X = 789, Y = 525
# column 4: X = 889, Y = 525

def click(x, y): 
  win32api.SetCursorPos((x, y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
  time.sleep(0.01)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

time.sleep(1)

while keyboard.is_pressed('q') == False:
  if pyautogui.pixel(589, 525)[0] == 0: click(589, 525)
  if pyautogui.pixel(689, 525)[0] == 0: click(689, 525)
  if pyautogui.pixel(789, 525)[0] == 0: click(789, 525)
  if pyautogui.pixel(889, 525)[0] == 0: click(889, 525)