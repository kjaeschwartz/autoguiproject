import webbrowser
import openpyxl
from selenium import webdriver
import pyautogui
import pyAgui_cmds
from openids_real_pySEL import test_id_open
import time
import clipboard

prev_cellinfo = []
driver = webdriver.Chrome('chromedriver.exe')

lastname,firstname,middlename,dob = [],[],[],[]
aka1first,aka1last,aka2first,aka2last,aka3first,aka3last = [],[],[],[],[],[]
tableinfolistlist = [lastname,firstname,aka1first,aka1last,aka2first,aka2last,aka3first,aka3last,dob]

Lnm,Fnm,aka1L,akaF,aka2L,aka2F,aka3L,aka3F,DOB = [333,297],[488,297],[333,325],[488,320],[333,340],[488,345],[333,370],[488,372],[264,454]
coords_list = [Lnm,Fnm,aka1L,akaF,aka2L,aka2F,aka3L,aka3F,DOB]

def get_clipboard():
    clipboard_content = clipboard.paste()
    clipboard_content = (clipboard_content.replace(' ', ''))
    print(clipboard_content)
    return(clipboard_content)
def pywinEDITBUTTONclicktest():  # success!!
    pyAgui_cmds.pywin_doubleclick_editbutton()
    pyAgui_cmds.pywin_click_editbutton()
    return "pywinEDITBUTTONclicktest"
def tabcopyall():
    def copystuff():
        time.sleep(.06)
        pyautogui.press('enter',interval= .01)
        pyautogui.hotkey('ctrl','a',interval=.01)
        # copy()
        pyautogui.hotkey('ctrl','c',interval=.01)
        clipinfo = get_clipboard()
        return clipinfo
    def specialtabrules(iteratorIndex):
        if iteratorIndex == 0:
            pyautogui.doubleClick(333, 297)
            pyautogui.click()
            cellinfo = copystuff()
            pyautogui.press('tab')
            time.sleep(.005)
        elif iteratorIndex == 8:
            copystuff()
            cellinfo = copystuff()
            pyautogui.press('tab',presses = 3)
            time.sleep(.005)
        elif iteratorIndex % 2 == 1:
            copystuff()
            cellinfo = copystuff()
            pyautogui.press('tab',presses = 2)
            time.sleep(.001)
        elif iteratorIndex % 2 == 0:
            copystuff()
            cellinfo = copystuff()
            pyautogui.press('tab')
            time.sleep(.001)
    for coords in coords_list:
        start = time.time()
        specialtabrules(coords_list.index(coords))
        cellinfo = copystuff()
        if coords_list.index(coords) == 0:
            print(f"first cell, init prev_cellinfo with {cellinfo}")
            prev_cellinfo.append(cellinfo)
            tableinfolistlist[coords_list.index(coords)].append(cellinfo)
        elif cellinfo == prev_cellinfo[0]:
            print(f"nothing in the space, nothing added to listlist")
            tableinfolistlist[coords_list.index(coords)].append("")
        elif cellinfo != prev_cellinfo[0]:
            print(f"new info of {cellinfo} added to listlist")
            prev_cellinfo.pop(0)
            prev_cellinfo.append(cellinfo)
            tableinfolistlist[coords_list.index(coords)].append(cellinfo)
        # keeping these around just in case I want to time this function
        end = time.time()
        elapsed = end - start
    # for i in range(0,len(tableinfolistlist)):
    #     return
    #     # if i == 0:
    #     #     pyautogui.doubleClick(333,297)
    #     #     pyautogui.click()
    #     #     cellinfo = copystuff()
    #     #     tableinfolistlist[i].append(cellinfo)
    #     #     pyautogui.press('tab', interval=.1)
    #     #     time.sleep(.05)
    #     # elif i == 8:
    #     #     for i in range(3):
    #     #         copystuff()
    #     #         cellinfo = copystuff()
    #     #         tableinfolistlist[i].append(cellinfo)
    #     #         pyautogui.press('tab',interval =.1)
    #     #         time.sleep(.05)
    #     # elif i % 2 == 1:
    #     #     for i in range(2):
    #     #         copystuff()
    #     #         cellinfo = copystuff()
    #     #         tableinfolistlist[i].append(cellinfo)
    #     #         pyautogui.press('tab',interval =.1)
    #     #         time.sleep(.05)
    #     # elif i % 2 == 0:
    #     #     copystuff()
    #     #     cellinfo = copystuff()
    #     #     tableinfolistlist[i].append(cellinfo)
    #     #     pyautogui.press('tab', interval=.1)
    #     #     time.sleep(.05)
    # return "tabcopyall"
