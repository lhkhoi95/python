from tkinter import *

def inserT():
    Lb1.insert(END, "Python")
    Lb1.insert(END, "Perl")
    Lb1.insert(END, "C")
    Lb1.insert(END, "PHP")
    Lb1.insert(END,'dsds')

    Lb1.pack()
top = Tk()

Lb1 = Listbox(top)
inserT()
top.mainloop()