import clipboard
from PIL import Image
import pyautogui
import webbrowser,time
from pathlib import Path
import openpyxl
from console.utils import wait_key

def do_thing():
    pyautogui.hotkey('ctrl', 'n', interval=.07)
    pyautogui.hotkey('winleft','left',interval=.07)
    time.sleep(.1)
    webbrowser.open('https://www.jud2.ct.gov/crdockets/parm1.aspx')
    prev_tab = pyautogui.hotkey('ctrl', 'shift', 'tab', interval=.1)
    close_tab = pyautogui.hotkey('ctrl', 'w', interval=.07)
    time.sleep(.1)
    webbrowser.open('https://www.jud2.ct.gov/crdockets/SearchByDefDisp.aspx')
    time.sleep(.1)
    pyautogui.press('tab', interval=.07)
    webbrowser.open('https://insights.appriss.com/login?targetUrl=%2F')
    time.sleep(.1)
    pyautogui.press('tab', interval=.07)
    webbrowser.open('https://rapidcourt.com/getsec2/')
pyautogui.click(1200,200)
do_thing()