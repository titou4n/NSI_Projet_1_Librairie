from Data.database_library import DatabaseLibrary
import datetime

database_library = DatabaseLibrary()

def menu():
  '''
  Fonction qui permet d'afficher le menu de la librairie (prend aucun argument)
  '''
  print("\n_______________________________________Menu_______________________________________")
  print("1-  Ajouter un livre")
  print("2-  Supprimer un livre")
  print("3-  Rechercher un livre")
  print("4-  Vendre un livre / Faire une commande")
  print("5-  Montant de livre vendue")
  print("6-  Pour visualiser le montant total du client")
  print("7-  Quitter")
  choix_menu = str(input("Votre choix : "))
  if choix_menu == "1":
    ajouter_livre()
  if choix_menu == "2":
    supprimer_livre()
  if choix_menu == "3":
    rechercher_livre()
  if choix_menu == "4":
    id_client = recherche_client()
    while id_client == None:
      id_client = recherche_client()
    id_commande = creation_commande(id_client)
    commande(id_client, id_commande)
  if choix_menu == "5":
    montant_livre_vendue()
  if choix_menu == "6":
    recherche_client()
  if choix_menu == "7":
    quit()
  menu()

def ajouter_livre():
  '''
  Fonction qui permet d'ajouter un livre dans la base de donnée de la librairie (prend aucun argument)
  '''
  print("\n____________________________Ajouter_un_livre____________________________")
  titre = demander_titre_livre()
  while titre == None:
    titre = demander_titre_livre()
  livres_possibles(titre)
  liste_id_auteurs  = demander_auteurs_livre()
  while liste_id_auteurs == None:
    liste_id_auteurs = demander_auteurs_livre()
  annee_publication = demander_annee_publication_livre()
  while annee_publication == None:
    annee_publication = demander_annee_publication_livre()
  id_editeur = demander_id_editeur_livre()
  while id_editeur == None:
    id_editeur = demander_id_editeur_livre()
  id_genre = demander_genre_livre()
  while id_genre == None:
    id_genre = demander_genre_livre()
  prix  = demander_prix_livre()  
  while prix == None:
    prix  = demander_prix_livre()
  quantite = demander_quantite_livre()
  while quantite == None:
    quantite = demander_quantite_livre()
  database_library.ajouter_livre_db(titre=titre, annee_publication=annee_publication, id_genre=id_genre, prix=prix, quantite=quantite, id_editeur=id_editeur)
  liste_id_isbn = database_library.chercher_id_isbn_via_titre_db(titre)
  id_isbn = liste_id_isbn[0][0]
  for i in range(len(liste_id_auteurs)):
    id_auteur = liste_id_auteurs[i]
    database_library.ajouter_table_ecrire_db(id_isbn, id_auteur)
  print("\nLe livre " + titre + " à été ajouté avec succès.")
  menu()

def supprimer_livre():
  '''
  Fonction qui permet de supprimer un livre
  '''
  print("\n_______________________Supprimer_un_livre_______________________")
  print("Rechercher le Livre à supprimer ")
  id_isbn = rechercher_livre()
  verification = str(input("\nÊtes vous sûres de vouloir supprimer ce livre (O->Oui/N->NON) :"))
  if verification == "O" or verification == "o":
    database_library.supprimer_livre_db(id_isbn)
    database_library.supprimer_id_isbn_dans_ecrire_db(id_isbn)
    print("Le livre à été supprimé avec succès.")
    menu()  
  else:
    print("Retour au menu...")
    menu()

