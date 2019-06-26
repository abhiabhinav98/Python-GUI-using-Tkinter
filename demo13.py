import tkinter
import tkinter.font
tw=tkinter.Tk()
lbl1=tkinter.Label(tw, text="Red Sun", bg="red", fg="white" )
lbl1.pack(padx=5,pady=5, side=tkinter.LEFT)
lbl2=tkinter.Label(tw, text="Blue Moon", bg="blue", fg="white" )
lbl2.pack(padx=5,pady=5, side=tkinter.RIGHT)
tw.mainloop()