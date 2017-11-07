from tkinter import *
import os, xmltodict, requests

def request():
    'Stuurt een request naar de server van NS en returnt een XML'
    auth_details = ('remcotaal@hotmail.com', 'Euclf-6uz8iWdUOl7LpERmknqv4u5IEY1Wr3hC2pkK3rJQnum3aNLg')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=Utrecht'
    response = requests.get(api_url, auth=auth_details)
    return response.text

def start():
    dictionary = xmltodict.parse(request())

    if 'error' not in dictionary:  # De XML bevat een dictionary error wanneer een verkeerde waarde wordt ingevuld
        index = 0
        spacing = 20
        global textVeld
        for tijd in dictionary['ActueleVertrekTijden']['VertrekkendeTrein']:
            vertrekTijd = tijd['VertrekTijd']
            vertrekTijd = vertrekTijd[11:19]
            treinSoort = tijd['TreinSoort']
            eindbestemming = tijd['EindBestemming']
            textVeld.insert(index, 'Het begin station is: Utrecht de treinsoort is {:9} {} uur De eindbestemming is: {}'.format(treinSoort, vertrekTijd, eindbestemming))
            index += 1
    else:
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


root = Tk()                                 # Maakt het venster
root.attributes('-fullscreen',True)         #Start fullscreen op

hoofdframe = Frame(master=root,             #Venster gele gedeelte
                   background='#FFD720',
                   width=1920,
                   height=980)

hoofdframe.pack(side='top', fill=X)

resultaatframe = Frame(master=hoofdframe,             #Venster gele gedeelte
                   background='#FFD720',
                   width=650,
                   height=980)

resultaatframe.pack(side='right', fill='both')


onderframe = Frame(master=root,             #Venster blauwe gedeelte
                   background='#001F6A',
                   width=1920,
                   height=100)
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
                 text="Ga terug",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop1)
button1.place(x=580, y=500)

button2 = Button(master=hoofdframe,                                 #Knop 2
                 text="Get cancer",
                 foreground="white",
                 background="#001F6A",
                 font=('arial', 12, 'bold'),
                 width=17,
                 height=3,
                 command=knop2)
button2.place(x=780, y=500)


textVeld = Listbox(master=resultaatframe,
                   height=60,
                   width=105,
                   bd=10)

textVeld.place(x=0, y=0)




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


start()

root.mainloop()
