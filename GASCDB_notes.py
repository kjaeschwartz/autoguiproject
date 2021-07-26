import pyautogui
import webbrowser,time
import openpyxl
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
# ETAdate = input("enter the ETA date in mm/dd/yyyy format:")
ETAdate = "7/28/2021"

def get_ETA():
    ids_wb = openpyxl.load_workbook('py_id_excel.xlsm')
    ids_sheet = ids_wb['ids_list']
    ETA_date = ids_sheet['F2']
    return ETA_date
                         #
                         # 1366,751
def get_wind():
    pyautogui.getWindowsWithTitle('ATM - Google Chrome')
    pyautogui.click(1737,5)
    pyautogui.hotkey('ctrl','r', interval = .05)
    pyautogui.press('enter', interval=.05)
# press_b = pyautogui.hotkey('b', interval=.05)
def awaiting_action():
    for i in range (31):
        pyautogui.press('tab',interval = .05)
    # time.sleep(.1)
    # pyautogui.click(1375,754)
    time.sleep(.1)
    pyautogui.press('enter', interval=.05)
    pyautogui.press('a', interval=.05)
    pyautogui.press('enter', interval=.05)
    time.sleep(.05)

def palalt():
    for i in range (13):
        pyautogui.press('tab',interval = .03)
    #time.sleep(.07)
    time.sleep(.15)
    pyautogui.press('left', interval=.05)
    pyautogui.press('down', interval=.05)
    pyautogui.press('left', interval=.05)
    pyautogui.typewrite("Emailed consent form to Palo Alto Police Department. Turnaround time is 3 business days.")

def vend_eta(ETAdate):
    pyautogui.press('tab', interval=.05)
    # pyperclip.copy(ETA_date)
    # pyperclip.paste()
    pyautogui.typewrite(ETAdate)
    time.sleep(.15)
    pyautogui.press('tab')
    time.sleep(.15)
    pyautogui.typewrite('Emailed to Palto Alto Police Department')
    time.sleep(.15)

ETA = get_ETA()
time.sleep(.15)
get_wind()
time.sleep(.15)
awaiting_action()
time.sleep(.1)
palalt()
time.sleep(.15)
vend_eta(ETAdate)