from tkinter import *
def changecolor():
    if x.get()==1:
        root.configure(bg="red")
    else:
        root.configure(bg=oc)
root = Tk()
root.geometry("200x200")
oc = root["bg"]
x = IntVar()
cb = Checkbutton(root, text="Red", command=changecolor, variable=x)
cb.pack()
root.mainloop()