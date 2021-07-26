from PIL import Image
import pyautogui

from pathlib import Path
#IMPORTANT!!!!!: SEARCH SCREEN MUST BE IN SPLIT SCREEN MOVE, NOT FULL SCREEN.
#IMPORTANT!!!!!!!! SEARCH SCREEN MUST BE IN SAME SCREEN AS PYCHARM, BOTH MUST BE ON THE LEFT SCREEN
#TODO: FIX DUAL SCREEN PROBLEM
wh = pyautogui.size()


state_py3 = Path("C:\\Users\kschwartz\Desktop\extra_stuff_i_guess\state-py3")

def check_screenshot_acc(imagefinder,newpngname):
    print(imagefinder)
    pyautogui.moveTo(imagefinder,duration = .15)
    screenshot = pyautogui.screenshot(region=(imagefinder))
    screenshot.save(state_py3/newpngname)


def find_picture_location(png_name):
    finder_pngs = Path("C:\\Users\kschwartz\Desktop\extra_stuff_i_guess\state-py3\Finder_pngs")
    openedImage = Image.open(finder_pngs/png_name)
    imagefinder = pyautogui.locateOnScreen(openedImage,confidence = .93)
    newpngname = "acctest_results\\acctest_" + png_name
    check_screenshot_acc(imagefinder,newpngname)


#if i wanna be picky i could put this in the function but eh, right now it makes more sense to leave it here
pngs_to_get = ["DOB_pic.png", "county_png.png","last_pic.png",  "first_pic.png",  "middle_png.png",
               "aka1_first_png.png", "aka2_first_png.png", "aka3_first_pic.png",'aka1_last_png.png',
               "aka2_last_png.png", "aka3_last_pic.png"]

def search_profile_fetch():
    for i in pngs_to_get:
        find_picture_location(i)

def search_id_fetch():
    findsearch = ["enter_id_box.png","search_press_box.png"]
    for i in findsearch:
        find_picture_location(i)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')

def move_to_word():
    fillervar = "foo"

search_profile_fetch()
search_id_fetch()
