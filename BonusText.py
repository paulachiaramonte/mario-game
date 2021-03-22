class BonusText:
    
    """ THE CONSTRUCTOR OF THE CLASS BONUS TEXT CONTAINS THE POSITION X AND THE POSITION, PLUS A PREDEFINED VALUE OF BONUS"""
    def __init__(self, x, y):
        self.__posX = x
        self.__posY = y
        self.__bonus = 3100
    
    @property 
    def posX(self):
        return self.__posX
    
    @property 
    def posY(self):
        return self.__posY
    
    @property
    def bonus(self):
        return self.__bonus
    
    """THIS METHOD SUBSTRACTS 100 TO THE VALUE OF BONUS"""
    def updateBonus(self):
        if self.__bonus > 0: # THIS METHOD WORKS ONLY WHEN THE BONUS VALUE IS HIGHER THAN 0
            self.__bonus -= 100
    
    """ THIS METHOD RETURNS THE VALUE OF BONUS IN A STRING"""
    def stringBonus(self):
        return str(self.__bonus)
    
    """ THIS METHOD RESETS THE VALUE OF BONUS TO 3000 WHEN THE GAME IS OVER, MARIO IS TOUCHED BY A BARREL OR MARIO GETS TO THE TOP OF THE PLATFORM"""
    def reset(self):
        self.__bonus = 3000