from tkinter import *
from functools import partial
from tkinter import font
import csv
import subprocess

fenetre = Tk()
fenetre.title("Silent")
fenetre.geometry("2000x1200")
fenetre.bind('<Escape>', lambda e: fenetre.destroy())

fond_menu_principale = PhotoImage(file="image/Fond menu principale.png")
label1 = Label(fenetre, image=fond_menu_principale)
label1.place(x=0, y=0)

# Création de 2 colonnes pour l'ihm
fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.rowconfigure(0, weight=1)
fenetre.rowconfigure(1, weight=1)

# TOUTES LES VARIABLES ICI(pas beacoup quand même)
tab = []

def update_label(labelvar, textvar):
    with open('CSV/Tout les perso.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            tab.append(row[0])

    text = textvar.get()
    labelvar.set("Bonjour " + text)

    with open('CSV\\configuration_actuelle.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([text])

    if text not in tab:
        with open('CSV/Perso_csv/' + text + '.csv', 'w') as new_file:
            new_file.write(",")
        with open('CSV/Tout les perso.csv', 'a') as fp:
            fp.write(text + '\n')
        subprocess.run(['python', 'silence_v0_1.py'])
    else:
        subprocess.run(['python', 'silence_v0_1.py'])


Impact = font.Font(family="Impact", size=30, weight="bold")
bjr = StringVar()
bjr.set("Bonjour")
texte1 = Label(fenetre, width=30, height=4, textvariable=bjr, foreground="white", background="blue")
texte1.configure(font=(Impact))
texte1.grid(column=0, row=1)

# Zone de texte pour le pseudo du joueur
text = StringVar(fenetre)
entry_name = Entry(fenetre, width=30, textvariable=text)
entry_name.grid(column=1, row=0)

# Bouton pour valider le pseudo
button = Button(fenetre, width=20, height=5, text='ok', foreground="green", command=partial(update_label, bjr, text))
button.grid(column=1, row=1)

#quitter l'application
def destroy():
    fenetre.destroy()

#Bouton pour quitter l'application
button2 = Button(fenetre, width=10, height=2, text='QUITTER', foreground="red", command=destroy)
button2.grid(column=1, row=2)

fenetre.mainloop()