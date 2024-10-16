from typing import Any 
from random import *

class Domino():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def __getgauche__(self):
        return self.val1

    def __getdroite__(self):
        return self.val2

    def __setgauche__(self, nouvellegauche):
        assert isinstance(nouvellegauche, int), 'La valeur doit être un entier'
        self.val1 = nouvellegauche

    def __setdroite__(self, nouvelledroite):
        assert isinstance(nouvelledroite, int), 'La valeur doit être un entier'
        self.val2 = nouvelledroite

    def double(self):
        return self.val1 == self.val2

    def blanc(self):
        return self.val1 == 0 or self.val2 == 0

    def nbr_tot_points(self):
        return self.val1 + self.val2

    def affichage(self):
        if self.double():
            print("---\n|" + str(self.val1) + "|\n---\n|" + str(self.val2) + "|\n---")
        else:
            print("---------\n| " + str(self.val1) + " | " + str(self.val2) + " |\n---------")

class JeuDomino():
    def __init__(self, pioche=[], j1=[], j2=[], plateau=[]):
        self.j1 = j1
        self.j2 = j2
        self.plateau = plateau
        self.pioche = pioche

    #\\\\\\\\\getters/////////#

    def __getj1__(self):
        return self.j1

    def __getj2__(self):
        return self.j2

    def __getpioche__(self):
        return self.pioche

    def __getplateau__(self):
        return self.plateau

    #\\\\\\\\\setters/////////#

    def __setj1__(self, newj1):
        self.j1 = newj1

    def __setj2__(self, newj2):
        self.j2 = newj2

    def __setpioche__(self, newpioche):
        self.pioche = newpioche

    def __setplateau__(self, newplateau):
        self.plateau = newplateau

    #\\\\\\\\\Méthodes/////////#

    def melanger(self):
        shuffle(self.pioche)

    def distribuer(self):
        for i in range(7):
            self.j1.append(self.pioche.pop())
        
        for j in range(7):
            self.j2.append(self.pioche.pop())

    def afficher_j1(self):
        print("Joueur 1, voici votre main : \n")
        
        for domino in self.j1:
            domino.affichage()
        
        print("********************************************")
    
    def afficher_j2(self):
        print("Joueur 2, voici votre main : \n")
        
        for domino in self.j2:
            domino.affichage()
        
        print("********************************************")    

    def afficher_plateau(self):
        if not self.plateau:
            print("Le plateau est vide.")
        
        elif len(self.plateau) == 1:
            print("Le plateau contient un seul domino :")
            self.plateau[0].affichage()
        
        else:
            print("Le plateau contient les dominos suivants :")
            
            for domino in self.plateau:
                domino.affichage()
    
    def tour_j1(self):
        print("Joueur 1, c'est votre tour !")
        
        choix = input("Choisissez une option :\n \n1. Piocher | \n2. Jouer un domino |\n")
        
        while (choix == '1' and not self.pioche) or choix not in ['1','2']:
            while choix == '1' and not self.pioche:
                print("La pioche est vide. Impossible de piocher.")
                choix = str(input("Choisissez une option :\n \n1. Piocher | \n2. Jouer un domino |\n"))
        
            while choix not in ['1','2']:
                print("Choix invalide, veuillez choisir entre 1 et 2 !")
                choix = input("Choisissez une option :\n \n1. Piocher | \n2. Jouer un domino |\n")            
        
        if choix == '1':
            domino_pioche = self.pioche.pop()
            self.j1.append(domino_pioche)
            print(f"Joueur 1 a pioché le domino : [{domino_pioche.val1} | {domino_pioche.val2}]")
        
        elif choix == '2':
            choixn = []
            n = 1
            
            for i in range(len(self.j1)):
                choixn.append(n)
                n += 1
            
            piece = int(input("Veuillez choisir le domino a jouer ---->"))
            
            while piece not in choixn:
                piece = int(input("Erreur vous n'avez pas rentré un chiffre ou alors ce domino n'existe pas, veuillez entrer le bon numéro de domino ---->"))
            
            valgauche = self.j1[piece - 1].__getgauche__()
            valdroite = self.j1[piece - 1].__getdroite__()
            dominogauche = self.plateau[0]
            dominodroite = self.plateau[-1]
            
            while dominogauche.__getgauche__() not in (valgauche, valdroite) and dominogauche.__getdroite__() not in (valgauche, valdroite) and dominodroite.__getgauche__() not in (valgauche, valdroite) and dominodroite.__getdroite__() not in (valgauche, valdroite):
                print("Ce domino ne peut pas être joué car il ne peut être placé ni a gauche ni a droite")
                piece = int(input("Veuillez choisir le domino a jouer ---->"))
                
                while piece not in choixn:
                    piece = int(input("Erreur, veuillez entrer le numéro du domino ---->"))
                
                valgauche = self.j1[piece - 1].__getgauche__()
                valdroite = self.j1[piece - 1].__getdroite__()                
            
            while True:
                cote = input("De quel côté veux-tu placer le domino ? ---> gauche ou droite ")
                
                if cote.lower() == "gauche":
                    if dominogauche.__getgauche__() in (valgauche, valdroite) or dominogauche.__getdroite__() in (valgauche, valdroite):
                        self.plateau.insert(0, self.j1.pop(piece - 1))
                        break
                    
                    else:
                        print("Le domino ne peut pas être placé car les valeurs ne correspondent pas veuillez le placer a droite")
                        
                elif cote.lower() == 'droite':
                    if dominodroite.__getgauche__() in (valgauche, valdroite) or dominodroite.__getdroite__() in (valgauche, valdroite):
                        self.plateau.append(self.j1.pop(piece - 1))
                        break
                    
                    else:
                        print("Le domino ne peut pas être placé car les valeurs ne correspondent pas veuillez le placer a gauche")
                
                else:
                    print("Choix de côté invalide, il faut choisir 'droite' ou 'gauche'")
        
        else:
            print("Choix invalide")

    def tour_j2(self):
        print("Joueur 2, c'est votre tour !")
        
        choix = input("Choisissez une option :\n \n1. Piocher | \n2. Jouer un domino |\n")
        
        while (choix == '1' and not self.pioche) or choix not in ['1','2']:
            while choix == '1' and not self.pioche:
                print("La pioche est vide. Impossible de piocher.")
                choix = str(input("Choisissez une option :\n \n1. Piocher | \n2. Jouer un domino |\n"))
        
            while choix not in ['1','2']:
                print("Choix invalide, veuillez choisir entre 1 et 2 !")
                choix = input("Choisissez une option :\n \n1. Piocher | \n2. Jouer un domino |\n")   
        
        if choix == '1':
            domino_pioche = self.pioche.pop()
            self.j2.append(domino_pioche)
            print(f"Joueur 2 a pioché le domino : [{domino_pioche.val1} | {domino_pioche.val2}]")
        
        elif choix == '2':
            choixn = []
            n = 1
            
            for i in range(len(self.j2)):
                choixn.append(n)
                n += 1
            
            piece = int(input("Veuillez choisir le domino à jouer ---->"))
            
            while piece not in choixn:
                piece = int(input("Erreur vous n'avez pas rentré un chiffre ou alors ce domino n'existe pas, veuillez entrer le bon numéro de domino ---->"))
            
            valgauche = self.j2[piece - 1].__getgauche__()
            valdroite = self.j2[piece - 1].__getdroite__()
            dominogauche = self.plateau[0]
            dominodroite = self.plateau[-1]
            
            while dominogauche.__getgauche__() not in (valgauche, valdroite) and dominogauche.__getdroite__() not in (valgauche, valdroite) and dominodroite.__getgauche__() not in (valgauche, valdroite) and dominodroite.__getdroite__() not in (valgauche, valdroite):
                print("Ce domino ne peut pas être joué car il ne peut être placé ni à gauche ni à droite")
                piece = int(input("Veuillez choisir le domino à jouer ---->"))
                
                while piece not in choixn:
                    piece = int(input("Erreur, veuillez entrer le numéro du domino ---->"))
                
                valgauche = self.j2[piece - 1].__getgauche__()
                valdroite = self.j2[piece - 1].__getdroite__()                
            
            while True:
                cote = input("De quel côté veux-tu placer le domino ? ---> gauche ou droite ")
                
                if cote.lower() == "gauche":
                    if dominogauche.__getgauche__() in (valgauche, valdroite) or dominogauche.__getdroite__() in (valgauche, valdroite):
                        self.plateau.insert(0, self.j2.pop(piece - 1))
                        break
                    
                    else:
                        print("Le domino ne peut pas être placé car les valeurs ne correspondent pas, veuillez le placer à droite")
                        
                elif cote.lower() == 'droite':
                    if dominodroite.__getgauche__() in (valgauche, valdroite) or dominodroite.__getdroite__() in (valgauche, valdroite):
                        self.plateau.append(self.j2.pop(piece - 1))
                        break
                    
                    else:
                        print("Le domino ne peut pas être placé car les valeurs ne correspondent pas, veuillez le placer à gauche")
                
                else:
                    print("Choix de côté invalide, il faut choisir 'droite' ou 'gauche'")
        
        else:
            print("Choix invalide")


pioche = [Domino(i, j) for i in range(7) for j in range(i, 7)]
jeu = JeuDomino(pioche)
jeu.melanger()
jeu.distribuer()
jeu.plateau.append(pioche.pop())
jeu.__setpioche__([])
