from tkinter import*
import datetime

root = Tk()
W = Label(root,text="hello world")
mybutton=Button(root,text="exit", command= exit)
d=datetime.datetime(root,"%A")
d.pack()
mybutton.pack()
W.pack()
root.mainloop()