import os 
import csv
from datetime import datetime

FICHIER= "budget.csv"

def initialiser_fichier():
    if not os.path.exists(FICHIER):
     with open(FICHIER,"w",newline="") as fichier:
        writer=csv.writer(fichier)
        writer.writeow(["date","type","categorie","montant","description"])
def ajouter_transaction():
    date=datetime.now().strftime("%d/%m/%y")
    tyte_transaction=input("type(revenu/depense):").lower
    categorie=input("categorie:") 
try:
    Montant=float(input("montant:"))
except ValueError:

    print("montant invalide")
    return
    
description=input("description:")


with open(FICHIER,"a",newline="")as fichier:
    writer=csv.writer(fichier)
    writer.writerow(["date","type_transaction","categorie", "montant", description])
    print("transaction ajoutée")


    def afficher_transaction():
        with open(FICHIER,"r") as fichier:
            reader=csv.reader(fichier)
            for ligne in reader:
                print(ligne)


    def calculer_solde():
        revenus=0
        depenses=0
        with open(FICHIER,"r") as f:
            reader=csv.DictReade(fichier)
            for row in reader:
                montant=float(row["montant"])
                if row|["type"]=="revenus":
                    revenus += montant
                elif row["type"]=="depenses":
                    depenses += montant

        solde= revenus-depenses
        print(f"revenus:{"revenus"}") 
        print(f"depenses:{"depenses"}") 
        print(f"solde:{solde}")    



def menu():
    initialiser_fichier()

    while True:
        print("   TRACKER DE BUDGET     ")
        print("1. ajouter transaction")
        print("2.voir transaction")
        print("3.voir solde ")
        print("4. quitter")

    choix=input("choix:")

    if choix =="1" : 
        ajouter_transaction()
    elif choix== "2":
        afficher_transaction()
    elif choix == "3":
        calculer_solde()
    elif choix == "4":
        print("quitter")
                  
    else:
     print("choix invalide")
    break 
    


menu()






       











