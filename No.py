class Domino():
    def __init__(self,val1,val2):
        """

        # affichage ("---------\n| "+"2"+" | "+"6"+" |\n---------")
        """
        self.val1 = val1
        self.val2 = val2
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
            print(" ---\n|" + self.val1 + "|\n---\n|" + self.val2 + "|\n---")
        else:
            print("---------\n| "+ str(self.val1) +" | "+ str(self.val2) +" |\n---------")
