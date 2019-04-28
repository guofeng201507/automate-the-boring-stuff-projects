import time
import pyautogui

time.sleep(3)
wechat_window = pyautogui.locateCenterOnScreen('wechat.png')
pyautogui.click(wechat_window)

wechatsearch_icon = pyautogui.locateCenterOnScreen('searchWechat.png')

pyautogui.click(wechatsearch_icon)

pyautogui.typewrite('wu')
time.sleep(1)
pyautogui.moveRel(0, 10, 0.5)

pyautogui.click()
time.sleep(1)
pyautogui.typewrite('I am testing my chatbot')
time.sleep(3)
pyautogui.press('enter')

pyautogui.typewrite('It works, Oh YEAH!')

pyautogui.press('enter')