def rechercher_livre():
  '''
  Fonction qui permet de rechercher un livre
  '''
  print("\n________Rechercher_livre________")
  print("1-  Rechercher par titre")
  print("2-  Rechercher par auteur")
  print("3-  Rechercher par genre")
  print("4-  Rechercher par isbn")
  print("5-  Rechercher par prix")
  print("6-  Rechercher par éditeur")
  print("7-  Rechercher par quantité")
  print("8-  Retourner  au  menu")
  choix_recherche_livre = str(input("Votre choix : "))
  liste_id_isbn = []
  if choix_recherche_livre == "1":
    titre = demander_titre_livre()
    liste_id_isbn = database_library.chercher_id_isbn_via_titre_db(titre)
  if choix_recherche_livre == "2":
    nom_auteur = str(input("\nAuteur du livre : ")).strip().upper()
    liste_id_isbn = database_library.chercher_id_isbn_via_nom_auteur_db(nom_auteur)
  if choix_recherche_livre == "3":
    nom_genre = demander_genre_livre()
    liste_id_isbn = database_library.chercher_id_isbn_via_genre_db(nom_genre)
  if choix_recherche_livre == "4":
    id_isbn = str(input("\nISBN du livre : "))
    if database_library.verifier_si_id_isbn_existe(id_isbn):
      info_livre(id_isbn)
      return id_isbn
    else:
      print("Aucun id est liée à votre recherche.")
      choix_ajouter = str(input("Voulez-vous ajouter un livre ? (O->Oui/N->Non) : "))
      if choix_ajouter == "O" or choix_ajouter == "o":
        ajouter_livre()
      else:
        rechercher_livre()
  if choix_recherche_livre == "5":
    prix = demander_prix_livre()
    liste_id_isbn = database_library.chercher_id_isbn_via_prix_db(prix)
  if choix_recherche_livre == "6":
    id_editeur = demander_id_editeur_livre()
    liste_id_isbn = database_library.chercher_id_isbn_via_id_editeur_db(id_editeur)
  if choix_recherche_livre == "7":
    quantite_livre = demander_quantite_livre()
    liste_id_isbn = database_library.chercher_id_isbn_via_quantite_livre_db(quantite_livre)
  if choix_recherche_livre == "8":
    menu()
  if liste_id_isbn == None :
    print("Aucun livre liée a votre recherche éxiste dans la base de données.")
    choix_ajouter = str(input("Voulez-vous ajouter un livre ? (O->Oui/N->Non) : "))
    if choix_ajouter == "O" or choix_ajouter == "o":
      ajouter_livre()
    else:
      rechercher_livre()
  elif len(liste_id_isbn) >= 1:
    for i in range(len(liste_id_isbn)):
      print("\nLivre "+str(i+1)+ " : ")
      info_livre(liste_id_isbn[i][0])
    choice_id_isbn = int(input("Veuillez-entrez l'id du livre que vous recherchiez : "))
    existe = database_library.verifier_si_id_isbn_existe(choice_id_isbn)
    while existe == False:
      choice_id_isbn = int(input("Veuillez-entrez l'id du livre que vous recherchiez : "))
      existe = database_library.verifier_si_id_isbn_existe(choice_id_isbn)
    return choice_id_isbn

def recherche_client():
  '''
  Cette fonction permet de rechercher l'id du client et si il n'existe pas dans la base de données, l'ajouter.
  recherche_client() retourne l'id du client
  '''
  nom_client    = str(input("\nNom du client    : ")).upper()
  if not nom_client:
    print("Veuillez-entrez le nom du client.")
    return None
  else:
    prenom_client = str(input("Prenom du client : ")).lower().capitalize()
    if not prenom_client:
      print("Veuillez-entrez le prénom du client.")
      return None
    else:
      if database_library.chercher_id_client_db(nom_client, prenom_client) == None:
        database_library.ajouter_client_db(nom_client, prenom_client)
      print("Bonjour "+prenom_client+" "+ nom_client+", Comment allez-vous ?")
      id_client = database_library.chercher_id_client_db(nom_client, prenom_client)
      print("\nLe montant total que le client a dépensé est de "+str(database_library.chercher_depense_client_db(id_client))+"€")
      return id_client

def creation_commande(id_client:int):
  '''
  Cette fonction permet de créer une commande et de prendre la dernière que le client vient de réaliser
  creation_commande() retourne l'id de la commande
  '''
  database_library.ajouter_commande_db(id_client, datetime.datetime.now())
  liste_id_commande     = database_library.chercher_id_commande_db(id_client)
  len_liste_id_commande = len(liste_id_commande)-1
  id_commande           = liste_id_commande[len_liste_id_commande][0]
  return id_commande

