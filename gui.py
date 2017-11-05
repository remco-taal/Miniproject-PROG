from tkinter import *
from PIL import Image, ImageTk

def hoofdframe():
    pass

def knop1():
    pass

def knop2():
    pass

def knop3():
    pass

def knop4():
    pass

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
                 text="Ik wil naar\n  Amsterdam",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop1)
button1.place(x=380, y=500)

button2 = Button(master=hoofdframe,                                 #Knop 2
                 text="Kopen\nlos kaartje",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop2)
button2.place(x=580, y=500)

button3 = Button(master=hoofdframe,                                 #Knop 3
                 text="Kopen\nOV-Chipkaart",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop3)
button3.place(x=780, y=500)

button4 = Button(master=hoofdframe,                                 #Knop 4
                 text="Ik wil naar\nHet buitenland",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop4)
button4.place(x=980, y=500)



root.mainloop()
