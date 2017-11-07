from tkinter import *
import requests, xmltodict


root = Tk()
s = StringVar()
root.geometry('1450x1450+500+300')

def request():
    'Stuurt een request naar de server van NS en returnt een XML'
    global station
    station = s.get()
    auth_details = ('remcotaal@hotmail.com', 'Euclf-6uz8iWdUOl7LpERmknqv4u5IEY1Wr3hC2pkK3rJQnum3aNLg')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station
    response = requests.get(api_url, auth=auth_details)
    label1 = Label(root, text=response.text).place(x=150, y=100)
    dictionary = xmltodict.parse(response.text)



    if 'error' not in dictionary:  # De XML bevat een dictionary error wanneer een verkeerde waarde wordt ingevuld
        for tijd in dictionary['ActueleVertrekTijden']['VertrekkendeTrein']:
            vertrekTijd = tijd['VertrekTijd']
            vertrekTijd = vertrekTijd[11:19]
            treinSoort = tijd['TreinSoort']
            eindbestemming = tijd['EindBestemming']
            label1 = Label(root,text='Het begin station is: {} {:9} {} uur De eindbestemming is: {}'.format(station.capitalize(),treinSoort, vertrekTijd,eindbestemming)).place(x=150, y=100)
    else:
        label1 = Label(root,text='error').place(x=150, y=100)
        request()



def hi():
    text1 = s.get()
    label1 = Label(root,text = text1).place(x = 150, y = 100)



button1 = Button(root, text="Ik wil naar\n  Amsterdam       ",fg="white", bg="blue",command = request)
button2 = Button(root, text="   Kopen   \n      los kaartje      ",fg="white", bg="blue")
button3 = Button(root, text="   Kopen   \n OV-Chipkaart     ",fg="white", bg="blue")
button4 = Button(root, text="Ik wil naar\nHet buitenland    ",fg="white", bg="blue")

mEntry = Entry(root,textvariable=s).place(x = 50,y=50)
button1.place(x = 50, y = 100)
button2.place(x = 50, y = 150)
button3.place(x = 50, y = 200)
button4.place(x = 50, y = 250)

root.mainloop()