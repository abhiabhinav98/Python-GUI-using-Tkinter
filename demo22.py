from tkinter import *
root = Tk()
def changecolorred():
    l1.config(bg="red")
def changecolorgreen():
    l1.config(bg="green")
def changecolorblue():
    l1.config(bg="blue")
l1=Label(root, height=3,width=20,bg="white")
b1=Button(root,text="Red",width=6, command=changecolorred)
b2=Button(root,text="Green",width=6, command=changecolorgreen)
b3=Button(root,text="Blue",width=6, command=changecolorblue)
l1.grid(row=0,column=1)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
root.mainloop()