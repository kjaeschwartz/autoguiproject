import pyautogui
import pyAgui_cmds
from openids_real_pySEL import test_id_open
import time
from pyAgui_cmds import tab,enter,click_editbutton,new_tab,new_win,closetab,get_clipboard,clickRwin,clickLwin,copy,sel_all


lastname,firstname,middlename,dob = [],[],[],[]
aka1first,aka1last,aka2first,aka2last,aka3first,aka3last = [],[],[],[],[],[]
tableinfolistlist = [lastname,firstname,middlename,dob,aka1first,aka1last,aka2first,aka2last,aka3first,aka3last]

Lnm,Fnm,aka1L,akaF,aka2L,aka2F,aka3L,aka3F,DOB = [333,297],[488,297],[333,325],[488,320],[333,340],[488,345],[333,370],[488,372],[264,454]
coords_list = [Lnm,Fnm,aka1L,akaF,aka2L,aka2F,aka3L,aka3F,DOB]

def get_editpage():
    clickLwin()
    for i in range(12):
        tab()
        time.sleep(.1)
    enter()
# def pywinclick_editbutton():
#     pyAgui_cmds.pywin_click_editbutton()
# def click_editpage():
#     time.sleep(.1)
#     click_editbutton()
# def lastnamebox():
#     clickLwin()
#     for i in range(9):
#         tab()
#     enter()
#     sel_all()
#     copy()
#     lastN = get_clipboard()
#     lastname.append(lastN)
# def lastnameclick():
#     time.sleep(.1)
#     click_lastbox()
#     time.sleep(.1)
# class databoxes():
#     def firstname():
#         enter()
#         time.sleep(.1)
#         tab()
#         copy()
#         firstN= get_clipboard()
#         firstname.append(firstN)
#         return firstN
#     def aka1last():
#         enter()
#         time.sleep(.1)
#         tab()
#         time.sleep(.1)
#         tab()
#         copy()
#         varN= get_clipboard()
#         aka1last.append(varN)
#         return varN
#     def aka1first():
#         enter()
#         time.sleep(.1)
#         tab()
#         copy()
#         time.sleep(.1)
#         varN= get_clipboard()
#         aka1last.append(varN)
#         return varN
#     def aka2lastt():
#         enter()
#         time.sleep(.1)
#         tab()
#         time.sleep(.1)
#         tab()
#         copy()
#         varN= get_clipboard()
#         aka2last.append(varN)
#         return varN
#     def aka2first():
#         enter()
#         time.sleep(.1)
#         tab()
#         copy()
#         time.sleep(.1)
#         varN= get_clipboard()
#         aka2first.append(varN)
#         return varN
#     def aka3last():
#         enter()
#         time.sleep(.1)
#         tab()
#         time.sleep(.1)
#         tab()
#         copy()
#         varN= get_clipboard()
#         aka3last.append(varN)
#         return varN
#     def aka3first():
#         enter()
#         time.sleep(.1)
#         tab()
#         copy()
#         time.sleep(.1)
#         varN= get_clipboard()
#         aka3first.append(varN)
#         return varN
#     def DOB():
#         for i in range(3):
#             tab()
#         copy()
#         time.sleep(.1)
#         varN= get_clipboard()
#         DOB.append(varN)
#         return varN
# def test_databoxes():
#     databoxes.firstname()
#     databoxes.aka1last()
#     databoxes.aka1first()
#     databoxes.aka2lastt()
#     databoxes.aka2first()
#     databoxes.aka3last()
#     databoxes.aka3first()
#     databoxes.DOB()

class tests():
    class clicktests():
        class editclick():
            def pywinEDITBUTTONclicktest():#success!!
                pyAgui_cmds.pywin_doubleclick_editbutton()
                pyAgui_cmds.pywin_click_editbutton()
            def pywinclicktest(): #failed, gets the mouse to hover over the edit button but doesnt click it
                test_id_open()
                pywinclick_editbutton()
                # get_editpage()
                # click_editbutton()
                # lastnamebox()
                # print(lastname)
                # print(test_databoxes())
            def defaulclickttest():
                test_id_open()
                # pywinclick_editbutton()
                click_editbutton()
                lastnamebox()
                print(lastname)
                print(test_databoxes())
        # class primNameclick():
        #     def main():
        #         Fstbox =[254,295]
        #         pyAgui_cmds.pywinMouseMove(Fstbox[0],Fstbox[1])
        #         time.sleep(.1)
        #         pyAgui_cmds.pywinTripleClick(Fstbox[0],Fstbox[1])
        #         time.sleep(.1)
        # class clickandcopy(x,y): #duplicate of primNameclick with some stuff added
        #     def main(x):
        #         Fstbox =[x,y]
        #         pyAgui_cmds.pywinMouseMove(x,y)
        #         time.sleep(.1)
        #         pyAgui_cmds.pywinTripleClick(Fstbox[0],Fstbox[1])
        #         time.sleep(.1)
        #     def copystuff():
        #         sel_all()
        #         copy()
        #         get_clipboard()
        #     main(x,y)
        #     copystuff()
        class clickandcopyall():
            def main():
                def copystuff():
                    time.sleep(.1)
                    pyautogui.click()
                    sel_all()
                    copy()
                    get_clipboard()
                    return
                for coords in coords_list:
                    # pyAgui_cmds.pywinMouseMove(coords[0], coords[1])
                    # pyAgui_cmds.pywinclick(coords[0], coords[1])
                    pyautogui.doubleClick(coords[0], coords[1],interval=.005)
                    copystuff()
                return
    # def mainGUImousetest():
    #     test_id_open()
    #     # pywinclick_editbutton()
    #     get_editpage()
    #     # click_editbutton()
    #     lastnamebox()
    #     print(lastname)
    #     print(test_databoxes())
def runtestsAndOtherStuff():
    test_id_open()
    time.sleep(.1)
    DbclickEditButton = tests.clicktests.editclick.pywinEDITBUTTONclicktest()
    # pyautogui.hotkey('ctrl','+',interval=.1)
    # clickFirstNameBox = tests.clicktests.primNameclick.main()
    # for coords in coords_list:
    #     tests.clicktests.clickandcopy(coords[0], coords[1])
    tests.clicktests.clickandcopyall.main()

runtestsAndOtherStuff()
