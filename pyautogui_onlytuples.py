import pyautogui
from pyautogui import moveTo
from pyautogui import click
from pyautogui import dragTo

# FOR THIS TO WORK EACH BROWSER WINDOW HAS TO TAKE UP EXACTLY HALF OF THE SCREEN

# todo: dyanamically create tuple coordinates for the djson marks so i later can just enter in a number and
# it will copy that many for me
# TODO:maybe make a function that will calculcate the next excel cell down on my template

wh = pyautogui.size()

newtabtuple, searchidtuple, searchbuttontuple, lastnametuple, firstnametuple, midnametuple = (3184, 93), (3310, 378), (3554, 376), (2886, 352), (3036, 347), (3243, 348)
DOBholdbeginTuple, DOBholdendTuple, countyTuple = (3334, 362), (3435, 362), (3144, 590)
testpaste = (2005, 688)
WI_court_dob = (1993, 534)
last_name_box,first_name_box,county_box = (2099, 420), (2318,427),(2000,710)


def tuplelist_func(ID_input):
    y = 264
    tuplelist = []
    for i in range(1, ID_input + 1):
        tuplevar = (2050, y)
        tuplelist.append(tuplevar)
        y += 20
    return tuplelist


def makeDjsonTuples(ID_input, tuplelist):
    djsonvarlist = []
    for i in range(1, ID_input + 1):
        djsonvarname = "djsonTuple" + str(i)
        djsonvarlist.append(djsonvarname)
    excel_id_coordinates = dict(zip(djsonvarlist, tuplelist))
    return excel_id_coordinates


def DOBcopypaste(pastehere):
    moveTo(DOBholdbeginTuple, duration=.15)
    dragTo(DOBholdendTuple, duration=.30)
    pyautogui.hotkey('ctrl', 'c', interval=0.15)pyautogui.hotkey(pyautogui.hotkey('ctrl', 'v', interval=0.15)'ctrl', 'v', interval=0.15)
    moveTo(pastehere, duration=.15)
    click(pastehere, duration=.15)
    pyautogui.hotkey('ctrl', 'v', interval=0.15)


def gen_copypaste(copyhere, pastethere):
    moveTo(copyhere, duration=.15)
    for i in range(0, 2):
        click(copyhere, duration=.10)
    moveTo(pastethere, duration=.15)
    click(pastethere, duration=.15)
    pyautogui.hotkey('ctrl', 'v', interval=0.15)

def paste(pastehere):
    pyautogui.hotkey('ctrl', 'v', interval=0.15)


def get_L_name(lastnametuple, last_name_box):
    gen_copypaste(lastnametuple, last_name_box)

def get_F_name(firstnametuple, first_name_box):
    gen_copypaste(firstnametuple, first_name_box)

def get_county(countytuple, county_box):
    gen_copypaste(countytuple,county_box)

# newtabtuple, searchidtuple, searchbuttontuple, lastnametuple, firstnametuple, midnametuple = (3184, 93), (3310, 378), (3554,376), (2936, 352), (3097, 345), (3243, 348)
# DOBholdbeginTuple, DOBholdendTuple, countyTuple = (3334,362), (3435,362), (3187, 584)
# testpaste = (2005,688)

ID_input = 20 #input("Number of ids:") or 20
tuplelist = tuplelist_func(ID_input)
excel_id_coordinates = makeDjsonTuples(ID_input, tuplelist)
# pastehere = testpaste
pastehere1 = WI_court_dob
DOBcopypaste(pastehere1)
get_L_name(lastnametuple, last_name_box)
get_F_name(firstnametuple,first_name_box)
get_county(countyTuple,county_box)
with open(r"C:\\Users\kschwartz\Desktop\DOB_pic.png","r+") as DOBpicture:
    pyautogui.locateOnScreen(DOBpicture)