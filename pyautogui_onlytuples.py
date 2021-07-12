import pyautogui
from pyautogui import moveTo
from pyautogui import click
from pyautogui import dragTo

#FOR THIS TO WORK EACH BROWSER WINDOW HAS TO TAKE UP EXACTLY HALF OF THE SCREEN

#todo: dyanamically create tuple coordinates for the djson marks so i later can just enter in a number and
# it will copy that many for me
#TODO:maybe make a function that will calculcate the next excel cell down on my template

wh = pyautogui.size()

newtabtuple, searchidtuple, searchbuttontuple, lastnametuple, firstnametuple, midnametuple = (3184, 93), (3310, 378), (3554,376), (2936, 352), (3097, 345), (3243, 348)
DOBholdbeginTuple, DOBholdendTuple, countyTuple = (3334,362), (3435,362), (3187, 584)
testpaste = (2005,688)



def tuplelist_func(ID_input):
    y = 264
    tuplelist = []
    for i in range(1,ID_input + 1):
        tuplevar = (2050,y)
        tuplelist.append(tuplevar)
        y +=20
    return tuplelist

def makeDjsonTuples(ID_input,tuplelist):
    djsonvarlist = []
    for i in range(1,ID_input + 1):
        djsonvarname = "djsonTuple" + str(i)
        djsonvarlist.append(djsonvarname)
    excel_id_coordinates = dict(zip(djsonvarlist, tuplelist))
    return excel_id_coordinates

def DOBcopyv():
    moveTo(DOBholdbeginTuple)
    dragTo(DOBholdendTuple,duration =.30)
    pyautogui.hotkey('ctrl', 'c', interval = 0.15)

def paste():
    pyautogui.hotkey('ctrl', 'v', interval = 0.15)

# newtabtuple, searchidtuple, searchbuttontuple, lastnametuple, firstnametuple, midnametuple = (3184, 93), (3310, 378), (3554,376), (2936, 352), (3097, 345), (3243, 348)
# DOBholdbeginTuple, DOBholdendTuple, countyTuple = (3334,362), (3435,362), (3187, 584)
# testpaste = (2005,688)

ID_input = input("Number of ids:") or 20
tuplelist = tuplelist_func(ID_input)
excel_id_coordinates = makeDjsonTuples(ID_input, tuplelist)




