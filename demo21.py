from tkinter import *
def dosomething():
    count.set(count.get()+1)
root = Tk()
root.geometry("200x200")
count=IntVar()
l1=Label(root, textvariable=count)
b1=Button(root, text="Click Me", command=dosomething)
b1.pack()
l1.pack()
root.mainloop()