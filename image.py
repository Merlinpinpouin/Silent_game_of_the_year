import all_textes as c
import csv
import os

blanc="image\\blanc.png"
a=None
with open('CSV\\configuration_actuelle.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            a=row[0]

def image_inventaire_1(): 
    csv_file = f'CSV/Perso_csv/{a}.csv'
    if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
        return blanc

    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        row = next(reader, None)  # Lire la première ligne
        if get_image_path(row[0])==None:
            return blanc

    item = row[0]  # Première colonne de la première ligne
    image_path = get_image_path(item)
    return image_path

def image_inventaire_2():
    csv_file = f'CSV/Perso_csv/{a}.csv'
    if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
        return blanc

    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        row = next(reader, None)  # Lire la première ligne
        if get_image_path(row[1])==None:
            return blanc

    item = row[1]  # Deuxième colonne de la première ligne
    image_path = get_image_path(item)
    return image_path

def mettre_dans_inventaire1(inve1):
    with open(f'CSV/Perso_csv/{a}.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        row = next(reader, None)
    with open(f'CSV/Perso_csv/{a}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([inve1, row[1]])

def mettre_dans_inventaire2(inve2):
    with open(f'CSV/Perso_csv/{a}.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        row = next(reader, None)
    with open(f'CSV/Perso_csv/{a}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([row[0], inve2])

biomes = {
        "dans un desert": "image\\biomes\\desert.png",
        "dans une plaine": "image\\biomes\\plaine.png",
        "dans une toundra": "image\\biomes\\toundra.png",
        "dans une foret": "image\\biomes\\foret.png",
        "dans une foret de cerisier": "image\\biomes\\cerisier.png",
        "sur une plage": "image\\biomes\\plage.png",
        "dans une montagne": "image\\biomes\\montagne.png"
    }

def image_biome():
    im = c.read_biome_from_csv()
    return biomes.get(im)

weapons = {
        "un sabre oriental": "image\\weapons\\sabre_oriental.png",
        "une arbalète": "image\\weapons\\arbalete.png",
        "un miroir": "image\\weapons\\miroir.png",
        "un cimeterre": "image\\weapons\\cimeterre.png",
        "une lance": "image\\weapons\\lance.png",
        "un lance-pierre": "image\\weapons\\lance_pierre.png",
        "une fronde": "image\\weapons\\fronde.png",
        "une épée": "image\\weapons\\epe.png",
        "une boule de neige": "image\\weapons\\boule_de_neige.png",
        "une épée de glace": "image\\weapons\\epe_de_glace.png",
        "un arc": "image\\weapons\\arc.png",
        "un gourdin": "image\\weapons\\gourdin.png",
        "un harpon": "image\\weapons\\harpon.png",
        "une corde": "image\\weapons\\corde.png",
        "un piège à loup": "image\\weapons\\piege_a_loup.png",
        "un katana": "image\\weapons\\katana.png",
        "un nunchaku": "image\\weapons\\nunchaku.png",
        "une orbe de qi": "image\\weapons\\orbe_de_qi.png",
        "un éventail": "image\\weapons\\eventail.png",
        "un parasol": "image\\weapons\\parasol.png",
        "un pistolet à eau": "image\\weapons\\pistolet_a_eau.png",
        "une dent de requin": "image\\weapons\\dent_de_requin.png",
        "une hallebarde": "image\\weapons\\hallebarde.png",
        "un sifflet": "image\\weapons\\sifflet.png",
        "une pioche": "image\\weapons\\pioche.png",
        "un silex": "image\\weapons\\silex.png"
    }

def image_weapons():
    im = c.read_weapon_from_csv()
    return weapons.get(im)

animals = {
        "un serpent": "image\\animals\\serpent.png",
        "un scorpion": "image\\animals\\scorpion.png",
        "un cheval": "image\\animals\\cheval.png",
        "un lièvre": "image\\animals\\lievre.png",
        "un ours polaire": "image\\animals\\ours_polaire.png",
        "un yak": "image\\animals\\yak.png",
        "un poisson": "image\\animals\\poisson.png",
        "un sanglier": "image\\animals\\sanglier.png",
        "un panda": "image\\animals\\panda.png",
        "un papillon": "image\\animals\\papillon.png",
        "un crabe": "image\\animals\\crabe.png",
        "une tortue": "image\\animals\\tortue.png",
        "une marmotte": "image\\animals\\marmotte.png",
        "un bouc": "image\\animals\\bouc.png"
    }

def image_animals():
    im = c.read_animal_from_csv()
    return animals.get(im)

foods = {
        "de la figue de Barbarie": "image\\foods\\Barbarie.png",
        "une Moussaka": "image\\foods\\Moussaka.png",
        "un tajine": "image\\foods\\tajine.png",
        "un couscous": "image\\foods\\couscous.png",
        "un thé à la menthe": "image\\foods\\the_a__la_menthe.png",
        "du pain": "image\\foods\\pain.png",
        "une pizza": "image\\foods\\pizza.png",
        "un pavé de boeuf": "image\\foods\\pave_de_boeuf.png",
        "une omelette": "image\\foods\\omelette.png",
        "une ratatouille": "image\\foods\\ratatouille.png",
        "une raclette": "image\\foods\\raclette.png",
        "une fondue": "image\\foods\\fondue.png",
        "de la viande de Renne": "image\\foods\\la_viande_de_Renne.png",
        "du poisson séché": "image\\foods\\poisson_seche.png",
        "une soupe": "image\\foods\\soupe.png",
        "une pomme de pin": "image\\foods\\pomme_de_pin.png",
        "une framboise": "image\\foods\\framboise.png",
        "des champignons": "image\\foods\\champignons.png",
        "des carottes sauvages": "image\\foods\\dcarottes_sauvages.png",
        "un lapin": "image\\foods\\lapin.png",
        "des pétales de cerisier": "image\\foods\\petales_de_cerisier.png",
        "un ramen": "image\\foods\\ramen.png",
        "du saké": "image\\foods\\sake.png",
        "des nouilles instantanées": "image\\foods\\nouilles_instantanees.png",
        "des sushi": "image\\foods\\sushi.png",
        "du crabe": "image\\foods\\crabe.png",
        "des moules": "image\\foods\\moules.png",
        "des algues": "image\\foods\\algues.png",
        "du poisson": "image\\foods\\poisson.png",
        "des coquillages": "image\\foods\\coquillages.png",
        "des myrtilles": "image\\foods\\myrtilles.png",
        "du chevreuille": "image\\foods\\chevreuille.png",
        "une chèvre": "image\\foods\\chevre.png",
        "du chocolat chaud": "image\\foods\\chocolat_chaud.png",
        "de l aligot": "image\\foods\\aligot.png"
    }

def image_foods():
    im = c.read_food_from_csv()
    return foods.get(im)

def get_image_path(item):
    # Combiner tous les dictionnaires en un seul
    all_items = {**biomes, **weapons, **animals, **foods}
    return all_items.get(item)