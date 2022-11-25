import tkinter
from tkinter import ttk

def reset(event):
    s1.set('')
    s2.set('')
    s3.set('')
    s4.set('')
window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=4)
s1 = tkinter.StringVar()
s2 = tkinter.StringVar()
s3 = tkinter.StringVar()
s4 = tkinter.StringVar()

selec1 = ttk.Radiobutton(window, text="no estoy deacuerdo", value='1', variable=s1)
selec2 = ttk.Radiobutton(window, text="estoy deacuerdo", value='1', variable=s2)
selec3 = ttk.Radiobutton(window, text="deacuerdo", value='1', variable=s3)
selec4 = ttk.Radiobutton(window, text="no ", value='1', variable=s4)
selec1.grid(column=1, row=0, padx=5, pady=5)
selec2.grid(column=1, row=1, padx=5, pady=5)
selec3.grid(column=1, row=2, padx=5, pady=5)
selec4.grid(column=1, row=3, padx=5, pady=5)
resB= ttk.Button(window, text='Reset')
resB.grid(column=0, row=0)
resB.bind('<Button-1>', reset)

window.mainloop()
