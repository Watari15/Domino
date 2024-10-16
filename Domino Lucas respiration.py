from typing import Any 
from random import *
from colorama import *
from time import *

class Domino():
    def __init__(self, val1, val2):
        """
        Initialise un objet Domino.
        :param val1: (int) La valeur d'un côté du domino.
        :param val2: (int) La valeur de l'autre côté du domino.
        """        
        self.val1 = val1
        self.val2 = val2

    def __getgauche__(self):
        """
        Obtient la valeur du côté gauche du domino.
        :return: (int) La valeur du côté gauche du domino.
        """        
        return self.val1

    def __getdroite__(self):
        """
        Obtient la valeur du côté droit du domino.
        :return: (int) La valeur du côté droit du domino.
        """
        return self.val2

    def __setgauche__(self, nouvellegauche):
        """
        Définit la valeur du côté gauche du domino.
        :param nouvellegauche: (int) La nouvelle valeur pour le côté gauche.
        """
        assert isinstance(nouvellegauche, int), 'La valeur doit être un entier'
        self.val1 = nouvellegauche

    def __setdroite__(self, nouvelledroite):
        """
        Définit la valeur du côté droit du domino.
        :param nouvelledroite: (int) La nouvelle valeur pour le côté droit.
        """        
        assert isinstance(nouvelledroite, int), 'La valeur doit être un entier'
        self.val2 = nouvelledroite

    def double(self):
        """
        Vérifie si le domino est un double.
        :return: (bool) True si le domino est un double, sinon False.
        """        
        return self.val1 == self.val2

    def blanc(self):
        """
        Vérifie si le domino a un côté blanc.
        :return: (bool) True si au moins un côté est 0, sinon False.
        """
        return self.val1 == 0 or self.val2 == 0

    def nbr_tot_points(self):
        """
        Calcule le nombre total de points sur le domino.
        :return: (int) La somme des valeurs des deux côtés du domino.
        """
        return self.val1 + self.val2

    def affichage(self):
        """
        Affiche le domino dans la console.
        """
        if self.double():
            print("---\n|" + str(self.val1) + "|\n---\n|" + str(self.val2) + "|\n---")
        else:
            print("---------\n| " + str(self.val1) + " | " + str(self.val2) + " |\n---------")

