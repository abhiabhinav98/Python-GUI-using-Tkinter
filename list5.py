from tkinter import *


def ask():
    index_tuple = lb1.curselection()
    if len(index_tuple)!=0:
        str=""
        for x in index_tuple:
            item=lb1.get(x)
            str+=item+"\n"
        lbl.configure(text="You selected :"+ str)
    else:
        lbl.configure(text="No value selected")

root = Tk()
root.geometry("400x400")
lb1 = Listbox(root, selectmode=MULTIPLE)
b = Button(root, text="Show Item", command=ask)
lbl = Label(root)
sports = ["Cricket", "Football", "Hockey", "Tennis", "Badminton", "Swimming", "VolleyBall", "Rugby", "Snooker", "Table Tennis"]
for x in sports:
    lb1.insert(END, x)
lb1.grid(row=1, column=0, sticky=W)
b.grid(row=2, column=0, sticky=W)
lbl.grid(row=3, column=0, sticky=W)
root.mainloop()
