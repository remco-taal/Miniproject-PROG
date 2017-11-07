from tkinter import *
import os, xmltodict, requests

def request():
    'Stuurt een request naar de server van NS en returnt een XML'
    global station
    station = invoerVeld.get()
    auth_details = ('remcotaal@hotmail.com', 'Euclf-6uz8iWdUOl7LpERmknqv4u5IEY1Wr3hC2pkK3rJQnum3aNLg')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station
    response = requests.get(api_url, auth=auth_details)
    return response.text

def start():
    dictionary = xmltodict.parse(request())
    global textVeld
    if 'error' not in dictionary:  # De XML bevat een dictionary error wanneer een verkeerde waarde wordt ingevuld
        index = 0
        textVeld.delete(0, END)
        for tijd in dictionary['ActueleVertrekTijden']['VertrekkendeTrein']:
            vertrekTijd = tijd['VertrekTijd']
            vertrekTijd = vertrekTijd[11:19]
            treinSoort = tijd['TreinSoort']
            eindbestemming = tijd['EindBestemming']
            textVeld.insert(index, 'Het begin station is: {} de treinsoort is {:9} {} uur De eindbestemming is: {}'.format(station, treinSoort, vertrekTijd, eindbestemming))
            index += 1
    else:
        textVeld.delete(0, END)                             #
        foutcode = dictionary['error']['message']
        textVeld.insert(0, foutcode)
        request()




def hoofdframe():
    pass

def knop1():
    global root
    root.destroy()
    os.system('gui.py')

def knop2():
    textVeld.delete(0, END)

def knop3():
    start()


def nl_to_eng(): #Wanneer er op de Engelse vlag wordt gedrukt veranderd de Nederlandstalige tekst naar het Engels
    button1['text'] = 'Go back'
    button2['text'] = 'Delete content'
    welkomlabel['text'] = 'Current travel information Utrecht'
    photo['file'] = 'afbeeldingen\kaartlezerengels.PNG'

def eng_to_nl(): #Wanneer er op de Nederlandse vlag wordt gedrukt veranderd de Engelstalige tekst naar het Nederlands
    button1['text'] = 'Ga terug'
    button2['text'] = 'Wis inhoud'
    welkomlabel['text'] = 'Actuele reisinformatie Utrecht'
    photo['file'] = 'afbeeldingen\kaartlezer.PNG'


root = Tk()                                 # Maakt het venster
invoerVeld = StringVar()
root.attributes('-fullscreen',True)         #Start fullscreen op

hoofdframe = Frame(master=root,             #Venster gele gedeelte
                   background='#FFD720',
                   width=1920,
                   height=980)

hoofdframe.pack(side='top', fill=X)

resultaatframe = Frame(master=hoofdframe,             #Venster gele gedeelte
                   background='#FFD720',
                   width=900,
                   height=980)

resultaatframe.pack(side='right', fill='both')


onderframe = Frame(master=root,             #Venster blauwe gedeelte
                   background='#001F6A',
                   width=1920,
                   height=100)
onderframe.pack(side='bottom', fill=X)


welkomlabel = Label(master=hoofdframe,                        #Welkom bij NS tekst
                    text='Actuele reisinformatie Utrecht',
                    foreground='#001F6A',
                    background='#FFD720',
                    font=('Helvetica', 30, 'bold'),
                    width=30,
                    height=3)
welkomlabel.place(x=160, y=50)



button1 = Button(master=hoofdframe,                                 #Knop 1
                 text="Ga terug",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop1)
button1.place(x=330, y=500)

button2 = Button(master=hoofdframe,                                 #Knop 2
                 text="Wis inhoud",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop2)
button2.place(x=530, y=500)

button3 = Button(master=hoofdframe,                                 #Knop 2
                 text="Zoeken",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop3)
button3.place(x=530, y=500)



textVeld = Listbox(master=resultaatframe,
                   height=51,
                   width=205,
                   bd=10,
                   font=('arial', 11, 'bold'),
                   background="#FFD720",
                   foreground="#001F6A")

textVeld.place(x=0, y=0)

mEntry = Entry(master=hoofdframe,
               textvariable=invoerVeld,
               width=15,
               font=('arial', 50))

mEntry.place(x=100, y=200)




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