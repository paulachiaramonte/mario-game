       
class StaticBarrel:
    
    """ THE CONSTRUCTOR OF THE CLASS STATIC BARREL ONLY CONTAINS THE POSITION X AND THE POSITION Y"""
    def __init__(self, x, y):
        self.__posX = x
        self.__posY = y
     
    @property
    def posX(self):
        return self.__posX
    
    @property 
    def posY(self):
        return self.__posY