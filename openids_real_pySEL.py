import pyperclip3
import clipboard
from PIL import Image
import pyautogui
import webbrowser,time
from pathlib import Path
import openpyxl
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver.exe')


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
firstnameslist= []
lastnameslist = []
#positions = [laststart, lastend , lastcenter,akalaststart,akalastend, akalastcenter,firststart, firstend,firstcenter, akafirststart, akafirstend, akafirstcenter, dobstart, dobend ]

def findelement_methods(findbymethod, element_attribute):
    switcher = {
        "findbyname": driver.find_element_by_name(element_attribute),
        "findbyid": driver.find_element_by_id(element_attribute),
        "findbytagname": driver.find_element_by_tag_name(element_attribute),
        "findbypartialLink": driver.find_element_by_partial_link_text(element_attribute),
        "findbyfullLink": driver.find_element_by_link_text(element_attribute),
        "findbyclassname": driver.find_element_by_class_name(element_attribute),
        "findbyCSSselector": driver.find_element_by_css_selector(element_attribute),
        "findbyxpath": driver.find_element_by_xpath(element_attribute),
        "findbyxpathfull": driver.find_element_by_xpath(element_attribute)
    }
    Switch_func = switcher.get(findbymethod)
    # Execute the function
    Switch_func()
class djson_stuff():
    def get_names():
        ids_wb = openpyxl.load_workbook('py_id_excel.xlsm')
        names_sheet = ids_wb['test_names_sheet']
        for rowOfCellObjects in ids_sheet['A2':'A51']:
            for cellObj in rowOfCellObjects:
                # print(cellObj.coordinate, cellObj.value)
                if cellObj.value != None:
                    firstnameslist.append(cellObj.value)
        for rowOfCellObjects in ids_sheet['B2':'B51']:
            for cellObj in rowOfCellObjects:
                # print(cellObj.coordinate, cellObj.value)
                if cellObj.value != None:
                    lastnameslist.append(cellObj.value)
        return

    def new_window():
        newwin = pyautogui.hotkey("ctrl", "n", interval=.1)
        return
    def DJSON():
        pushright = pyautogui.hotkey('winleft', 'right', interval=.07)
        return

def login():
    driver.get("https://atm.accuratebackground.com/atm/findSearch.html")
    driver.find_element_by_id('userName').send_keys("kschwartz277")
    driver.find_element_by_id('userPassword').send_keys("Hornet@559")
    loginbutton = driver.find_element_by_css_selector("button.btn.btn-primary")
    loginbutton.click()
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
def get_names():
    return
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
        for i in range(4):
            pyautogui.press("tab",interval=.02)
        time.sleep(.1)
        pyautogui.press("enter")

def test_id_open():
    login()
    id_list = get_ids()
    id_list = ["214486493"]
    enter_ids(id_list)
def all_ids_open():
    login()
    id_list = get_ids()
    id_list = ["214486493"]
    enter_ids(id_list)

# goto_first_prof(id_list)
# for i in range(0,len(listlist)):
#     print(listlist[i])

# last = movedrag(lastdrag[0],lastdrag[1])
# lastlist.append(last)