def commande(id_client:int, id_commande:int):
  '''
  Cette fonction permet d'éffectuer une commande
  commande(id_client:int, id_commande:int)
  Prend en argument id_client:int et id_commande:int
  '''
  print("\n__________________Commande__________________")
  id_isbn           = rechercher_livre()
  quantite_a_vendre = input("\nVeuillez-entrez la quantité de livre à vendre : ")
  if int(quantite_a_vendre) == ValueError:
    print("Veuillez entrer un chiffre ou un nombre pour la quantité de livre a vendre.")
    commande(id_client, id_commande)
  else:
    quantite_a_vendre = int(quantite_a_vendre)
    info_livre = database_library.recuperer_information_livre(id_isbn)
    quantite_livres_db =info_livre[0][4]
    quantite_livres_db = quantite_livres_db - quantite_a_vendre
    if quantite_livres_db < 0:
      print("Il n'y a pas assez de livre.")
      commande(id_client, id_commande)
    else :
      database_library.ajouter_details_commande_db(id_isbn, id_commande, quantite_a_vendre)
      database_library.mise_a_jour_quantite_db(id_isbn, quantite_livres_db)
      choix_continuer_achat = str(input("Voulez-vous continuer vos achats (O->Oui/N->Non) : "))
      if choix_continuer_achat == "O" or choix_continuer_achat == "o":
        liste_commande = database_library.chercher_commande_via_id_commande_db(id_client, id_commande)
        afficher_commande(liste_commande, id_commande)
        commande(id_client, id_commande)
      else:
        liste_commande = database_library.chercher_commande_via_id_commande_db(id_client, id_commande)
        montant_commande = afficher_commande(liste_commande, id_commande)
        montant_total_client_depanse = database_library.chercher_depense_client_db(id_client=id_client)+montant_commande
        database_library.mise_a_jour_depense_client_db(total_depense_client=montant_total_client_depanse, id_client=id_client)
        print("\nLe montant total que le client a dépensé est de "+str(database_library.chercher_depense_client_db(id_client))+"€")
        menu()

def afficher_commande(liste_commande:list, id_commande:int):
  '''
  Cette fonction permet d'afficher la commande
  afficher_commande(liste_commande:list, id_commande:int) et renvoit montant_total_commande:float
  Prend en argument liste_commande:list et id_commande:int et renvoit le montant total de la commande
  '''
  print("\nCommande n° : "+str(id_commande))
  print("   Titre du livre :                        Quantité : ")
  for i in range(len(liste_commande)):
    id_isbn = liste_commande[i][0]
    information_livre = database_library.recuperer_information_livre(id_isbn)
    prix = information_livre[0][3]
    info_livre = database_library.recuperer_information_livre(id_isbn)
    len_titre_livre = len(info_livre[0][0])
    espace_titre_quantite = 40-len_titre_livre
    print(str(i+1)+"- "+str(info_livre[0][0])+" "*espace_titre_quantite+str(liste_commande[i][1])+"  *  "+str(prix)+"€")
    #total_depense_livre = int(liste_commande[i][1])*prix
  prix_quantite_commande = database_library.chercher_prix_total_commande_db(id_commande)
  montant_commande = 0
  for i in range(len(prix_quantite_commande)):
    prix     =  prix_quantite_commande[i][0]
    quantite = prix_quantite_commande[i][1]
    montant_commande = montant_commande+(prix*quantite)
  print("\nLe montant de cette commande est de "+str(montant_commande)+"€")
  return montant_commande

def montant_livre_vendue():
  '''
  Cette fonction permet d'afficher le montant de livre vendue
  '''
  prix_quantite_livre_vendu = database_library.chercher_prix_quantite_livre_vendue_db()
  if prix_quantite_livre_vendu == None:
    print("\nAucun livre n'a encore été vendu.")
  else:
    montant_livre_vendue = 0
    for i in range(len(prix_quantite_livre_vendu)):
      prix     =  prix_quantite_livre_vendu[i][0]
      quantite = prix_quantite_livre_vendu[i][1]
      montant_livre_vendue = montant_livre_vendue+(prix*quantite)
    print("\nLe montant de livre vendu est de "+str(montant_livre_vendue)+"€")
    menu()

