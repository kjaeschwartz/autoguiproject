# from tkinter import *
#
# ws = Tk()
# text_area = Text(ws, height=100, width=30).pack()
# ws.title("id entry widget")
# ws.geometry('400x300')
# ws['bg'] = '#000000'
#
# IDconst = []
#
# def printValue():
#     IDsEntered = idListentry.get("1.0","end-1c")
#     Label(ws, text=f'IDs, Registered!', pady=20, bg='#ffbf00').pack()
#     print(IDsEntered)
#     IDconst.append(IDsEntered)
#
# def retrieve_input():
#     inputValue=idListentry.get("1.0","end-1c")
#     print(inputValue)
#     IDconst.append(inputvalue)
#
# idListentry = Text(ws, height=10, width=30,pady = 10).pack()
# # idListentry.pack(pady=30)
#
# buttonCommit=Button(ws, height=1, width=10, text="Commit",
#                     command=lambda: retrieve_input())
# buttonCommit.pack()
# # Button(
# #     ws,
# #     text="enter ids",
# #     padx=10,
# #     pady=5,
# #     command=printValue
# #     ).pack()
#
# ws.mainloop()

from tkinter import *
root=Tk()
root.title("id entry widget")
root.geometry('400x300')
root['bg'] = '#000000'
IDconst = []

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)

textBox=Text(root, height=10, width=30,pady = 10)
textBox.pack()
textBox.place(x = 70, y = 10)


buttonCommit=Button(root, height=1, width=10, text="Commit",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()
buttonCommit.place(x = 150,y= 250)

mainloop()
IDsList = IDconst[0].splitlines
print(IDSlist)