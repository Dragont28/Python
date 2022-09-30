from tkinter import *

r = Tk()
r.title("Primera Interfaz Gráfica")
r.resizable(1,1)
r.iconbitmap("kali.ico")
r.geometry("600x600")
r.config(bg="black")

f2 = Frame()
f2.pack()
f2.config(width=500, height=50)
f2.config(bg="black")
f2.anchor("center")

f = Frame()
f.pack()
f.config(width = 500, height = 500)
f.config(bg="white")
f.anchor("center")

r.mainloop()

