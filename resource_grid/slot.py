#Represent a slot in the resource grid
#A slot is alwase fully allocated to a single user
class slot:
    def __init__(self, place_x, place_y):

        self.subcarriers = [[0 for _ in range(12)] for _ in range(7)]
        
        self.fill_reserved(place_x, place_y)

    def allocate(self, user):
        self.user = user
        
        for i in range(0, 7):
            for j in range(0, 12):
                if(self.subcarriers[i][j] == 0):
                    self.subcarriers[i][j] = self.user

    def fill_reserved(self, place_x, place_y):
        for i in range(0, 7):
            for j in range(0, 12):
                self.subcarriers[i][j] = self.is_it_reserved(place_x, place_y, i, j)
    
    def is_it_reserved(self,place_x, place_y, x, y):

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
        count=0
        for i in range(0, 7):
            for j in range(0, 12):
                if(self.subcarriers[i][j] != -1):
                    count+=1
        
        return count*byte_per_symbol

    def print(self):
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