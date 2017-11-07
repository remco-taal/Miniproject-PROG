from tkinter import *
import os
#from PIL import Image, ImageTk



def hoofdframe():
    pass


def knop1():
    global root
    root.destroy()
    os.system('Beginscherm.py')


root = Tk() # Maakt het venster

hoofdframe = Frame(master=root,             #Venster gele gedeelte
                   background='#FFD720',
                   width=10000,
                   height=711)
hoofdframe.pack(side='top', fill=X)

onderframe = Frame(master=root,             #Venster blauwe gedeelte
                   background='#001F6A',
                   width=850,
                   height=90)
onderframe.pack(side='bottom', fill=X)


welkomlabel = Label(master=hoofdframe,                        #Welkom bij NS tekst
                    text='Welkom bij NS',
                    foreground='#001F6A',
                    background='#FFD720',
                    font=('Helvetica', 30, 'bold'),
                    width=14,
                    height=3)
welkomlabel.place(x=600, y=50)

photo = PhotoImage(file='kaartlezer.PNG')               #Foto kaartlezer
fotolabel = Label(master=hoofdframe, image=photo)
fotolabel.place(x=560, y=220)

button1 = Button(master=hoofdframe,                                 #Knop 1
                 text="Ga terug naar\n beginscherm",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop1)
button1.place(x=380, y=500)

root.mainloop()
