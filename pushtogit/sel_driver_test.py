from selenium import webdriver
import clipboard
from PIL import Image
import pyautogui
import webbrowser,time
from pathlib import Path
import openpyxl
driver = webdriver.Chrome('chromedriver.exe')

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


login()
ids_list = get_ids()
print(ids_list)

