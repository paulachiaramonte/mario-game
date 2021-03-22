class DonkeyKong:
    
    """ THE CONSTRUCTOR OF THIS CLASS CONTAINS THE POSITION X (posX) AND THE POSITION Y (posY) PLUS SOME PRE DEFINED PARAMETERS"""
    def __init__(self, x, y):
        self.__posX = x
        self.__posY = y
        self.__time = -60 # USED FOR THE MOVEMENT OF DONKEYKONG THROWING THE BARRELS
        self.__delay = 5  # USED FOR THE ANIMATION
        self.__image = 0 # USED FOR THE ANIMATION
        self.__timer = 0 # USED FOR THE ANIMATION
    
    @property
    def posX(self):
        return self.__posX
    
    @property
    def posY(self):
        return self.__posY
    
    @property 
    def time(self):
        return self.__time
    
    @property
    def image(self):
        return self.__image
    
    """ THIS METHOD CHANGES THE VALUE OF TIME 60, BECAUSE WE WANT THAT THE TIME IS EQUAL TO THE PYXEL FRAME COUNT EVERY TIME A BARREL IS THROWN"""
    def changeTime(self):
        self.__time += 60
        
    """ THIS METHOD SIMULATES THE ANIMATION OF DONKEY KONG AT THE GAME OVER SCREEN, BY DOING SOME SORT OF A CYCLE THAT CHANGES THE IMAGES OF DONKEY KONG """
    def animation(self):
        self.__timer += 1 # THIS INCREASES EVERY FRAME COUNT
        
        if self.__timer > self.__delay: # TO SIMULATE A MORE NATURAL MOVEMENT, WE MAKE THE IMAGES CHANGE EVERY NUMBER OF FRAMES RATHER THAN IN EVERY FRAME BY USING THE DELAY PARAMETER
            self.__timer = 0
            self.__image += 1 # CHANGES TO THE NEXT IMAGE
            if self.__image > 1: # THIS CREATES THE CYCLE OF IMAGES. BECAUSE DONKEY KONG'S MOVEMENT DEPEND ON ONLY TWO IMAGES, THE PARAMETER IMAGE WILL ONLY HAVE THE VALUES 0 OR 1.
                self.__image = 0 
        