from tkinter import *


def ask(e):
    item = lb1.curselection()[0]
    lbl.configure(text="You selected "+lb1.get(item))

root = Tk()
root.geometry("400x400")
lb1 = Listbox(root)
lb1.bind("<Double-Button-1>", ask)
lbl = Label(root)
sports = ["Cricket", "Football", "Hockey", "Tennis", "Badminton", "Swimming", "VolleyBall", "Rugby", "Snooker", "Table Tennis"]
for x in sports:
    lb1.insert(END, x)
lb1.grid(row=1, column=0, sticky=W)
lbl.grid(row=3, column=0, sticky=W)
root.mainloop()
