import sqlite3
import datetime

class DatabaseLibrary():
  def connection_db(self):
    conn = sqlite3.connect('Data\database_library.db')
    conn.row_factory = sqlite3.Row
    return conn

  def ajouter_livre_db(self, titre:str, annee_publication:int, id_genre:int, prix:float, quantite:int, id_editeur:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"INSERT INTO livres (titre, annee_publication, id_genre, prix, quantite, id_editeur) VALUES (?,?,?,?,?,?);"
    conn.execute(query, (titre, annee_publication, id_genre, prix, quantite, id_editeur))
    conn.commit()
    conn.close()

  def ajouter_genre_db(self, nom_genre:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"INSERT INTO genre (nom_genre) VALUES (?);"
    conn.execute(query, (nom_genre,))
    conn.commit()
    conn.close()

  def ajouter_auteur_livre_db(self, nom_auteur:str, prenom_auteur:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"INSERT INTO auteurs (nom_auteur, prenom_auteur) VALUES (?,?);"
    conn.execute(query, (nom_auteur, prenom_auteur))
    conn.commit()
    conn.close()

  def ajouter_editeur_livre_db(self, nom_editeur:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"INSERT INTO editeurs (nom_editeur) VALUES (?);"
    conn.execute(query, (nom_editeur,))
    conn.commit()
    conn.close()

  def ajouter_table_ecrire_db(self, id_isbn:int, id_auteur:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"INSERT INTO ecrire (id_isbn, id_auteur) VALUES (?,?);"
    conn.execute(query, (id_isbn, id_auteur))
    conn.commit()
    conn.close()

  def ajouter_client_db(self, nom_client:str, prenom_client:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"INSERT INTO clients (nom_client, prenom_client) VALUES (?,?);"
    conn.execute(query, (nom_client, prenom_client))
    conn.commit()
    conn.close()
    
  def ajouter_details_commandes_db(self, id_isbn:int, id_commande:int, quantite:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"INSERT INTO details_commandes (id_isbn, id_commande, quantite) VALUES (?,?,?);"
    conn.execute(query, (id_isbn, id_commande, quantite))
    conn.commit()
    conn.close()

  def ajouter_commande_db(self, id_client:int, date_commande:datetime):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"INSERT INTO commandes (id_client, date_commande) VALUES (?,?);"
    conn.execute(query, (id_client, date_commande))
    conn.commit()
    conn.close()

  def chercher_depense_client_db(self, id_client:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT total_depense_client FROM clients WHERE id_client=?;"
    result = conn.execute(query, (id_client,))
    result = result.fetchall()
    conn.close()
    if result:
        return result[0][0]
    else:
        return None

  def chercher_id_commande_db(self, id_client:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_commande FROM commandes WHERE id_client=?;"
    result = conn.execute(query, (id_client,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None

  def chercher_id_genre_db(self, nom_genre:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_genre FROM genre WHERE nom_genre=?;"
    result = conn.execute(query, (nom_genre,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None
  
  def chercher_id_auteur_db(self, nom_auteur:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_auteur FROM auteurs WHERE nom_auteur=?;"
    result = conn.execute(query, (nom_auteur,))
    result = result.fetchall()
    conn.close()
    if result:
        return result[0][0]
    else:
        return None
  
  def chercher_id_editeur_db(self, nom_editeur:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_editeur FROM editeurs WHERE nom_editeur=?;"
    result = conn.execute(query, (nom_editeur,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None
    
  def chercher_nom_editeur_db(self, id_editeur:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT nom_editeur FROM editeurs WHERE id_editeur=?;"
    result = conn.execute(query, (id_editeur,))
    result = result.fetchall()
    conn.close()
    if result:
        return result[0][0]
    else:
        return None

  def chercher_nom_genre_db(self, id_genre:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT nom_genre FROM genre WHERE id_genre=?;"
    result = conn.execute(query, (id_genre,))
    result = result.fetchall()
    conn.close()
    if result:
        return result[0][0]
    else:
        return None  

  def chercher_id_isbn_via_titre_db(self, titre:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_isbn FROM livres WHERE titre=?;"
    result = conn.execute(query, (titre,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None

  def chercher_id_isbn_via_nom_auteur_db(self, nom_auteur:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT livres.id_isbn FROM livres INNER JOIN ecrire ON ecrire.id_isbn=livres.id_isbn INNER JOIN auteurs ON auteurs.id_auteur=ecrire.id_auteur WHERE auteurs.nom_auteur=?;"
    result = conn.execute(query, (nom_auteur,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None
    
  def chercher_id_isbn_via_genre_db(self, nom_genre:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT livres.id_isbn FROM livres INNER JOIN genre ON genre.id_genre=livres.id_genre WHERE genre.nom_genre=?;"
    result = conn.execute(query, (nom_genre,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None
    
  def chercher_id_isbn_via_prix_db(self, prix:float):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_isbn FROM livres WHERE prix=?;"
    result = conn.execute(query, (prix,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None

  def chercher_id_isbn_via_id_editeur_db(self, id_editeur:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_isbn FROM livres WHERE id_editeur=?;"
    result = conn.execute(query, (id_editeur,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None

  def chercher_id_isbn_via_quantite_livre_db(self, quantite_livre:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_isbn FROM livres WHERE quantite=?;"
    result = conn.execute(query, (quantite_livre,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None

  def chercher_prix_total_commande_db(self, id_commande):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT livres.prix, detail_commandes.quantite FROM livres INNER JOIN detail_commandes ON livres.id_isbn=detail_commandes.id_isbn INNER JOIN commandes ON commandes.id_commande=detail_commandes.id_commande WHERE commandes.id_commande=?;"
    result = conn.execute(query, (id_commande,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None

  def chercher_prix_quantite_livre_vendue_db(self):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT livres.prix, detail_commandes.quantite FROM livres INNER JOIN detail_commandes ON livres.id_isbn=detail_commandes.id_isbn;"
    result = conn.execute(query)
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None

  def chercher_id_client_db(self, nom_client:str, prenom_client:str):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_client FROM clients WHERE nom_client=? AND prenom_client=?;"
    result = conn.execute(query, (nom_client, prenom_client))
    result = result.fetchall()
    conn.close()
    if result:
        return result[0][0]
    else:
        return None
    
  def chercher_id_commande_db(self, id_client:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_commande FROM commandes WHERE id_client=?;"
    result = conn.execute(query, (id_client,))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None
    
  def chercher_commande_via_id_commande_db(self, id_client:int, id_commande:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT detail_commandes.id_isbn, detail_commandes.quantite FROM detail_commandes INNER JOIN commandes ON commandes.id_commande=detail_commandes.id_commande WHERE commandes.id_client=? AND commandes.id_commande=?;"
    result = conn.execute(query, (id_client, id_commande))
    result = result.fetchall()
    conn.close()
    if result:
        return result
    else:
        return None
    
  def ajouter_details_commande_db(self, id_isbn:int, id_commande:int, quantite:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"INSERT INTO detail_commandes (id_isbn, id_commande, quantite) VALUES (?,?,?);"
    conn.execute(query, (id_isbn, id_commande, quantite))
    conn.commit()
    conn.close()

  def recuperer_information_livre(self, id_isbn:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT titre, annee_publication, id_genre, prix, quantite, id_editeur FROM livres WHERE id_isbn=?;"
    result = conn.execute(query, (id_isbn,))
    result = result.fetchall()
    conn.close()
    return result
  
  def chercher_nom_prenom_auteurs_db(self, id_isbn:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT nom_auteur, prenom_auteur FROM auteurs INNER JOIN ecrire ON ecrire.id_auteur=auteurs.id_auteur WHERE ecrire.id_isbn=?;"
    result = conn.execute(query, (id_isbn,))
    result = result.fetchall()
    conn.close()
    return result

  def supprimer_livre_db(self, id_isbn:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"DELETE FROM livres WHERE id_isbn=?;"
    conn.execute(query,(id_isbn,))
    conn.commit()
    conn.close()

  def supprimer_id_isbn_dans_ecrire_db(self, id_isbn:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"DELETE FROM ecrire WHERE id_isbn=?;"
    conn.execute(query,(id_isbn,))
    conn.commit()
    conn.close()

  def mise_a_jour_quantite_db(self, id_isbn:int, quantite:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"UPDATE livres SET quantite=? WHERE id_isbn=?;"
    conn.execute(query, (quantite, id_isbn))
    conn.commit()
    conn.close()

  def mise_a_jour_depense_client_db(self, total_depense_client:float, id_client):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"UPDATE clients SET total_depense_client=? WHERE id_client=?;"
    conn.execute(query, (total_depense_client, id_client))
    conn.commit()
    conn.close()

  def verifier_si_id_isbn_existe(self, id_isbn:int):
    conn = sqlite3.connect('Data\database_library.db')
    query = f"SELECT id_isbn FROM livres WHERE id_isbn=?;"
    result = conn.execute(query, (id_isbn,))
    result = result.fetchall()
    conn.close()
    if result:
        return True
    else:
        return False