def info_livre(id_isbn:int):
  '''
  Cette fonction permet d'afficher le montant de livre vendue
  info_livre(id_isbn:int)
  Prend en argument id_isbn:int du livre
  '''
  info_livre    = database_library.recuperer_information_livre(id_isbn)
  nom_editeur   = database_library.chercher_nom_editeur_db(info_livre[0][5])
  nom_genre     = database_library.chercher_nom_genre_db(info_livre[0][2])
  liste_auteurs = database_library.chercher_nom_prenom_auteurs_db(id_isbn)
  print("\nID ISBN              : " + str(id_isbn))
  print("Titre du livre       : " + str(info_livre[0][0]))
  for i in range(len(liste_auteurs)):
    print("Auteur             "+str(i+1)+" : "+str(liste_auteurs[i][1])+" "+str(liste_auteurs[i][0]))
  print("Année de publication : " + str(info_livre[0][1]))
  print("Genre                : " + str(nom_genre))
  print("Prix                 : " + str(info_livre[0][3]) + "€")
  print("Quantité             : " + str(info_livre[0][4]))
  print("Nom éditeur          : " + str(nom_editeur))

def demander_titre_livre():
  '''
  Cette fonction demande le titre du livre et le retourne si il est correcte sinon retourne None
  demander_titre_livre() retourne titre:str
  '''
  titre = str(input("Titre du livre       : ")).strip().capitalize()
  if not titre:
    print("veuillez-entrez un titre")
    return None
  else:
    return titre
    
def demander_auteurs_livre():
  '''
  Cette fonction demande le nbr d'auteurs puis le nom et prénom retourne la liste des id des auteurs sinon retourne None
  demander_auteurs_livre() retourne liste_id_auteurs:list
  '''
  try:
    nbr_auteurs = int(input("Nombre d'auteurs     : "))
    if nbr_auteurs < 0 or not nbr_auteurs:
      print("Veuillez-entrer un nombre positif d'auteurs.")
      return None
    else:
      liste_id_auteurs = []
      for i in range(nbr_auteurs):
        nom_auteur    = str(input("Nom de l'auteur     "+str(i+1)+": ")).strip().upper()
        if len(nom_auteur) == 0 or not nom_auteur:
          print("Veuillez-entrer le nom d'auteur.")
          return None
        if database_library.chercher_id_auteur_db(nom_auteur) != None:
          id_auteur = database_library.chercher_id_auteur_db(nom_auteur)
          liste_id_auteurs.append(id_auteur)
        else:
          prenom_auteur = str(input("Prénom de l'auteur  "+str(i+1)+": ")).strip().lower().capitalize()
          if len(prenom_auteur)==0 or prenom_auteur == None:
            print("Veuillez-entrer le prénom d'auteur.")
            return None
          database_library.ajouter_auteur_livre_db(nom_auteur, prenom_auteur)
          id_auteur = database_library.chercher_id_auteur_db(nom_auteur)
          liste_id_auteurs.append(id_auteur)
    return liste_id_auteurs
  except ValueError:
    print("Veuillez-entrer le nombres d'auteurs.")
    return None

def demander_annee_publication_livre():
  '''
  Cette fonction demande l'année de publication du livre sinon retourne None
  demander_annee_publication_livre() retourne annee_publication:int
  '''
  try:
    annee_publication = int(input("Année de publication : "))
    if annee_publication == None or not annee_publication or annee_publication > datetime.datetime.now().year:
      print("Veuillez-entrer l'année de publication.")
      return None
    else:
      return annee_publication
  except:
    print("Veuillez-entrer l'année de publication.")
    return None

