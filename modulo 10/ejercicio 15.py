import tkinter

items = ['bananas', 'naranjas', 'frutillas', 'melocoto', 'durazno']
window = tkinter.Tk()
label = tkinter.Label(window, text="seleccione las frutas más ricas", background="red", fg="white")
label.grid(column=1, row=0)
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=4)
lista_item = tkinter.StringVar( value = items)
listB = tkinter.Listbox(window, height=15, listvariable=lista_item)
listB.grid(column=2,row=1)

window.mainloop()
