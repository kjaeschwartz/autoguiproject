import clipboard
from PIL import Image
import pyautogui
import webbrowser,time
import pywinauto
from pathlib import Path
import openpyxl
from console.utils import wait_key


def get_clipboard():
    clipboard_content = clipboard.paste()
    clipboard_content = (clipboard_content.replace(' ', ''))
    print(clipboard_content)
    return(clipboard_content)

def closetab():
    closetab = pyautogui.hotkey('ctrl', 'w', interval=.07)
    return
def tab():
    pyautogui.press("tab", interval=.02)
    time.sleep(.03)
    return

def new_win():
    newwin = pyautogui.hotkey("ctrl", "n", interval=.1)
    return
def enter():
    pyautogui.press("enter",interval = .05)
    return
def new_tab():
    newwin = pyautogui.hotkey("ctrl", "t", interval=.1)
    return
def pushleft():
    pushleft = pyautogui.hotkey("win", "left", interval=.1)
    return
def pushright():
    pushleft = pyautogui.hotkey("win", "right", interval=.1)
    return
def clickLwin():
    pyautogui.click(882,46)
    time.sleep(.1)
    return
def clickRwin():
    pyautogui.click(1900,37)
    time.sleep(.1)
    return
def copy():
    time.sleep(.1)
    copy= pyautogui.hotkey("ctrl", "c", interval=.1)
    time.sleep(.3)
    return
def sel_all():
    time.sleep(.1)
    sel_all = pyautogui.hotkey("ctrl", "a", interval=.1)
    time.sleep(.2)
    return
def pywin_click_editbutton():
    time.sleep(.05)
    pywinauto.mouse.click(button='left',coords=(200,343))
    # pyautogui.click(200, 343)
    time.sleep(.05)
    return
def click_editbutton():
    time.sleep(.05)
    pyautogui.click(200, 343)
    time.sleep(.05)
    return
def click_lastbox():
    pyautogui.click(286,284)
    return
def pywinclick(coord1,coord2):
    pywinauto.mouse.click(button='left',coords=(coord1,coord2))
    return
def pywin_doubleclick_editbutton():
    time.sleep(.05)
    pywinauto.mouse.double_click(button='left',coords=(200,343))
    # pyautogui.click(200, 343)
    time.sleep(.05)
    return
def pywinTripleClick(coord1,coord2):
    time.sleep(.05)
    pywinauto.mouse.click(button='left', coords=(coord1, coord2))
    pywinauto.mouse.double_click(button='left', coords=(coord1, coord2))
    time.sleep(.05)
    return
def pywinMouseMove(coord1,coord2):
    pywinauto.mouse.move(coords=(coord1, coord2))