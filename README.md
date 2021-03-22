# mario-game
Project in which I recreated a simpler version of the arcade game Donkey Kong using 'Pyxel' a game engine for Python. 
Final project for the Programming course at the my university

For able to play the game Pyxel must be installed https://github.com/kitao/pyxel

# Functionality of the game 

When the game is initialized, Donkey Kong starts right away throwing the barrels down the platforms, and Mario is allowed to move from right to left and jump only when he is standing on the platform, and up and down when he is in front of a functional ladder. Also, when he reaches the end of a platform, he can go down to the platform below, without needing to use a ladder. When a barrel approaches Mario, he has to jump the barrel, and if he does the player gets one point. Else, if the player touches a barrel, he loses a life and restarts the game from the start point and all the barrels in the board disappear. These barrels can go down at the end of the platform, and they also have a 25% chance of going down a functional ladder.

The goal of Mario is to reach the highest platform and climb the ladder to the Princess’ platform. When he reaches this platform, the game starts all over again, Mario goes back to his start point, and the bonus score accumulated is added to the current score. When Mario loses all his lives, the game finishes and the screen shows ‘Game Over’, accompanied by an animated Donkey Kong celebrating his victory, and the score in the previous game and the highest score achieved by the player all of the times he has played. We added another functionality, which is if the player presses the letter R, the game starts all over again, the score is set to zero, the high score is kept and he gets back all of his lives. 

# Classes Design
To develop the game I created 11 private classes: 

### Mario: 
Class that creates the object controlled by the user in the game. This class contains a constructor that receives only the position X and the position Y of the object, and it also has some private predefined parameters used for the functionality of the class’ methods. 
### Barrel:
Class that creates the obstacles the player has to avoid in the game. This class contains a constructor that receives position X, the position Y, the direction and the velocity parameters, and it also has some private predefined parameters
### Donkey Kong 
Class that contains a constructor that receives only the position X and the position Y of the Donkey Kong object and includes some predefined private parameters used for the method of animation. 
### Score
Class that displays the score accumulated by the player during the game. It contains a constructor that receives the parameters of position X, position Y, and the score, and contains a private predefined parameter of the high score.
### Bonus
The bonus class displays the points that the player will receive when Mario gets to the princess’s platform. It contains a constructor that receives only the position X and position Y, and it has a private predefined parameter with the value of Bonus. 
### Ladders, Platforms, Princess, Static Barrel, Oil and Princess Extras:
All of these classes are static images in the game, so they only have a constructor that receives only two parameters, the position X and the position Y. The main purpose of the objects of these classes is to be drawn in the main program. 


# Most relevant methods used
The most significant methods used in all the classes are the ones related to the movement of the objects, the animation of them and the updating and resetting the values of each object. Each class has their methods that make the development of the game possible. 

**Methods for the Mario Class**

The ***moveR***, ***moveL***, ***moveU***, ***moveD*** change the values of the position of X and the position of Y of the Mario object, to make it move. moveR increases the value of x by 2, and moveL decreases the value of x by 2. On the other side, moveU decreases the value of y by 1, and moveD increases the value of y of the player by 1. 

The ***jump*** method decreases the value of y by 14 and increases or decreases the value of x of Mario by 8, depending on the direction of the player. This jump method is followed by a ***desjump***, which after the player has jumped, the value of y is increased by 14, for able to return the player to the y position where it had earlier jumped. On the other hand, the gravity method increases the value of the position y, simulating a falling. 

The ***update*** method takes one life from the player and returns the player to Mario’s initial position. The ***reset*** only returns the player to Mario’s initial position. The ***startOver*** method returns all the lives to Mario and returns to the starting method. The first method is used when Mario is touched by a barrel, the second one when Mario reaches the top of the platform and finishes the game and the third one is used when Mario loses all his lives and the player wants to play again. 

**Methods for Barrel Class**

The move method of Barrel has conditions that use the direction property of the class. When then barrel direction is equal to ‘east’, the method increases the value of x; when the barrel direction is equal to ‘west’, the method decreases the value of x, both to simulate the movement to the right and the left. Additionally, when the barrel’s direction is equal to ‘south’ or ‘gravity’, the value of y of the barrel is decreased. The first one is used for going down the ladders, and the second one is to go down at the end of the platform. Another method used by the Barrel class is the changeDirection method, which receives a value and changes the parameter of direction to this value.

**Methods for ScoreText and BonusText class**

The ScoreText has ***changeScore*** function, which adds 100 to the score, and also has the ***reset*** method, which defines the value of score to 0. This first method is used when Mario jumps a barrel and the second one when the game is over. 

In the BonusText class, the significant methods are the ***updateBonus*** function, which decreases the value of bonus by 100, and the ***reset*** method, which defines the value of bonus to its original value, which is 3000. This first method is activated every certain amount of time, and the second one is used when Mario loses a life, he gets to the princess’ platform or the game is over.

**Methods for Animation**

For the animation methods in the classes of Mario, Barrel, and DonkeyKong, the method ***animation*** method is used with the parameters time, delay and image from the class. This method increases the time, with the intention that the time will increase in each frame. The parameter delay stores the number of frames we want the object to skip before changing to another image, and the parameter image stores the number of images the object will change repeatedly. In the method, when the time is higher the delay, the time is returned to 0 and the parameter image is increased by one. Additionally, inside the method, when the image is higher than the number of images that the objects change to, the parameter image is set to 0. What this method does is changing the image of the object every certain amount of time, which is defined by the delay parameter, and creating a cycle to simulate the movement of the characters in the game. 


