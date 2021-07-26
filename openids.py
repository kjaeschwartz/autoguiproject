import pyperclip3
import clipboard
from PIL import Image
import pyautogui
import webbrowser,time
from pathlib import Path
import openpyxl

# nexttab = pyautogui.hotkey('ctrl','tab', interval=.1)
# prev_tab = pyautogui.hotkey('ctrl','shift','tab', interval=.1)

lastdrag = [(1051,374),(1151,370)]
akalastdrag = [(1069,391),(1154,389)]
firstdrag = [(1196,375), (1340,372)]
akafirstdrag = [(1243,389),(1341,387)]
dobdrag = [ (1573,392), (1758,389)]
lastlist = []
firstlist = []
doblist = []
akafirstlist = []
akalastlist = []
draglist = [lastdrag,firstdrag,dobdrag,akalastdrag,akafirstdrag]
listlist = [lastlist,firstlist,doblist,akalastlist,akafirstlist]
#positions = [laststart, lastend , lastcenter,akalaststart,akalastend, akalastcenter,firststart, firstend,firstcenter, akafirststart, akafirstend, akafirstcenter, dobstart, dobend ]

def get_clipboard():
    clipboard_content = clipboard.paste()
    clipboard_content = (clipboard_content.replace(' ', ''))
    print(clipboard_content)

def get_ids():
    ids_wb = openpyxl.load_workbook('py_id_excel.xlsm')
    ids_sheet = ids_wb['ids_list']

    ids_list = []
    for rowOfCellObjects in ids_sheet['A2':'A51']:
        for cellObj in rowOfCellObjects:
            # print(cellObj.coordinate, cellObj.value)
            if cellObj.value != None:
                ids_list.append(cellObj.value)
    return ids_list

def movedrag(start,end):
    pyautogui.click(start, duration = .25)
    pyautogui.dragTo(end, duration = .15)
    clipboard_content = clipboard.paste()
    print(clipboard_content)
    return clipboard_content
def relative_drag():
    pyautogui.click()
    pyautogui.drag(100, 0)
    clipboard_content = clipboard.paste()
    print(clipboard_content)
    return clipboard_content


def DJSON():
    webbrowser.open_new('https://www.nsopw.gov/en/Search/Results')

def make_chrome_window():
    fw = pyautogui.getWindowsWithTitle('ATM - Google Chrome')
    pyautogui.scroll(200)
    if len(fw) == 0:
        print("l is 0")
        webbrowser.open('https://atm.accuratebackground.com/atm/login.jsp')
        fw = pyautogui.getWindowsWithTitle('Vendor Login | Accurate Background - Google Chrome')
    fw = fw[0]
    fw.width = 974
    fw.topleft = (953, 0)


def find_picture_location(png_name):
    finder_pngs = Path("C:\\Users\kschwartz\Desktop\extra_stuff_i_guess\state-py3\GUI_FIND_PNGS")
    openedImage = Image.open(finder_pngs/png_name)
    # searchbox = (1201, 391, 390, 23)
    imagefinder = pyautogui.locateOnScreen(openedImage, confidence=.6, grayscale = True)#, region=searchbox)
    print(f"imagefinger is:{imagefinder}")
    imagefinder = pyautogui.center(imagefinder)
    pyautogui.moveTo(imagefinder, duration=.15)


def goto_first_prof(id_list):
    make_chrome_window()
    for i in range(len(id_list)):
        time.sleep(.05)

        #
        pyautogui.click(1008, 374)
        for h in range(4):
            pyautogui.press('down')

    # for i in range(len(id_list)):
    #     time.sleep(.05)
    #     # test_pngs = ["dob_png.png","first_png.png","last_png.png"]
    #     # for i in test_pngs:
    #     #     find_picture_location(i)
    #     #     pyautogui.move(15, 0)
    #     #     time.sleep(.05)
    #     #     clipboard2 = relative_drag()
    #     #     if i == 0:
    #     #         doblist.append(clipboard2)
    #     #     elif i == 1:
    #     #         firstlist.append(clipboard2)
    #     #     elif i == 2:
    #     #         lastlist.append(clipboard2)
    #     #     time.sleep(.15)
    #     # pyautogui.hotkey('ctrl', 'shift', 'tab', interval=.1)
    #     pyautogui.click(1008, 374)
    #     time.sleep(.05)
    #     last = movedrag(lastdrag[0],lastdrag[1])
    #     lastlist.append(last)
    #     first = movedrag(firstdrag[0],firstdrag[1])
    #     firstlist.append(first)
    #     dob = movedrag(dobdrag[0],dobdrag[1])
    #     doblist.append(dob)
    #     akafirst = movedrag(akafirstdrag[0],akafirstdrag[1])
    #     akafirstlist.append(akafirst)
    #     akalast = movedrag(akalastdrag[0],akalastdrag[1])
    #     akalastlist.append(akalast)
    #     pyautogui.hotkey('ctrl', 'shift', 'tab', interval=.1)
    #     # draglist = [lastdrag, firstdrag, dobdrag, akalastdrag, akafirstdrag]
    #     # listlist = [lastlist, firstlist, doblist, akalastlist, akafirstlist]
#
# for i in range(0,len(draglist)):
#     adder = movedrag(draglist[i[0]],draglist[i[1]])
#     listlist[i].append(adder)
def get_new_tab():
    # make_chrome_window()
    webbrowser.open('https://www.google.com/')
    time.sleep(.1)
    open_bm_manager = pyautogui.hotkey('alt', 'e', interval=.05)
    time.sleep(.05)
    press_b = pyautogui.hotkey('b', interval=.05)
    time.sleep(.15)
    press_left = pyautogui.hotkey('right', interval=.05)
    time.sleep(.5)
    press_down = pyautogui.press('down', presses=6, interval=.01)
    press_enter = pyautogui.press('enter', interval=.05)
    prev_tab = pyautogui.hotkey('ctrl','shift','tab', interval=.15)
    close_tab = pyautogui.hotkey('ctrl','w', interval=.15)

#I have 5 pixels from when the label starts to when the word starts

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
        time.sleep(.05)
        enter_id_box = (1340,405)
        press_search_button = (1625,405)
        pyautogui.click(enter_id_box)
        time.sleep(.05)
        pyautogui.typewrite(h)
        pyautogui.click(press_search_button)

id_list = get_ids()
search_id_fetch(id_list)
# goto_first_prof(id_list)
# for i in range(0,len(listlist)):
#     print(listlist[i])

# last = movedrag(lastdrag[0],lastdrag[1])
# lastlist.append(last)