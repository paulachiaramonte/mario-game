
class Mario:
    
    """THE CONTRUCTOR OF THE CLASS MARIO CONTAINS THE POSITION OF THE OBJECT (posX and posY) PLUS SOME PRE DEFINED PARAMETERS"""
    def __init__(self, x, y):
        self.__posX = x
        self.__posY = y
        self.__east = True # SHOWS THE DIRECTION OF THE PLAYER, IF IT IS GOING TO THE RIGHT IS True, IF IT IS GOING TO THE LEFT IS False
        self.__when = 0 # THIS IS SOME SORT OF A TIMER, THAT ALLOWS THE MARIO OBJECT TO JUMP AND GOING DOWN IN AN AMOUNT OF TIME
        self.__jumping = False # SHOWS IF THE PLAYER IS JUMPING OR NOT
        self.__gravity = True # ACTIVATES (True) AND DESACTIVATES THE GRAVITY (False)
        self.__up = False # SHOWS IF IT IS GOING UP USING THE LADDER
        self.__down = False # SHOW IF IT IS GOING DOWN USING THE LADDER
        self.__lives = 3 # COINTAINS THE AMOUNT OF LIVES OF MARIO
        self.__time = 0 # USED FOR THE ANIMATION
        self.__delay = 5 # USED FOR THE ANIMATION
        self.__image = 0 # USED FOR THE ANIMATION
    
    @property
    def posX(self):
        return self.__posX

    @property
    def posY(self):
        return self.__posY
    
    @property
    def when(self):
        return self.__when
    
    @when.setter
    def whenSetter(self, value):
        self.__when = value
    
    @property
    def jumping(self):
        return self.__jumping
    
    @property 
    def east(self):
        return self.__east
    
    @property
    def up(self):
        return self.__up
    
    @property 
    def down(self):
        return self.__down
    
    @property
    def lives(self):
        return self.__lives
    
    @property 
    def image(self):
        return self.__image

    """ THIS METHOD MOVES THE PLAYER TO THE RIGHT, BY ADDING 2 TO THE POSITION X"""
    def moveR(self):
        self.__posX += 2
        self.__east = True # CHANGES THE DIRECTION 
        self.__down = False # CHANGES THE PARAMETER OF GOING DOWN TO FALSE
        self.__up = False # CHANGES THE PARAMETER OF GOING UP TO FALSE

    """ THIS METHOD MOVES THE PLAYER TO THE LEFT, BY SUBSTRACTING 2 TO THE POSITION X """
    def moveL(self):
        self.__posX -= 2
        self.__east = False # CHANGES THE DIRECTION
        self.__down = False # CHANGES THE PARAMETER OF GOING DOWN TO FALSE
        self.__up = False # CHANGES THE PARAMETER OF GOING UP TO FALSE
        
    """ THIS METHOD MOVES THE PLAYER UP, BY SUBSTRACTING 1 TO THE POSITION Y """
    def moveU(self):
        self.__posY -= 1
        self.__up = True # CHANGES THE PARAMETER OF GOING UP TO TRUE
    
    """ THIS METHOD MOVES THE PLAYER DOWN, BY ADDING 1 TO THE POSITION Y """
    def moveD(self):
        self.__posY += 1
        self.__down = True # CHANGES THE PARAMETER OF GOING DOWN TO TRUE
    
    """ THIS METHOD MAKES THE PLAYER GO UP, SIMULATING A JUMP """
    def jump(self):
        self.__posY -= 14
        if self.__east == True: # DEPENDING ON THE DIRECTION OF THE PLAYER:
            self.__posX += 8 ### THE METHOD ADDED 8 TO THE POSITION X IF IT WAS GOING TO THE RIGHT
        elif self.__east == False:
            self.__posX -= 8 ### THE METHOD SUBSTRACTED 8 TO THE POSITION X IF IT WAS GOING TO THE LEFT
        self.__jumping = True # CHANGES THIS PARAMETER TO TRUE
        self.__down = False # CHANGES THE PARAMETER OF GOING DOWN TO FALSE
        self.__up = False # CHANGES THE PARAMETER OF GOING UP TO FALSE
    
    """ THIS METHOD MAKES THE PLAYER GOING DOWN AFTER THE JUMP """
    def desjump(self):
        self.__posY += 14 # RETURNED THE PLAYER DOWN BY ADDING WHAT WAS SUBSTRACTED IN THE JUMP METHOD
        if self.__east == True:
            self.__posX += 8
        elif self.__east == False:
            self.__posX -= 8
        self.__jumping = False
        self.__down = False
        self.__up = False
        
    """ THIS METHOD CHANGES THE VALUE OF GRAVITY"""
    def changeGravity(self, value):
        self.__gravity = value
    
    """ THIS METHOD CHANGES THE VALUE OF UP """
    def changeUp(self, value):
        self.__up = value
    
    """ THIS METHOD CHANGES THE VALUE OF DOWN"""
    def changeDown(self, value):
        self.__down = value
    
    """ THIS METHOD SIMULATES THE GRAVITY, BY ADDIND 2 TO THE POSITION Y """
    def gravity(self):
        if self.__gravity == True: # IT IS ACTIVATED ONLY WHEN THE VALUE OF THE PARAMTER gravity IS TRUE
            self.__posY += 2        
            
    """ THIS METHOD IS USED WHEN MARIO TOUCHES A BARREL """
    def update(self):
        self.__lives -= 1 # TAKES ONE LIFE FROM THE PLAYER
        self.__posX = 40 # RETURNS THE MARIO TO ITS ORIGINAL POSITION 
        self.__posY = 170
    
    """ THIS METHOD IS USED WHEN MARIO GETS TO PRINCESS' PLATFORM, AND THE GAMES STARTS ALL OVER AGAIN"""
    def reset(self):
        self.__posX = 40 # RETURNS MARIO TO HIS ORIGINAL POSITION
        self.__posY = 170
        self.__up = False # BECAUSE MARIO ENDS THE GAME CLIMBING UP THE LADDER, WE HAVE TO SET THOSE VALUES TO FALSE AGAIN
        self.__down = False
        
    """ THIS METHOD IS USED WHEN THE GAME IS OVER, AND THE PLAYER WANTS TO PLAY AGAIN"""
    def startOver(self):
        self.__posX = 40 # MARIO RETURNS TO HIS ORIGIANL POSITION
        self.__posY = 170
        self.__lives = 3 # STARTS THE GAME WITH ALL OF HIS LIVES
    
    """ THIS METHOD SIMULATES THE ANIMATION OF MARIO, BY DOING SOME SORT OF A CYCLE THAT CHANGES THE IMAGES OF MARIO """
    def animation(self):
        self.__time += 1 # THIS INCREASES EVERY FRAME COUNT
        
        if self.__time > self.__delay: # TO SIMULATE A MORE NATURAL MOVEMENT, WE MAKE THE IMAGES CHANGE EVERY NUMBER OF FRAMES RATHER THAN IN EVERY FRAME BY USING THE DELAY PARAMETER
            self.__time = 0
            self.__image += 1 # CHANGES TO THE NEXT IMAGE
            if self.__image > 1: # THIS CREATES THE CYCLE OF IMAGES. BECAUSE MARIO'S MOVEMENT DEPEND ON ONLY TWO IMAGES, THE PARAMETER IMAGE WILL ONLY HAVE THE VALUES 0 OR 1.
                self.__image = 0
    


    

        

        
            
        
        
        
        