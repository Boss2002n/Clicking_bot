import pyautogui as pg
import time
import names


'''Makes free accounts of otter.ai. Needs three pinned tabs, 
otter.ai accounts, otter.ai, 10minutemail.net in 
succession from left to right. Needs cell to fill to be at the top in otter.ai accounts'''

pg.hotkey("command", "tab")
y = 270
i = 1

tic = time.perf_counter()
k = 1
for j in range(4):
    pg.moveTo(600, 20, duration=0.5)  # 10 minute mail tab
    pg.click()
    pg.moveTo(600, 620, duration=0.5)  # Get another mail
    pg.click()
    time.sleep(i*2.5)
    pg.moveTo(600, 535, duration=0.5)  # Copy
    pg.click()
    pg.click()
    time.sleep(i)
    pg.moveTo(520, 20, duration=0.5)  # Otter ai tab
    pg.click()
    pg.moveTo(1150, 121, duration=0.5)  # Sign up
    pg.click()
    time.sleep(i*5)
    pg.moveTo(610, 611, duration=0.5)  # Text box
    pg.click()
    pg.keyDown("command")
    pg.keyDown("v")
    pg.keyUp("command")
    pg.keyUp("v")
    pg.press("enter")
    time.sleep(i*1.5)
    pg.typewrite("Qwerty123!")
    pg.press("enter")
    time.sleep(i*2)
    pg.typewrite(names.get_first_name())
    pg.press("tab")
    pg.typewrite(names.get_last_name())
    pg.press("enter")
    time.sleep(i*1.5)
    pg.moveTo(1195, 152, duration=0.5)  # Skip
    pg.click()
    time.sleep(i/2)
    pg.moveTo(1195, 152, duration=0.5)  # Skip
    pg.click()
    pg.sleep(i*4)
    pg.moveTo(656, 698, duration=0.5)
    pg.click()
    pg.moveTo(173, 138, duration=0.5)  # Profile
    pg.click()
    pg.moveTo(147, 520, duration=0.5)  # Logout
    pg.click()
    pg.moveTo(213, 17)  # excel
    pg.click()
    pg.moveTo(175, y, duration=0.5)  # cell
    pg.click()
    pg.keyDown("command")
    pg.keyDown("v")
    pg.keyUp("command")
    pg.keyUp("v")
    y += 20
    time.sleep(i*3)
    k += 1

toc = time.perf_counter()
print("Made {} accounts in {} seconds".format(k, toc - tic))
