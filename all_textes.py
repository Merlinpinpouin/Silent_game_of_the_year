#NOM
import sqlite3
import random
import csv

last_biome = None
last_weapon = None
last_food = None
last_animal = None

#BIOMES
def select_random_biome():
    conn = sqlite3.connect('DB\silence.db')
    c = conn.cursor()
    c.execute("SELECT biome_name, biome_id FROM Biomes")
    biomes = c.fetchall()
    conn.close()
    return random.choice(biomes)[0] 

def write_biome_to_csv(biome_name):
    with open('CSV\\biome.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([biome_name])

def read_biome_from_csv():
    with open('CSV\\biome.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            return row[0]


#WEAPONS
def select_random_weapon(biome_id):
    conn = sqlite3.connect('DB\silence.db')
    c = conn.cursor()
    c.execute("SELECT weapon_name FROM Weapons WHERE biome_id=?", (biome_id,))
    weapon = c.fetchall()
    conn.close()
    return random.choice(weapon)[0]

def write_weapon_to_csv(weapon_name):
    with open('CSV\weapon.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([weapon_name])

def read_weapon_from_csv():
    with open('CSV\weapon.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            return row[0]

#text weapon
change_weapons_first="Tu entrevois au sol un éclat brillant, tu te baisses et tu t'aperçois"



#FOOD
def select_random_food(biome_id):
    conn = sqlite3.connect('DB\silence.db')
    c = conn.cursor()
    c.execute("SELECT food_name FROM Foods WHERE biome_id=?", (biome_id,))
    food = c.fetchall()
    conn.close()
    return random.choice(food)[0]

def write_food_to_csv(food_name):
    with open('CSV\Food.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([food_name])

def read_food_from_csv():
    with open('CSV\Food.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            return row[0]

#text animal
change_food_first="Tu entrevois au sol une chose alléchante, tu te baisses et tu t'aperçois"

#ANIMALS
def select_random_animal(biome_id):
    conn = sqlite3.connect('DB\silence.db')
    c = conn.cursor()
    c.execute("SELECT animal_name FROM Animals WHERE biome_id=?", (biome_id,))
    animal = c.fetchall()
    conn.close()
    return random.choice(animal)[0]

def write_animal_to_csv(animal_name):
    with open('CSV\Animal.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([animal_name])

def read_animal_from_csv():
    with open('CSV\Animal.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            return row[0]

#text animal
change_animal_first='Tu vois un mouvement au loin, tu t approche et tu vois'

#beginning
nomduperso=None
with open('CSV\\configuration_actuelle.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            nomduperso=row[0]
conn = sqlite3.connect('DB\silence.db')
c = conn.cursor()
write_biome_to_csv(select_random_biome())
nom='Bonjour cher(e) ' +nomduperso+', tu viens de te reveiller ' + str(read_biome_from_csv()) + '.'
conn.commit()
conn.close()


#boucle pour biome
def boucle():
    t=read_biome_from_csv()
    if t == 'dans un desert':
        biome_id=1
    elif t == 'dans une plaine':
        biome_id=2
    elif t == 'dans une toundra':
        biome_id=3
    elif t == 'dans une foret':
        biome_id=4
    elif t == 'dans une foret de cerisier':
        biome_id=5
    elif t == 'sur une plage':
        biome_id=6
    elif t == 'dans une montagne':
        biome_id=7
    return biome_id

biome_id=boucle()

#fonction pour non-repetition
def select_unique_event(select_function, last_event):
    new_event = select_function()
    while new_event == last_event:
        new_event = select_function()
    return new_event

def rien_a_faire():
    rand=random.randint(1,3)
    if rand==1:
        nothing1="Le ciel est dégagé aujourd'hui, tu te poses un moment "
        nothing2="pour réfléchir et tu te sens mieux maintenant."
    elif rand==2:
        nothing1="Le ciel se couvre, tu décides de t'abriter et la pluie qui "
        nothing2="se met à tomber brusquement."
    elif rand==3:
        nothing1="Tu entends le chant d'un oiseau au loin, gazouillant légèrement "
        nothing2="Et tes cheveux balayés par le vent flottent dans l'air sec d'un soir d'été. "
    elif rand==4:
        nothing1="C'est le soir, les criquets chantent et la lune te sourit, tu t'endors "
        nothing2="Calmement, et à ton réveil, tu te sens reposé."
    return nothing1, nothing2

def change():
    global last_biome
    conn = sqlite3.connect('DB/silence.db')
    c = conn.cursor()
    new_biome = select_unique_event(select_random_biome, last_biome)
    write_biome_to_csv(new_biome)
    last_biome = new_biome
    conn.commit()
    conn.close()
    changement_de_biome = 'Tu viens de changer de biome, tu es maintenant ' + str(read_biome_from_csv()) + '.'
    return changement_de_biome

def weapons():
    global last_weapon
    biome_id = boucle()
    conn = sqlite3.connect('DB/silence.db')
    c = conn.cursor()
    new_weapon = select_unique_event(lambda: select_random_weapon(biome_id), last_weapon)
    write_weapon_to_csv(new_weapon)
    last_weapon = new_weapon
    conn.commit()
    conn.close()
    changement_de_weapon = " que c'est " + str(read_weapon_from_csv()) + '.'
    return changement_de_weapon

def food():
    global last_food
    biome_id = boucle()
    conn = sqlite3.connect('DB/silence.db')
    c = conn.cursor()
    new_food = select_unique_event(lambda: select_random_food(biome_id), last_food)
    write_food_to_csv(new_food)
    last_food = new_food
    conn.commit()
    conn.close()
    changement_de_food = " que c'est " + str(read_food_from_csv()) + '.'
    return changement_de_food

def animal():
    global last_animal
    biome_id = boucle()
    conn = sqlite3.connect('DB/silence.db')
    c = conn.cursor()
    new_animal = select_unique_event(lambda: select_random_animal(biome_id), last_animal)
    write_animal_to_csv(new_animal)
    last_animal = new_animal
    conn.commit()
    conn.close()
    changement_de_animal = " que c'est " + str(read_animal_from_csv()) + '.'
    return changement_de_animal