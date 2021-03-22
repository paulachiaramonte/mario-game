class Barrel:
    """ THE CONSTRUCTOR OF THE CLASS BARREL CONTAINS THE POSITION X, THE POSITION Y, THE DIRECTION OF THE BARREL AND THE VELOCITY OF THE BARREL"""
    def __init__(self, x, y, direction, velocity):
        self.__posX = x
        self.__posY = y
        self.__direction = direction 
        self.__velocity = velocity
        self.__time = 0 # USED FOR THE ANIMATION
        self.__image = 0 # USED FOR THE ANIMATION 
        self.__delay = 3 # USED FOR THE ANIMATION
    
    @property
    def posX(self):
        return self.__posX
    
    @property
    def posY(self):
        return self.__posY
    
    @property
    def direction(self):
        return self.__direction
    
    @property
    def velocity(self):
        return self.__velocity
    
    @property
    def time(self):
        return self.__time
    
    @property
    def image(self):
        return self.__image
    
    """ THIS METHOD CHANGES THE DIRECTION OF THE BARREL, BY ADDING THE DIRECTION IN THE VALUE VARIABLE OF THE FUNCTION """
    def changeDirection(self, value):
        self.__direction = value
    
    """ THIS METHOD MOVES THE BARREL, DEPENDING ON THE DIRECTION OF THE BARREL"""
    def move(self):
        if self.__direction == 'east': # IF THE DIRECTION IS EAST, THE METHOD WILL ADD 2 TO THE POSITION X
            self.__posX += 2
        elif self.__direction == 'west': # IF THE DIRECTION IS WEST, THE METHOD WILL SUBSTRACT 2 TO THE POSITION X 
            self.__posX -= 2
        elif self.__direction == 'south': # IF THE POSITION IS SOUTH, THE METHOD WILL ADD 2 TO THE POSITION Y
            self.__posY += 2
        elif self.__direction == 'gravity': # IF THE POSITION IS GRAVITY, THE METHOD WILL ADD 2 TO THE POSITION Y
            self.__posY += 2
                                            #THE DIFFERENCE IN SOUTH AND GRAVITY IS IN THE ANIMATION, BECAUSE BOTH DIRECTIONS HAVE DIFFERENT IMAGES
    
    """ THIS METHOD SIMULATES THE ANIMATION OF THE BARRELS, BY DOING SOME SORT OF A CYCLE THAT CHANGES THE IMAGES OF THE ROLLING OF THE BARRELS """
    def animation(self):
        self.__time += 1 # THIS INCREASES EVERY FRAME COUNT
        
        if self.__time > self.__delay: # TO SIMULATE A MORE NATURAL MOVEMENT, WE MAKE THE IMAGES CHANGE EVERY NUMBER OF FRAMES RATHER THAN IN EVERY FRAME BY USING THE DELAY PARAMETER
            self.__time = 0
            self.__image += 1 # CHNAGES TO THE NEXT IMAGE
            if self.__image > 3: # THIS CREATES THE CYCLE OF IMAGES. BECAUSE THE BARRELS' MOVEMENT DEPEND ON FOUR IMAGES, THE PARAMETER IMAGE WILL CHANGE THE VALUES FROM 0 TO 3
                self.__image = 0
