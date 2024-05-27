#Represent a slot in the resource grid
#A slot is alwase fully allocated to a single user
class slot:
    user=0
    def __init__(self, place_x, place_y):
        """Créé un slot de la grille de ressources et rajoute les signes réservé par le protocole
        place_x : position en x du slot
        place_y : position en y du slot
        """
        self.subcarriers = [[0 for _ in range(12)] for _ in range(7)]
        
        self.fill_reserved(place_x, place_y)

    def allocate(self, user):
        """Alloue le slot à un utilisateur
        user : l'utilisateur à qui allouer le slot
        """
        self.user = user
        
        for i in range(0, 7):
            for j in range(0, 12):
                if(self.subcarriers[i][j] == 0):
                    self.subcarriers[i][j] = self.user

    def fill_reserved(self, place_x, place_y):
        """Rempli les slots réservés par le protocole
        place_x : position en x du slot
        place_y : position en y du slot
        """
        for i in range(0, 7):
            for j in range(0, 12):
                self.subcarriers[i][j] = self.is_it_reserved(place_x, place_y, i, j)
    
    def is_it_reserved(self,place_x, place_y, x, y):
        """Vérifie si le slot est réservé par le protocole
        place_x : position en x du slot
        place_y : position en y du slot
        x : position en x dans le slot
        y : position en y dans le slot
        """

        if(place_x%2==0 and x<2):
            return -1
        elif(place_x%10==0 and x>4):
            return -1        
        elif((place_x-1)%20==0 and x<4):
            return -1
        elif((y+1)%3==0 and (x==0 or x==4)):
            return -1
        else:
            return 0
    
    def size(self, byte_per_symbol):
        """Retourne la taille du slot en octets utilisable
        byte_per_symbol : nombre d'octets par symbole
        """
        count=0
        for i in range(0, 7):
            for j in range(0, 12):
                if(self.subcarriers[i][j] != -1):
                    count+=1
        
        return count*byte_per_symbol

    def print(self):
        """Affiche le slot
        """
        for j in range(0, 12):
            for i in range(0, 7):
                print(self.subcarriers[i][j], end=" ")
            print()
        print()

    def allocate(self, user):
    
        self.user = user
        
        for i in range(0, 7):
            for j in range(0, 12):
                if(self.subcarriers[i][j] != -1):
                    self.subcarriers[i][j] = self.user

if __name__ == "__main__":
    rg = slot(0,0)

    rg.print()

    rg.allocate(8)

    rg.print()

    print(rg.size())