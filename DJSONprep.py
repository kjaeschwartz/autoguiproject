import webbrowser,time
import pyautogui

def do_thing():
    pyautogui.hotkey('ctrl', 'n', interval=.07)
    pyautogui.hotkey('winleft','left',interval=.07)
    time.sleep(.1)
    webbrowser.open('https://www.nsopw.gov/')
pyautogui.click(1200,200)
do_thing()