import pyautogui
import webbrowser

fw = pyautogui.getWindowsWithTitle('ATM - Google Chrome')
pyautogui.scroll(200)
if len(fw) == 0:
    print("l is 0")
    webbrowser.open('https://atm.accuratebackground.com/atm/login.jsp')
    fw = pyautogui.getWindowsWithTitle('Vendor Login | Accurate Background - Google Chrome')
fw = fw[0]
fw.width = 974
fw.topleft = (953, 0)