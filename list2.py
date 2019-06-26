from tkinter import *
root = Tk()
root.geometry("200x200")
lb1 = Listbox(root)
sports=["Cricket","Football","Hockey","Tennis","Badminton","Swimming","VolleyBall","Rugby","Snooker","Table Tennis"]
for x in sports:
    lb1.insert(END,x)
lb1.grid(row=1,column=0,sticky=W)
root.mainloop()