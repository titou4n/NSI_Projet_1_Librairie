import sqlite3

livres_datas = [
    (1, 1, 1, '1984', 1949, 10, 100.00, 50),
    (2, 2, 1, 'Dune', 1965, 8, 85.00, 30),
    (3, 3, 1, 'Fondation', 1951, 9, 92.50, 40),
    (4, 4, 1, 'Le meilleur des mondes', 1931, 7, 75.00, 20),
    (5, 5, 1, 'Fahrenheit 451', 1953, 7, 78.50, 35),
    (6, 6, 1, 'Ubik', 1969, 9, 88.00, 45),
    (7, 7, 1, 'Chroniques martiennes', 1950, 8, 82.00, 25),
    (8, 8, 1, 'La nuit des temps', 1968, 7, 70.00, 15),
    (9, 9, 1, 'Blade Runner', 1968, 8, 87.50, 30),
    (10, 10, 1, 'Les Robots', 1950, 9, 94.00, 40),
    (11, 11, 1, 'La Planète des singes', 1963, 8, 80.00, 25),
    (12, 8, 1, 'Ravage', 1943, 8, 79.00, 20),
    (13, 6, 1, 'Le Maître du Haut Château', 1962, 8, 86.50, 35),
    (14, 12, 1, 'Le monde des Ā', 1945, 7, 72.50, 15),
    (15, 3, 1, 'La Fin de l’éternité', 1955, 8, 89.00, 30),
    (16, 13, 1, 'De la Terre à la Lune', 1865, 10, 98.00, 55)
]
auteurs_datas = [
    (1, 'George', 'ORWELL'),
    (2, 'Frank', 'HERBERT'),
    (3, 'Isaac', 'ASIMOV'),
    (4, 'Aldous', 'HUXLEY'),
    (5, 'Ray', 'BRADBURY'),
    (6, 'Philip', 'K.DICK'),
    (7, 'René', 'BARJAVEL'),
    (8, 'Pierre', 'BOULLE'),
    (9, 'A.E.', 'VAN VOGT'),
    (10, 'Jules', 'VERNE')
]
ecrire_datas = [
    (1, 1),  # George Orwell pour "1984"
    (2, 2),  # Frank Herbert pour "Dune"
    (3, 3),  # Isaac Asimov pour "Fondation"
    (4, 4),  # Aldous Huxley pour "Le meilleur des mondes"
    (5, 5),  # Ray Bradbury pour "Fahrenheit 451"
    (6, 6),  # Philip K. Dick pour "Ubik"
    (7, 5),  # Ray Bradbury pour "Chroniques martiennes"
    (8, 7),  # René Barjavel pour "La nuit des temps"
    (9, 6),  # Philip K. Dick pour "Blade Runner"
    (10, 3),  # Isaac Asimov pour "Les Robots"
    (11, 8),  # Pierre Boulle pour "La Planète des singes"
    (12, 7),  # René Barjavel pour "Ravage"
    (13, 6),  # Philip K. Dick pour "Le Maître du Haut Château"
    (14, 9),  # A.E. Van Vogt pour "Le monde des Ā"
    (15, 3),  # Isaac Asimov pour "La Fin de l’éternité"
    (16, 10)  # Jules Verne pour "De la Terre à la Lune"
]
editeurs_datas = [
    (1, 'Penguin Books'),
    (2, 'Ace Books'),
    (3, 'Gnome Press'),
    (4, 'Chatto & Windus'),
    (5, 'Ballantine Books'),
    (6, 'Doubleday'),
    (7, 'Bantam Books'),
    (8, 'French & European Publications'),
    (9, 'Methuen Publishing'),
    (10, 'Signet Books'),
    (11, 'Julliard'),
    (12, 'Denoël'),
    (13, 'Sudel'),
    (14, 'Hayakawa Shobō'),
    (15, 'Brick Tower Press'),
    (16, 'Hetzel')
]
genre_datas = [
    (1, 'Science-Fiction')
]

