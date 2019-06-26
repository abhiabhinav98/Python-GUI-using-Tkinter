from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


def ask():
    ans = simpledialog.askinteger("Input", "Enter a number", minvalue=1, maxvalue=lb1.size())
    if ans is not None:
        lbl.configure(text="You selected "+lb1.get(ans-1))
    else:
        messagebox.showinfo(" ", "You didn't input any value.")


root = Tk()
root.geometry("400x400")
lb1 = Listbox(root)
b = Button(root, text="Click Me", command=ask)
lbl = Label(root)
sports = ["Cricket", "Football", "Hockey", "Tennis", "Badminton", "Swimming", "VolleyBall", "Rugby", "Snooker", "Table Tennis"]
for x in sports:
    lb1.insert(END, x)
lb1.grid(row=1, column=0, sticky=W)
b.grid(row=2, column=0, sticky=W)
lbl.grid(row=3, column=0, sticky=W)
root.mainloop()
