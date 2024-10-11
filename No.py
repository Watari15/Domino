class Domino():
    def __init__(self,val1,val2):
        """

        # affichage ("---------\n| "+"2"+" | "+"6"+" |\n---------")
        """
        self.val1 = val1
        self.val2 = val2
    
    #////////Méthodes////////
    def double(self):
        if self.val1==self.val2:
            return True
        return False
    def blanc(self):
        if self.val1==0 or self.val2==0:
            return True
        return False
    def nbr_tot_points(self):
        nbr_point = self.val1 + self.val2
    def affichage(self):
        if self.double(self)==True:
            print(" ---\n|" + str(self.val1) + "|\n---\n|" + str(self.val2) + "|\n---")
        else:
            print("---------\n| "+ str(self.val1) +" | "+ str(self.val2) +" |\n---------")
   
    #////////Getteur////////
    def __getgauche__(self):
        return self.val1
    def __getdroite__(self):
        return self.val1
    
    #////////Setteur////////
    def __setgauche__(self,nouvellegauche):
        self.val1 = nouvellegauche
    def __setdroite__(self,nouvelledroite):
        self.val2 = nouvelledroite

# Deuxieme Classe commence ici

class JeuDeDomino():
    def __init__(self,pioche=[],j1=[],j2=[],plateau=[]):
        self.pioche = pioche
        self.j1 = j1
        self.j2 = j2
        self.plateau = plateau
    
    #////////Methodes////////
    
    def melanger(self):
        pass
    def ditribuer(self):
        pass
    def afficher_j1(self):
        pass
    def affichjer_j2(self):
        pass
    def afficher_plateau(self):
        pass
    def tour_j1(self):
        pass
    def tour_j2(self):
        pass
    def jouer(self):
        pass
