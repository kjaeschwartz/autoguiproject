from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import webbrowser,time
from pathlib import Path
import re
import urllib.request
import openpyxl
from lxml import html
import requests
from bs4 import BeautifulSoup

#imports for the pyppeteer test (will grab dynamic html that can be passed to bs4)
from pyppeteer import launch
import os
import asyncio



#TODO: UNABLE TO FIND ELEMENT ERROR IS BECAUSE THE PAGE IS DYNAMICALLY GENERATED, IM GONNA NEED TO USE THIS APPROACH https://iqss.github.io/dss-webscrape/web-scraping-approaches.html#dynamic-web-pages
driver = webdriver.Chrome('chromedriver.exe')

# global_dynamicUrl = "https://atm.accuratebackground.com/atm/selectSearchRequest.html"
# global_dynamicPage = requests.get(global_dynamicUrl)
# global_dynamicHtml = html.fromstring(global_dynamicPage.text)
# table_area = global_dynamicHtml.xpath('//*[@id="result"]/table')
# table_entries = table_area.find_elements_by_tag_name("tr")

def ajax_requests():
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    driver.execute_script("window.open('https://atm.accuratebackground.com/atm/findSearch.html')")
    log = driver.get_log('performance')
    return
def next_tab():
    pyautogui.hotkey("ctrl","tab")
def close_tab():
    pyautogui.hotkey("ctrl", "w")
def login():
    driver.get("https://atm.accuratebackground.com/atm/findSearch.html")
    driver.find_element_by_id('userName').send_keys("kschwartz277")
    driver.find_element_by_id('userPassword').send_keys("Hornet@559")
    loginbutton = driver.find_element_by_css_selector("button.btn.btn-primary")
    loginbutton.click()
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
# def check_exists_by_xpath(xpath):
#     try:
#         webdriver.find_element_by_xpath(xpath)
#     except NoSuchElementException:
#         return (False,"The element does not exist")
#     return True
def get_ids():
    ids_wb = openpyxl.load_workbook('py_id_excel.xlsm')
    ids_sheet = ids_wb['ids_list']

    ids_list = []
    for rowOfCellObjects in ids_sheet['A2':'A51']:
        for cellObj in rowOfCellObjects:
            # print(cellObj.coordinate, cellObj.value)
            if cellObj.value != None:
                ids_list.append(cellObj.value)
    return_vars = [ids_list,ids_wb]
    return return_vars
def enter_ids(ids_list):
    for i in range(len(ids_list)):
        # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.execute_script("window.open('https://atm.accuratebackground.com/atm/findSearch.html','_blank')")
        time.sleep(.3)
        pyautogui.typewrite(str(ids_list[i]))
        # driver.find_element_by_name('method.search').click()
        # find_element_by_css_selector('method\.search').click
        time.sleep(.1)
        for i in range(4):
            pyautogui.press("tab",interval=.02)
        time.sleep(.1)
        pyautogui.press("enter")
    pyautogui.hotkey("ctrl","2")
def copy_name():
    # output
    # first_name = driver.find_element_by_css_selector('#h2 > tbody > tr:nth-child(2) > td:nth-child(1)')
    # first_name = driver.find_element(By.XPATH, '//*[@id="h2"]/tbody/tr[2]/td[1]')
    # first_name = driver.find_element(By.XPATH, '//*[@id="h2"]/tbody/tr[2]/td[1]')
    time.sleep(1)
    # findelement_methods("findbyclassname","#h2 > tbody > tr:nth-child(2) > td:nth-child(1)")
    # print(first_name.text)
    # for c in first_name:
    #     print(c.text)
    return
def get_table_info(ids_wb):
    outputsheet = ids_wb['test_names_sheet']
    table_body = driver.find_element_by_xpath('//*[@id="result"]/table/tbody')
    rows = table_body.find_elements_by_tag_name('tr')
    print(rows)
def print_all_available_elements():
    ids = driver.find_elements_by_xpath('//*')
    for ii in ids:
        # print ii.tag_name
        print(ii)  # id name as string
def sel_html_download_test(): #failed sel html download test.
    # opts = Options()
    # #opts.binary_location = "Users\kschwartz\PycharmProjects\pythonProject\chromedriver.exe"
    # chrome_driver = os.getcwd() + "chromedriver.exe"
    # driver2 = webdriver.Chrome(options=opts, executable_path="Users\kschwartz\PycharmProjects\pythonProject\chromedriver.exe")
    # driver2.get(os.getcwd() + "/test.html")
    # soup = BeautifulSoup(driver.page_source)
    # print(soup.find(id="test").get_text())
    return
def testing_function():
    global_dynamicUrl = "https://atm.accuratebackground.com/atm/selectSearchRequest.html"
    global_dynamicPage = requests.get(global_dynamicUrl)
    global_dynamicHtml = html.fromstring(global_dynamicPage.text)
    WebDriverWait(driver, 1)
    table_area = global_dynamicHtml.xpath('//*[@id="result"]/table')
    print(table_area)
    table_entries = global_dynamicHtml.find_elements_by_tag_name("tbody")
    # table = driver.find_element_by_xpath('//*[@id="results"]/table')
    # entries = table.find_elements_by_tag_name("tr")
    # for i in entries:
    #     print(i)
def is_it_dynamic():
    currUrl = driver.current_url
    response = urllib.request.urlopen(currUrl)
    html = response.read()
    text = html.decode()
    re.findall("(.*?)", text)
    url = requests.get(currUrl)
    url.json()
def bs4_request():
    currhtml = driver.page_source
    print(currhtml)
    soup = BeautifulSoup(currhtml,"lxml")
    firstnameselect = soup.select('#h2 > tbody > :nth-child(2) > :nth-child(1)')
    print(firstnameselect)
def javascriptTest():
    jstest = "document.getElementById('h2');"
    jstest_res = driver.execute_script(jstest)
    print(jstest_res)
def main_body_commands():
    login()
    get_ids_vals = get_ids()
    ids_list = get_ids_vals[0]
    ids_wb = get_ids_vals[1]
    ids_list = ["213215288"]
    print(ids_list)
    enter_ids(ids_list)
    javascriptTest()
    bs4_request()


sel_html_download_test()
# handle_dynamic_pyppet()
#

# WebDriverWait(driver,2)
# selectorfirst = driver.find_element_by_css_selector('#h2 > tbody > :nth-child(2) > :nth-child(1)')
# print(selectorfirst)
# testing_function()
# ajax_requests()
# print(is_it_dynamic())
# get_table_info(ids_wb)
# copy_name()
# element_attribute = "trg"
# driver.find_element_by_partial_link_text("First:"),

# first = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located(By.CSS_SELECTOR, '#h2 > tbody > tr:nth-child(2) > td:nth-child(1)'))
# print(first.text)
# tbody = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//*[@id="result"]/table/tbody')))
# print(tbody.text)
