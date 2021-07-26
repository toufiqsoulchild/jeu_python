from os import remove
from random import randint

def calculatrice():
    a = input("Entrez un premier nombre: ")
    b = input("Entrez un deuxieme nombre: ")

    if  (a.isdigit() and b.isdigit()) is False:
        print("Entrez deux nombres valides !")
    else:
        a,b = int(a),int(b)
        print(f"le resultat de l'addition de {a} avec {b} est {a + b}.")

def liste():
    a = "1: Ajouter un élément à la liste"
    b = "2: Retirer un élément de la liste"
    c = "3: Afficher la liste"
    d = "4: Vider la liste"
    e = "5: Quitter\n"
    f = 0
    courses = []
    options = [a, b, c, d, e]
    while f != 5:
        for choix in options:
            print(choix)
        
        f = int(input("Faite votre choix: "))
        if f == 1:
            courses.extend([input("Que voulez ajouter ? ")])
        elif f == 2:
            stuff = (input("Que voulez retirer ? "))
            if stuff in courses:
                courses.pop(courses.index(stuff))
                print(f"\nl'élément {stuff} à bien été supprimée de la liste.\n")
            else: 
               print(f"\nL'élément {stuff} n'est pas dans la liste.\n")
        elif f == 3:
            if len(courses) == 0:
                print("\nLa liste ne contient aucun élément\n")
            else:  
                print("\nVoici le contenu de la liste: ")
                for stuff in courses:
                    print(f" {courses.index(stuff)+1}. {stuff}\n")
        elif f == 4:
            for stuff in courses:
                courses.remove(stuff)
            print("\nLa liste a été vidée de sont contenu.\n")
               
    print("\nA bientôt\n")

def nombre_mystere():
    print("#"*43 + "\n" + "#"*10 + " Jeu du nombre mystère " + "#"*10 + "\n" + "#"*43)
    essais = 5
    mystere = input("Saisir le nombre mystère: ")
    retry=""

    while essais > 0:
            saisie = input("Devine le nombre mystère: ")
            if not saisie.isdigit():
                print("\nVeuillez saisir un nombre valide !\n")   
                continue
           
            if int(saisie) > int(mystere):
                print (f"Le nombre mystère est plus petit que {saisie}.\n")

            elif int(saisie) < int(mystere):
                print (f"\nLe nombre mystère est plus grand que {saisie}.\n")
            else:
                break
            essais = essais - 1
            print (f"Il te reste {essais} essais.\n")

    
    if essais == 0:
        print("Vous n'avez plus d'essais.\nFin du game")
    
    elif int(saisie) == int(mystere):
            print(f"\nBravo ! Vous avez trouvé le nombre en {6-essais} essais.\nFin du jeu.")
    
def jeu():
    pvg = 50
    pve = 50
    nb_potions = 3
    
    
    while pve !=0 and pvg !=0:
        potion = randint(15,50)
        attaque = randint(5,10)
        attaqueEn = randint(5,15)
        action = input("Souhaitez vous attaquer (1) ou utiliser une potion (2) ? ")
        
        if action == "1":
            pvg = pvg - attaqueEn
            pve = pve - attaque
            print (f"\nVous avez infligé {attaque} point de dégats.\n")
            print (f"L'ennemi vous a infligé {attaqueEn} points de dégats.\n")
            print (f"Il vous reste {pvg} points de vie.\n")
            print (f"Il reste {pve} points de vie à l'ennemi.\n" + "-"*50)

        elif action == "2":
            pvg = pvg + potion
            print(f"\nVous avez récupéré {potion} points de vie.")
            if nb_potions > 0:     
                nb_potions = potion - 1
            else:
                print("Vous n'avez plus de potions")
        
        elif not action.isdigit():
            continue
        elif action != "1" and action != "2":
            continue
        
        elif action == "":
            print("Vous passez votre tour !")

    if pve <= 0:
        print("tu as gagné !")       
    elif pvg <= 0:
        print("Tu as perdu !")
    print("fin du jeu.")
    
jeu()
        

    
