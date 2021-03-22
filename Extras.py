class Oil:
    """ THE CONSTRUCTOR OF THE CLASS OIL ONLY CONTAINS THE POSITION X AND THE POSITION Y"""
    def __init__(self, x, y):
        self.__posX = x
        self.__posY = y
    
    @property
    def posX(self):
        return self.__posX
    
    @property
    def posY(self):
        return self.__posY
    
class princessExtra:
    
    """ THE CONSTRUCTOR OF THE CLASS PRINCESS EXTRA ONLY CONTAINS THE POSITION X AND THE POSITION Y OF THE DRAWING HELP!"""
    def __init__(self, helpX, helpY):
        self.__helpX = helpX
        self.__helpY = helpY


    @property
    def helpX(self):
        return self.__helpX
    
    @property
    def helpY(self):
        return self.__helpY
        