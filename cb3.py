from tkinter import *
def changecolor():
    root.configure(bg=x.get())
root = Tk()
root.geometry("200x200")
oc = root["bg"]
x = StringVar()
cb = Checkbutton(root, text="Red", command=changecolor, variable=x, onvalue="red", offvalue=oc)
cb.deselect()
cb.pack()
root.mainloop()