def initialisation_db():
    # Créer une connexion à la base de données (ou la créera si elle n'existe pas)
    conn = sqlite3.connect('Data\database_library.db')
    # Créer un curseur pour exécuter des commandes SQL
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS livres;""")
    cursor.execute("""DROP TABLE IF EXISTS auteurs;""")
    cursor.execute("""DROP TABLE IF EXISTS editeurs;""")
    cursor.execute("""DROP TABLE IF EXISTS ecrire;""")
    cursor.execute("""DROP TABLE IF EXISTS commandes;""")
    cursor.execute("""DROP TABLE IF EXISTS detail_commandes;""")
    cursor.execute("""DROP TABLE IF EXISTS clients;""")
    cursor.execute("""DROP TABLE IF EXISTS genre;""")
    print("Les tables de l'ancienne base de données ont été supprimé avec succés.")
    # Création des tables pour stocker des informations sur les livres
    cursor.execute("""
    CREATE TABLE livres (
    id_isbn           INTEGER PRIMARY KEY AUTOINCREMENT
                              NOT NULL,
    id_editeur        INTEGER NOT NULL
                              REFERENCES editeurs (id_editeur),
    id_genre          INTEGER NOT NULL
                              REFERENCES genre (id_genre),
    titre             TEXT    NOT NULL,
    annee_publication INTEGER NOT NULL,
    prix              FLOAT   NOT NULL,
    quantite          INT
    );
    """)
    # Créer une table pour stocker des informations sur les clients
    cursor.execute("""
    CREATE TABLE clients (
    id_client            INTEGER PRIMARY KEY AUTOINCREMENT
                                 NOT NULL,
    nom_client           TEXT    NOT NULL,
    prenom_client        TEXT    NOT NULL,
    total_depense_client DECIMAL DEFAULT (0) 
    );
    """)
    # Créer une table pour stocker des informations sur les commandes
    cursor.execute("""
    CREATE TABLE commandes (
        id_commande   INTEGER PRIMARY KEY AUTOINCREMENT
                            NOT NULL,
        id_client     INTEGER NOT NULL
                            REFERENCES clients (id_client),
        date_commande DATETIME    NOT NULL,
        FOREIGN KEY (
            id_client
        )
        REFERENCES clients (id_client)
    );
    """)
    cursor.execute("""
    CREATE TABLE auteurs (
        id_auteur     INTEGER PRIMARY KEY AUTOINCREMENT
                            NOT NULL,
        nom_auteur    TEXT    NOT NULL,
        prenom_auteur TEXT    NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE ecrire (
        id_isbn   INTEGER REFERENCES livres (id_isbn) 
                        NOT NULL,
        id_auteur INTEGER REFERENCES auteurs (id_auteur) 
                        NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE detail_commandes (
        id_isbn     INTEGER NOT NULL
                            REFERENCES livres (id_isbn),
        id_commande INTEGER NOT NULL
                            REFERENCES commandes (id_commande),
        quantite    INTEGER NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE editeurs (
        id_editeur  INTEGER PRIMARY KEY
                            NOT NULL,
        nom_editeur TEXT    NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE genre (
    id_genre  INTEGER PRIMARY KEY AUTOINCREMENT
                      NOT NULL,
    nom_genre TEXT    NOT NULL
    );
    """)
    # Enregistrer les modifications dans la base de données
    conn.commit()
    # Fermer la connexion à la base de données
    conn.close()
    print("Les nouvelles tables de la base de données de la librairie ont été créée avec succès.")

def ajout_livre(livres_datas):
    conn = sqlite3.connect('Data\database_library.db')
    for livre_data in livres_datas:
        query = """INSERT INTO livres (titre, annee_publication, id_genre, prix, quantite, id_editeur) VALUES (?,?,?,?,?,?);"""
        conn.execute(query,(livre_data[3], livre_data[4], livre_data[2], livre_data[6], livre_data[7], livre_data[1]))
        conn.commit()
    conn.close()

def ajout_auteurs(auteurs_datas):
    conn = sqlite3.connect('Data\database_library.db')
    for auteurs_data in auteurs_datas:
        query = """INSERT INTO auteurs (nom_auteur, prenom_auteur) VALUES (?,?);"""
        conn.execute(query,(auteurs_data[2], auteurs_data[1]))
        conn.commit()
    conn.close()

def ajout_editeurs(editeurs_datas):
    conn = sqlite3.connect('Data\database_library.db')
    for editeurs_data in editeurs_datas:
        query = """INSERT INTO editeurs (nom_editeur) VALUES (?);"""
        conn.execute(query,(editeurs_data[1],))
        conn.commit()
    conn.close()

def ajout_genres(genre_datas):
    conn = sqlite3.connect('Data\database_library.db')
    for genre_data in genre_datas:
        query = """INSERT INTO genre (nom_genre) VALUES (?);"""
        conn.execute(query,(genre_data[1],))
        conn.commit()
    conn.close()

def ajout_ecrire(ecrire_datas):
    conn = sqlite3.connect('Data\database_library.db')
    for ecrire_data in ecrire_datas:
        query = """INSERT INTO ecrire (id_isbn, id_auteur) VALUES (?,?);"""
        conn.execute(query,(ecrire_data[0], ecrire_data[1]))
        conn.commit()
    conn.close()


initialisation_db()
ajout_livre(livres_datas)
ajout_auteurs(auteurs_datas)
ajout_editeurs(editeurs_datas)
ajout_genres(genre_datas)
ajout_ecrire(ecrire_datas)
print("Les ajouts de livres dans la base de données de la librairie ont été réussi avec succès.")
print("Vous pouvez désormais quitter cette page.")