def demander_id_editeur_livre():
  '''
  Cette fonction demande le nom de l'éditeur et retourne son id sinon retourne None
  demander_id_editeur_livre() retourne id_editeur:int
  '''
  nom_editeur = str(input("Nom de l'editeur     : ")).strip().capitalize()
  if not nom_editeur:
      print("Veuillez-entrer le nom de l'éditeur.")
      return None
  else:
    liste_id_editeur = database_library.chercher_id_editeur_db(nom_editeur)
    if liste_id_editeur == None:
      database_library.ajouter_editeur_livre_db(nom_editeur)
      liste_id_editeur = database_library.chercher_id_editeur_db(nom_editeur)
    id_editeur = liste_id_editeur[0][0]
    return id_editeur

def demander_genre_livre():
  '''
  Cette fonction demande le genre du livre et retourne son id sinon retourne None
  demander_genre_livre() retourne id_genre:int
  '''
  genre = str(input("Genre du livre       : ")).strip().capitalize()
  if not genre :
      print("Veuillez-entrer un genre.")
      return None
  else:
    liste_id_genre = database_library.chercher_id_genre_db(genre)
    if liste_id_genre == None:
      database_library.ajouter_genre_db(genre)
      liste_id_genre = database_library.chercher_id_genre_db(genre)
    id_genre = int(liste_id_genre[0][0])
    return id_genre
  
def demander_prix_livre():
  '''
  Cette fonction demande le prix du livre et retourne son id sinon retourne None
  demander_prix_livre() retourne prix:float
  '''
  try:
    prix = float(input("Prix du livre en €   : "))
    if not prix or prix < 0:
      print("Le prix doit être positif")
      return None
    else:
      return prix
  except:
    print("Le prix doit être positif")
    return None

def demander_quantite_livre():
  '''
  Cette fonction demande la quantité de livre à ajouter et retourne sa qunatité sinon retourne None
  demander_quantite_livre() retourne quantite:int
  '''
  try:
    quantite = int(input("Nombre de livre      : "))
    if not quantite or quantite < 0:
      print("Le nombre de livre doit être positif.")
      return None
    else:
      return quantite
  except:
    print("Le nombre de livre doit être positif.")
    return None

def livres_possibles(titre:str):
  '''
  Cette fonction permet d'afficher le livre si il existe dans la base de donnée
  et si il éxiste proposer de metre à jour la quantité de ce livre
  livres_possibles(titre:str)
  Prend en argument le titre:str du livre
  '''
  liste_id_isbn_possibles = database_library.chercher_id_isbn_via_titre_db(titre)
  if liste_id_isbn_possibles != None :
    print("\nLivres possibles : ")
    for i in range(len(liste_id_isbn_possibles)):
      id_isbn_possibles= liste_id_isbn_possibles[i][0]
      info_livre(id_isbn_possibles)
    verification_id_isbn = str(input("Est-ce un des livres presentés si dessus (O->Oui/N->Non) : "))
    if verification_id_isbn == "O" or verification_id_isbn == "o":
      id_isbn = int(input("\nVeuillez entrez l'ISBN correspondant : "))
      choix_mettre_jour_quantite_stock = str(input("Voullez-vous mettre à jour la quantité du stock (O->Oui/N->Non) : "))
      if choix_mettre_jour_quantite_stock =="O" or choix_mettre_jour_quantite_stock == "o":
        quantite_a_ajouter = input("\nVeuillez entrez la quantité de livre à ajouter : ")
        if int(quantite_a_ajouter) == ValueError:
          print("Veuillez entrer un chiffre ou un nombre pour la quantité de livre à ajouter.")
          ajouter_livre()
        else:
          quantite_a_ajouter = int(quantite_a_ajouter)
          information_livre  = database_library.recuperer_information_livre(id_isbn)
          quantite_livres_db = information_livre[0][4]
          quantite_livres_db = quantite_livres_db + quantite_a_ajouter
          database_library.mise_a_jour_quantite_db(id_isbn, quantite_livres_db)
          menu()
      else:
        menu()
    else:
      print("Excuser moi de ce dérangement, je vous laisse continuer...")

if __name__ == "__main__":
  #database_library.connection_db()
  menu()


