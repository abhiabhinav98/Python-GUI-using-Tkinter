from tkinter import *
root = Tk()
root.geometry("200x200")
lb1 = Listbox(root)
sports=["Cricket","Football","Hockey","Tennis","Badminton","Swimming","VolleyBall","Rugby","Snooker"]
i=0
for x in sports:
    lb1.insert(i,x)
lb1.grid(row=1,column=0,sticky=W)
root.mainloop()