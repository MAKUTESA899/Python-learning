from tkinter import*
root = Tk()
W = Label(root,text="hello world")
mybutton=Button(root,text="come" command= exit)
mybutton.pack()
W.pack()
root.mainloop()