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

def nl_to_eng(): #Wanneer er op de Engelse vlag wordt gedrukt veranderd de Nederlandstalige tekst naar het Engels
    button1['text'] = 'I want to go\nto Amsterdam'
    button2['text'] = 'Current departure\ntime current station'
    button3['text'] = 'Current departure\ntime other station'
    button4['text'] = 'I want to\ngo abroad'
    welkomlabel['text'] = 'Welcome to NS'

def eng_to_nl(): #Wanneer er op de Nederlandse vlag wordt gedrukt veranderd de Engelstalige tekst naar het Nederlands
    button1['text'] = 'Ik wil naar\nAmsterdam'
    button2['text'] = 'Actuele vertrektijd\nhuidig station'
    button3['text'] = 'Actuele vertrektijd\nander station'
    button4['text'] = 'Ik wil naar\nHet buitenland'
    welkomlabel['text'] = 'Welkom bij NS'


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


photo = PhotoImage(file='afbeeldingen\kaartlezer.PNG')               #Foto kaartlezer
fotolabel = Label(master=hoofdframe, image=photo)
fotolabel.place(x=560, y=220)

button1 = Button(master=hoofdframe,                                 #Knop 1
                 text="Ik wil naar\nAmsterdam",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop1)
button1.place(x=380, y=500)

button2 = Button(master=hoofdframe,                                 #Knop 2
                 text="Actuele vertrektijd\nhuidig station",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop2)
button2.place(x=580, y=500)

button3 = Button(master=hoofdframe,                                 #Knop 3
                 text="Actuele vertrektijd\nander station",
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

buttonNL = Button (master=onderframe,                               #Knop van Engels naar Nederlands
                   width=10,
                   height=10,
                   command=eng_to_nl)
photoNL = PhotoImage (file='afbeeldingen\kroodwitblauw.png')
buttonNL.config(image=photoNL,                                      #Het converteren dat de afbeelding een knop wordt
                width=48,
                height=25)
buttonNL.place(x=50, y=25)

labelengels = Label(master=onderframe,                              #Label onder de Engelse vlag
                    text='English',
                    foreground='white',
                    background='#001F6A',
                    font=('arial', 9))
labelengels.place(x=128, y=55)

buttonENG = Button (master=onderframe,                              #Knop van Nederlands naar Engels
                   width=10,
                   height=10,
                    command=nl_to_eng)
photoENG = PhotoImage (file='afbeeldingen\kengenland.png')
buttonENG.config(image=photoENG,                                    #Het converteren dat de afbeelding een knop wordt
                width=48,
                height=25)
buttonENG.place(x=125, y=25)

labelnederlands = Label(master=onderframe,                          #Label onder de Nederlandse vlag
                        text='Nederlands',
                        foreground='white',
                        background='#001F6A',
                        font=('arial', 9))
labelnederlands.place(x=42, y=55)

root.mainloop()