class JeuDomino():
    def __init__(self, pioche=[], j1=[], j2=[], plateau=[]):
        """
        Initialise un objet JeuDomino.
        :param pioche: (list) La pile de dominos à piocher.
        :param j1: (list) La main du joueur 1.
        :param j2: (list) La main du joueur 2.
        :param plateau: (list) Le plateau de jeu contenant les dominos joués.
        """
        self.j1 = j1
        self.j2 = j2
        self.plateau = plateau
        self.pioche = pioche

    #\\\\\\\\\getters/////////#

    def __getj1__(self):
        """
        Obtient la main du joueur 1.
        :return: (list) La main du joueur 1.
        """
        return self.j1

    def __getj2__(self):
        """
        Obtient la main du joueur 2.
        :return: (list) La main du joueur 2.
        """        
        return self.j2

    def __getpioche__(self):
        """
        Obtient la pioche.
        :return: (list) La pile de dominos à piocher.
        """
        return self.pioche

    def __getplateau__(self):
        """
        Obtient le plateau de jeu.
        :return: (list) Le plateau de jeu contenant les dominos joués.
        """
        return self.plateau

    #\\\\\\\\\setters/////////#

    def __setj1__(self, newj1):
        """
        Définit la main du joueur 1.
        :param newj1: (list) La nouvelle main pour le joueur 1.
        """
        self.j1 = newj1

    def __setj2__(self, newj2):
        """
        Définit la main du joueur 2.
        :param newj2: (list) La nouvelle main pour le joueur 2.
        """
        self.j2 = newj2

    def __setpioche__(self, newpioche):
        """
        Définit la pioche.
        :param newpioche: (list) La nouvelle pile de dominos à piocher.
        """
        self.pioche = newpioche

    def __setplateau__(self, newplateau):
        """
        Définit le plateau de jeu.
        :param newplateau: (list) Le nouveau plateau de jeu.
        """
        self.plateau = newplateau

    #\\\\\\\\\Méthodes/////////#

    def melanger(self):
        """
        Mélange la pioche de dominos.
        """
        shuffle(self.pioche)

    def distribuer(self):
        """
        Distribue 7 dominos à chaque joueur à partir de la pioche.
        """
        for i in range(7):
            self.j1.append(self.pioche.pop())
        
        for j in range(7):
            self.j2.append(self.pioche.pop())

    def afficher_j1(self):
        """
        Affiche la main du joueur 1 dans la console.
        """
        print("Voici votre main : \n")
        sleep(1)
        n=1
        for domino in self.j1:
            print("Domino numéro", Fore.YELLOW, str(n),Fore.WHITE)
            domino.affichage()
            n+=1
        
        print("********************************************")
    
    def afficher_j2(self):
        """
        Affiche la main du joueur 2 dans la console.
        """
        sleep(1)
        print("Voici votre main : \n")
        n=1
        for domino in self.j2:
            print("Domino numéro", Fore.YELLOW, str(n),Fore.WHITE)
            domino.affichage()
            n+=1
        
        print("********************************************")    

    def afficher_plateau(self):
        """
        Affiche le plateau de jeu dans la console.
        """
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
        """
        Gère le tour du joueur 1 : affiche le plateau, sa main, et permet de piocher ou de jouer un domino.
        """
        print(Fore.YELLOW,"Joueur 1, c'est votre tour !",Fore.WHITE)
        sleep(2)
        
        self.afficher_plateau()
        sleep(2)
        self.afficher_j1()
        sleep(1)
        
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
                        print("Le joueur 1 a placé son domino à gauche")
                        sleep(2)
                        
                        break
                    
                    else:
                        print("Le domino ne peut pas être placé car les valeurs ne correspondent pas veuillez le placer a droite")
                        
                elif cote.lower() == 'droite':
                    if dominodroite.__getgauche__() in (valgauche, valdroite) or dominodroite.__getdroite__() in (valgauche, valdroite):
                        self.plateau.append(self.j1.pop(piece - 1))
                        print("Le joueur 1 a placé son domino à droite")
                        sleep(2)
                        break
                    
                    else:
                        print("Le domino ne peut pas être placé car les valeurs ne correspondent pas veuillez le placer a gauche")
                
                else:
                    print("Choix de côté invalide, il faut choisir 'droite' ou 'gauche'")
        
        else:
            print("Choix invalide")

    def tour_j2(self):
        """
        Gère le tour du joueur 2 : affiche le plateau, sa main, et permet de piocher ou de jouer un domino.
        """
        print(Fore.YELLOW,"Joueur 2, c'est votre tour !",Fore.WHITE)
        sleep(2)
        
        self.afficher_plateau()
        sleep(2)
        self.afficher_j2()
        sleep(1)
        
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
                        print("Le joueur 2 a placé son domino à gauche")
                        sleep(2)
                        break
                    
                    else:
                        print("Le domino ne peut pas être placé car les valeurs ne correspondent pas, veuillez le placer à droite")
                        
                elif cote.lower() == 'droite':
                    if dominodroite.__getgauche__() in (valgauche, valdroite) or dominodroite.__getdroite__() in (valgauche, valdroite):
                        self.plateau.append(self.j2.pop(piece - 1))
                        print("Le joueur 2 a placé son domino à gauche")
                        sleep(2)
                        break
                    
                    else:
                        print("Le domino ne peut pas être placé car les valeurs ne correspondent pas, veuillez le placer à gauche")
                
                else:
                    print("Choix de côté invalide, il faut choisir 'droite' ou 'gauche'")
        
        else:
            print("Choix invalide")
    
    def jeu(self):
        
        
        print("Bienvenue au jeu de domino ! Ce jeu ce joue a deux joueurs")
        
        print(Fore.BLUE +"Initialisation du jeu...")
        
        sleep(1)
        
        print("Mélange des dominos...")
        
        self.melanger()
        sleep(2)
        
        print("Distribution des dominos ...")
        
        sleep(1)
        self.distribuer()
        
        print("Placement du domino principal en cours...",Fore.WHITE)
        
        self.plateau.append(pioche.pop())
        
        sleep(1)
        
        print("Le jeu peut maintenant commencer :")
        
        while True:
            self.tour_j1()
            if self.j1==[]:
                break
            self.tour_j2()
            if self.j2==[]:
                break
        
        if self.j1==[]:
            print(Fore.YELLOW,"Bravo, le joueur 1 a gagné !",Fore.WHITE)
        
        else:
            print(Fore.YELLOW,"Bravo, le joueur 2 a gagné !",Fore.WHITE)
        
        
        
        
        
        
        


pioche = [Domino(i, j) for i in range(7) for j in range(i, 7)]
jeu = JeuDomino(pioche)
jeu.jeu()
