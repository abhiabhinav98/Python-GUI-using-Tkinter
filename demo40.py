from tkinter import *
from tkinter import filedialog
def accept():
    file_name = filedialog.askopenfilenames(filetypes=[("mp3 files","*.mp3")],title="Select your favourite song")
    if type(file_name) is tuple:
        str1=""
        for x in file_name:
            str1=str1+x+"\n"
        l1.configure(text=str1)
    if type(file_name) is str:
        l1.configure(text="No file selected.")
root= Tk()
root.geometry("600x600")
btn=Button(root,text="Open File",command=accept)
l1=Label(root)
btn.pack()
l1.pack()
root.mainloop()