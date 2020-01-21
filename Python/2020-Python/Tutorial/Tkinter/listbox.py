from tkinter import *
top = Tk()

top.geometry("200x350")
lbl = Label(top,text = "A list of favourite countries...")

listbox = Listbox(top)
listbox.insert(1,"India")
listbox.insert(2,"Russia")
listbox.insert(3,"Israel")
listbox.insert(4,"Japan")

lbl.pack()
listbox.pack()

top.mainloop()