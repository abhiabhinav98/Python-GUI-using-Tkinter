import tkinter
import tkinter.font
tw=tkinter.Tk()
tw.title("My GUI App 2")
img = tkinter.PhotoImage(file="C:/Users/HP/Desktop/images/loginlogo1.png")
tw.iconphoto(tw,img)
sw=tw.winfo_screenwidth()
sh=tw.winfo_screenheight()
xc=sw//4
yc=sh//4
rw=sw//2
rh=sh//2
tw.geometry(f"{rw}x{rh}+{xc}+{yc}")
tw.resizable(False,False)
f=tkinter.font.Font(weight="bold",size=30)
lbl=tkinter.Label(tw,text="Python Rocks")
lbl.pack()
lbl.configure(bg="red",font=f,width=30)
tw.mainloop()