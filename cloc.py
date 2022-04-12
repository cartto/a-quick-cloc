# cat
from tkinter import *
from threading import *
from datetime import *

t = Tk()
t.title("time")
t.geometry("300x300")
t["bg"] = "black"


new = datetime.now()
first_time = new.strftime("%I")
second_time = new.strftime("%M")
am_pm = new.strftime("%p")
subbed_ftime = first_time[1:2]

Label(t,bg = "black").pack()
Label(t,bg = "black").pack()

timelabel = Label(t, font = ("Ariel", 50),bg = "black", text = subbed_ftime + ":" + second_time + " " + am_pm, fg = "white")
timelabel.pack()

def updatetime():
    t.after(1, updatetime)
    new = datetime.now()
    first_time = new.strftime("%I")
    second_time = new.strftime("%M")
    am_pm = new.strftime("%p")
    subbed_ftime = first_time[1:2]
    timelabel["text"] = (subbed_ftime + ":" + second_time + " " + am_pm)
    # timelabel["fg"] = "red"
updatetime()
t.mainloop()
