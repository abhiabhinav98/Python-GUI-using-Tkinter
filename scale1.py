from tkinter import *
def color(str):

    a = int(str)
    clr = hex(a)
    print(clr)
    clr1=clr[2:]
    clr1 = "#"+clr1
    print(clr1)
    root.configure(bg=clr1)
root = Tk()
root.geometry("400x400")
x = IntVar()
s = Scale(root, from_=0 ,to=255 ,variable=x, command = color, orient=HORIZONTAL)
s.pack()
root.configure(bg="#000")
root.mainloop()