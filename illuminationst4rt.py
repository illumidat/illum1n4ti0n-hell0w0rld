import pyautogui
import time

i = 1

print(
    "Illumination Anti AFK started working, if you want to stop it, simply close this terminal."
)

time.sleep(5)
pyautogui.moveTo(1010, 381)

while i <= 10:
    time.sleep(10)
    pyautogui.doubleClick()
