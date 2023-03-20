import pyautogui
import random
while True:
    x_offset = random.randint(-800, 800)
    y_offset = random.randint(-800, 800)
    new_x, new_y = pyautogui.position()
    new_x += x_offset
    new_y += y_offset
    pyautogui.moveTo(new_x, new_y, duration=0.6)
