import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('DB\silence.db')
c = conn.cursor()

# Création de la table des biomes
c.execute('''CREATE TABLE Biomes (
    biome_id INTEGER PRIMARY KEY,
    biome_name TEXT UNIQUE
)''')

# Insertion des données dans la table des biomes
biomes_data = [
    ('dans un desert',),
    ('dans une plaine',),
    ('dans une toundra',),
    ('dans une foret',),
    ('dans une foret de cerisier',),
    ('sur une plage',),
    ('dans une montagne',)
]
c.executemany('INSERT INTO Biomes (biome_name) VALUES (?)', biomes_data)

# Création de la table des aliments
c.execute('''CREATE TABLE Foods (
    food_id INTEGER PRIMARY KEY,
    food_name TEXT UNIQUE,
    biome_id INTEGER REFERENCES Biomes(biome_id)
)''')

# Insertion des données dans la table des aliments
foods_data = [
    ('de la figue de Barbarie', 1),
    ('une Moussaka', 1),
    ('un tajine', 1),
    ('un couscous', 1),
    ('un thé à la menthe', 1),
    ('du pain', 2),
    ('une pizza', 2),
    ('un pavé de boeuf', 2),
    ('une omelette', 2),
    ('une ratatouille', 2),
    ('une raclette', 3),
    ('une fondue', 3),
    ('de la viande de Renne', 3),
    ('du poisson séché', 3),
    ('une soupe', 3),
    ('une pomme de pin', 4),
    ('une framboise', 4),
    ('des champignons', 4),
    ('des carottes sauvages', 4),
    ('un lapin', 4),
    ('des pétales de cerisier', 5),
    ('un ramen', 5),
    ('du saké', 5),
    ('des nouilles instantanées', 5),
    ('des sushi', 5),
    ('du crabe', 6),
    ('des moules', 6),
    ('des algues', 6),
    ('du poisson', 6),
    ('des coquillages', 6),
    ('des myrtilles', 7),
    ('du chevreuille', 7),
    ('une chèvre', 7),
    ('du chocolat chaud', 7),
    ('de l aligot', 7)
]
c.executemany('INSERT INTO Foods (food_name, biome_id) VALUES (?, ?)', foods_data)

# Création de la table des animaux
c.execute('''CREATE TABLE Animals (
    animal_id INTEGER PRIMARY KEY,
    animal_name TEXT UNIQUE,
    biome_id INTEGER REFERENCES Biomes(biome_id)
)''')

# Insertion des données dans la table des animaux
animals_data = [
    ('un serpent', 1),
    ('un scorpion', 1),
    ('un cheval', 2),
    ('un lièvre', 2),
    ('un ours polaire', 3),
    ('un yak', 3),
    ('un poisson', 4),
    ('un sanglier', 4),
    ('un panda', 5),
    ('un papillon', 5),
    ('un crabe', 6),
    ('une tortue', 6),
    ('une marmotte', 7),
    ('un bouc', 7)
]
c.executemany('INSERT INTO Animals (animal_name, biome_id) VALUES (?, ?)', animals_data)

# Création de la table des armes
c.execute('''CREATE TABLE Weapons (
    weapon_id INTEGER PRIMARY KEY,
    weapon_name TEXT,
    biome_id INTEGER REFERENCES Biomes(biome_id)
)''')

# Insertion des données dans la table des armes
weapons_data = [
    ('un sabre oriental', 1),
    ('une arbalète', 1),
    ('un miroir', 1),
    ('un cimeterre', 1),
    ('une lance', 2),
    ('un lance-pierre', 2),
    ('une fronde', 2),
    ('une épée', 2),
    ('une boule de neige', 3),
    ('une épée de glace', 3),
    ('un arc', 3),
    ('un gourdin', 3),
    ('une arbalète', 4),
    ('un harpon', 4),
    ('une corde', 4),
    ('un piège à loup', 4),
    ('un katana', 5),
    ('un nunchaku', 5),
    ('une orbe de qi', 5),
    ('un éventail', 5),
    ('un parasol', 6),
    ('un pistolet à eau', 6),
    ('une dent de requin', 6),
    ('une hallebarde', 7),
    ('un sifflet', 7),
    ('une pioche', 7),
    ('un silex', 7)
]
c.executemany('INSERT INTO Weapons (weapon_name, biome_id) VALUES (?, ?)', weapons_data)


conn.commit()
conn.close()