def tabeditbutton():
    pyautogui.click(160, 204)
    pyautogui.press("tab", presses=9)
    pyautogui.press('enter')
def clickandcopyall():
    def copystuff():
        time.sleep(.01)
        pyautogui.click()
        pyautogui.hotkey('ctrl','a',interval=.01)
        # copy()
        pyautogui.hotkey('ctrl','c',interval=.01)
        clipinfo = get_clipboard()
        return clipinfo
    for coords in coords_list:
        start = time.time()
        pyautogui.doubleClick(coords[0], coords[1], interval=.005)
        cellinfo = copystuff()
        tableinfolistlist[coords_list.index(coords)].append(cellinfo)
        end = time.time()
        elapsed = end - start
    return "clickandcopyall"
def runtestsAndOtherStuff():
    timer("test_id_open")
    timer("pywinEDITBUTTONclicktest")
    timer("clickandcopyall")
def timer(functionvar):
    start = time.time()
    if functionvar == "test_id_open":
        test_id_open()
    elif functionvar == "pywinEDITBUTTONclicktest":
        pywinEDITBUTTONclicktest()
    elif functionvar == "clickandcopyall":
        clickandcopyall()
    elif functionvar == "tabcopyall":
        tabcopyall()
    elif functionvar == "runtestsAndOtherStuff":
        test_id_open()
        pywinEDITBUTTONclicktest()
        clickandcopyall()
    elif functionvar == "runintegratedtest":
        pywinEDITBUTTONclicktest()
        clickandcopyall()
        # runtestsAndOtherStuff()
    elif functionvar == "integratedtabtime":
        tabeditbutton()
        tabcopyall()
    end = time.time()
    elapsed = end - start
    print(f"\nperforming {functionvar} function took {elapsed} time")
    return elapsed  # print(f"\nperforming {functionvar} function took {elapsed} time")
# class djson_stuff():
#     def get_names():
#         ids_wb = openpyxl.load_workbook('py_id_excel.xlsm')
#         names_sheet = ids_wb['test_names_sheet']
#         for rowOfCellObjects in ids_sheet['A2':'A51']:
#             for cellObj in rowOfCellObjects:
#                 # print(cellObj.coordinate, cellObj.value)
#                 if cellObj.value != None:
#                     firstnameslist.append(cellObj.value)
#         for rowOfCellObjects in ids_sheet['B2':'B51']:
#             for cellObj in rowOfCellObjects:
#                 # print(cellObj.coordinate, cellObj.value)
#                 if cellObj.value != None:
#                     lastnameslist.append(cellObj.value)
#         return
#
#     def new_window():
#         newwin = pyautogui.hotkey("ctrl", "n", interval=.1)
#         return
#     def DJSON():
#         pushright = pyautogui.hotkey('winleft', 'right', interval=.07)
#         return
def login():
    driver.get("https://atm.accuratebackground.com/atm/findSearch.html")
    driver.find_element_by_id('userName').send_keys("kschwartz277")
    driver.find_element_by_id('userPassword').send_keys("Hornet@559")
    loginbutton = driver.find_element_by_css_selector("button.btn.btn-primary")
    loginbutton.click()
# gets ids from the excel sheet
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
def make_driver_window():
    driver.get("https://atm.accuratebackground.com/atm/findSearch.html")
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
def enter_ids(ids_list):
    for i in range(len(ids_list)):
        # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.execute_script("window.open('https://atm.accuratebackground.com/atm/findSearch.html','_blank')")
        time.sleep(.3)
        pyautogui.typewrite(str(ids_list[i]))
        time.sleep(.1)
        print("hi")
        for i in range(4):
            pyautogui.press("tab",interval=.02)
        time.sleep(.1)
        pyautogui.press("enter")
        time.sleep(2)
        #----------------place commands here
        timer("integratedtabtime")
        # pywinEDITBUTTONclicktest()
        pyautogui.click()
        time.sleep(.1)

def test_id_open():
    login()
    id_list = get_ids()
    id_list = ["214486493"]
    enter_ids(id_list)
def all_ids_open():
    login()
    id_list = get_ids()
    enter_ids(id_list)

all_ids_open()
