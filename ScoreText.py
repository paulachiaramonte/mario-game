class ScoreText:
    
    """ THE CONSTRUCTOR OF THE CLASS SCORE TEXT CONTAINS THE POSITION X, THE POSITION Y AND THE SCORE, PLUS A PREDEFINED VALUE OF HIGH SCORE"""
    def __init__(self, x, y, score):
        self.__posX = x
        self.__posY = y
        self.__score = score
        self.__highScore = 0
        
    
    @property
    def posX(self):
        return self.__posX
    
    @property
    def posY(self):
        return self.__posY

    @property
    def score(self):
        return self.__score
    
    @property
    def highScore(self):
        return self.__highScore
    
    """THIS METHODS CHANGES THE VALUE OF SCORE BY ADDING IT 100"""
    def changeScore(self):
        self.__score += 100

    """ THIS METHODS CHANGES THE HIGH SCORE"""
    def changeHighScore(self, value):
        self.__highScore = value
    
    """ THIS METHOD ADDS TO THE SCORE A VALUE, WHICH IN THE GAME WILL BE THE BONUS"""
    def addBonus(self, value):
        self.__score += value
    
    """ THIS METHOD RESETS THE VALUE OF SCORE TO 0. WE USE IT WHEN THE GAME IS OVER"""
    def reset(self):
        self.__score = 0