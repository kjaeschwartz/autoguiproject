import pyautogui
from pyautogui import moveto
from pyautogui import click
from pyautogui import drag

#todo: dyanamically create tuple coordinates for the djson marks so i later can just enter in a number and
# it will copy that many for me
DJSON1, DJSON2, DJSON3, DJSON4, DJSON5, DJSON6, DJSON7, DJSON8, DJSON9, DJSON10, DJSON11, DJSON12, DJSON13, DJSON14, DJSON15, DJSON16, DJSON17, DJSON18, DJSON19, DJSON20, = Point(x=2050,y=264), Point(x=2050,y=284), Point(x=2050,y=304), Point(x=2050,y=324), Point(x=2050,y=344), Point(x=2050,y=364), Point(x=2050,y=384), Point(x=2050,y=404), Point(x=2050,y=424), Point(x=2050,y=444), Point(x=2050,y=464), Point(x=2050,y=484), Point(x=2050,y=504), Point(x=2050,y=524), Point(x=2050,y=544), Point(x=2050,y=564), Point(x=2050,y=584), Point(x=2050,y=604), Point(x=2050,y=624), Point(x=2051,y=625),
print(DJSON1)
djsonTuple1, djsonTuple2, djsonTuple3, djsonTuple4, djsonTuple5, djsonTuple6, djsonTuple7, djsonTuple8, djsonTuple9, djsonTuple10, djsonTuple11, djsonTuple12, djsonTuple13, djsonTuple14, djsonTuple15, djsonTuple16, djsonTuple17, djsonTuple18, djsonTuple19, djsonTuple20 = (2050,264), (2050,284), (2050,304), (2050,324), (2050,344), (2050,364), (2050,384), (2050,404), (2050,424), (2050,444), (2050,464), (2050,484), (2050,504), (2050,524), (2050,544), (2050,564), (2050,584), (2050,604), (2050,624), (2050,625)
# newTabSearch = Point(x=3184, y=93)
newtabtuple = (3184,93)
# searchidpos = Point(x=3310, y=378)
searchidtuple = (3310,378)
# searchbutton = Point(x=3554, y=376)
searchbuttontuple = (3554,376)
# lastname =Point(x=2936, y=352)
lastnametuple = (2936,352)
# firstname = Point(x=3097, y=345)
firstnametuple = (3097,345)
# midname = Point(x=3243, y=348)
midnametuple = (3243,348)
DOBholdbeginTuple = (3336,362)
DOBholdendTuple = (3410,365)
countyTuple =(3187,584)




wh = pyautogui.size()