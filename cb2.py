from tkinter import *
def changecolor():
    print(x.get())
root = Tk()
root.geometry("200x200")
oc = root["bg"]
x = StringVar()
cb = Checkbutton(root, text="Click Me", command=changecolor, variable=x, onvalue = "hi", offvalue="bye")
cb.deselect()
cb.pack()
root.mainloop()