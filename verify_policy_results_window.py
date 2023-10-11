import time
from tkinter import *
import ttkbootstrap as tb

def openNewWindow(root,errmessage):
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Policy results")
    newWindow.iconbitmap("./A&GICON.ico")
    newWindow.geometry('600x400')

    # sets the geometry of toplevel
    h = Scrollbar(newWindow, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)

    v = Scrollbar(newWindow, orient='vertical')
    v.pack(side=RIGHT, fill=Y)

    # A Label widget to show in toplevel

    t = Text(newWindow, height=600,  wrap=NONE, fg="red",
             foreground="red",
             xscrollcommand=h.set,
             yscrollcommand=v.set)
    t.pack(fill="both", expand=True,)
    #Passed in the reuslts {errmessage}
    t.insert(END, f"{errmessage}")
    # t.tag_add("start", "1.6", "1.12")
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)
