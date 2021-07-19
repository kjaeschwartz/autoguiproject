import pyperclip3
from PIL import Image
import pyautogui
import webbrowser,time
from pathlib import Path
import openpyxl


def get_ids():
    ids_wb = openpyxl.load_workbook('py_id_excel.xlsx')
    ids_sheet = ids_wb['ids_list']

    ids_list = []
    for rowOfCellObjects in ids_sheet['A2':'A51']:
        for cellObj in rowOfCellObjects:
            # print(cellObj.coordinate, cellObj.value)
            if cellObj.value != None:
                ids_list.append(cellObj.value)
    return ids_list

def get_new_tab():
    webbrowser.open('https://atm.accuratebackground.com/atm/login.jsp')
    time.sleep(.15)
    open_bm_manager = pyautogui.hotkey('alt', 'e', interval=.05)
    time.sleep(.05)
    press_b = pyautogui.hotkey('b', interval=.05)
    time.sleep(.05)
    press_left = pyautogui.hotkey('right', interval=.05)
    time.sleep(1)
    press_down = pyautogui.press('down', presses=6, interval=.05)
    press_enter = pyautogui.press('enter', interval=.05)
    prev_tab = pyautogui.hotkey('ctrl','shift','tab', interval=.1)
    close_tab = pyautogui.hotkey('ctrl','w', interval=.1)

def find_picture_location(png_name):
    finder_pngs = Path("C:\\Users\kschwartz\Desktop\extra_stuff_i_guess\state-py3\Finder_pngs")
    openedImage = Image.open(png_name)
    searchbox = (1201,391,390,23)
    imagefinder = pyautogui.locateOnScreen(openedImage,confidence = .6,region = searchbox )
    print(f"imagefinger is:{imagefinder}")
    imagefinder = pyautogui.center(imagefinder)
    pyautogui.moveTo(imagefinder,duration = .15)


def make_chrome_window():
    fw = pyautogui.getWindowsWithTitle('ATM - Google Chrome')
    if len(fw) == 0:
        print("l is 0")
        webbrowser.open('https://atm.accuratebackground.com/atm/login.jsp')
        fw = pyautogui.getWindowsWithTitle('Vendor Login | Accurate Background - Google Chrome')
    fw = fw[0]
    fw.width = 974
    fw.topleft = (953, 0)

def search_id_fetch(id_list):
    ids = id_list
    ids_str = []
    for i in ids:
        i = str(i)
        ids_str.append(i)
    ids_list = ids_str
    # for h in range(0,len(ids_list)):
    make_chrome_window()
    for h in ids_list:
        time.sleep(.05)
        get_new_tab()
        findsearch = ["enter_id_box.png", "search_press_box.png"]
        time.sleep(.15)
        enter_id_box = (1340,405)
        press_search_button = (1625,405)
        pyautogui.click(enter_id_box)
        time.sleep(.05)
        pyautogui.typewrite(h)
        pyautogui.click(press_search_button)

id_list = get_ids()
search_id_fetch(id_list)




