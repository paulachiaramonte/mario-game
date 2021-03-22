import pyxel 
import random

from Mario import Mario
from DonkeyKong import DonkeyKong
from Princess import Princess
from Ladder import Ladder
from ScoreText import ScoreText
from Platform import Platform
from Barrel import Barrel
from StaticBarrel import StaticBarrel
from Extras import Oil
from BonusText import BonusText
from Extras import princessExtra

#CREATING THE CHARACTERS' OBJECTS WITH THEIR CLASS CONSTRUCTOR
player = Mario(40, 170)
donkey = DonkeyKong(35, 25)
princess = Princess(100, 5)

#CREATING THE SCORE AND THE BONUS OBJECTS
score = ScoreText(180, 5, 0)
bonus = BonusText(198, 20)

#CREATING THE STATIC BARRELS OBJECTS AND THE MAIN BARREL OBJECT, WHICH IS THE REFERENCE FOR CREATING THE OTHER BARRELS.
mainBarrel = Barrel(60, 46, 'east', 60)
staticBarrel1 = StaticBarrel(25, 40)
staticBarrel2 = StaticBarrel(25, 25)
staticBarrel3 = StaticBarrel(13, 40)
staticBarrel4 = StaticBarrel(13, 25)

#CREATING OBJECTS OF EXTRA DECORATIONS
oil = Oil(5, 170)
pExtra = princessExtra(116, 10)


#CREATING ALL THE LADDER WITH THE LADDER CLASS CONSTRUCTOR
ladder1_0 = Ladder(180, 146)
ladder1_1 = Ladder(180, 150)
ladder1_2 = Ladder(180, 155)
ladder1_3 = Ladder(180, 160)
ladder1_4 = Ladder(180, 165)
ladder1_5 = Ladder(180, 170)
ladder1_6 = Ladder(180, 175)
ladder1_7 = Ladder(180, 180)

ladder2_0 = Ladder(50, 98)
ladder2_1 = Ladder(50, 104)
ladder2_2 = Ladder(50, 110)
ladder2_3 = Ladder(50, 116)
ladder2_4 = Ladder(50, 122)
ladder2_5 = Ladder(50, 128)
ladder2_6 = Ladder(50, 134)
ladder2_7 = Ladder(50, 140)

ladder3_0 = Ladder(200, 56)
ladder3_1 = Ladder(200, 62)
ladder3_2 = Ladder(200, 68)
ladder3_3 = Ladder(200, 74)
ladder3_4 = Ladder(200, 80)
ladder3_5 = Ladder(200, 86)
ladder3_6 = Ladder(200, 92)
ladder3_7 = Ladder(200, 98)

ladder4_0 = Ladder(132, 26)
ladder4_1 = Ladder(132, 32)
ladder4_2 = Ladder(132, 38)
ladder4_3 = Ladder(132, 44)
ladder4_4 = Ladder(132, 50)


brokenLadder1_0 = Ladder(100, 180)
brokenLadder1_1 = Ladder(100, 175)
brokenLadder1_2 = Ladder(100, 155)
brokenLadder1_3 = Ladder(100, 150)

brokenLadder3_0 = Ladder(120, 98)
brokenLadder3_1 = Ladder(120, 92)
brokenLadder3_2 = Ladder(120, 62)
brokenLadder3_3 = Ladder(120, 56)

# CREATING A LIST (ladders) WITH ALL THE LADDERS, FOR ABLE TO DRAW THEM
ladders = [ladder1_0, ladder1_1, ladder1_2, ladder1_3, ladder1_4, ladder1_5, ladder1_6, ladder1_7, 
           ladder2_0, ladder2_1, ladder2_2, ladder2_3, ladder2_4, ladder2_5, ladder2_6, ladder2_7, 
           ladder3_0, ladder3_1, ladder3_2, ladder3_3, ladder3_4, ladder3_5, ladder3_6, ladder3_7, 
           ladder4_0, ladder4_1, ladder4_2, ladder4_3, ladder4_4, 
           brokenLadder1_0, brokenLadder1_1, brokenLadder1_2, brokenLadder1_3, 
           brokenLadder3_0, brokenLadder3_1, brokenLadder3_2, brokenLadder3_3]

ladder5 = Ladder(86, 50)
x = ladder5.posX
y = ladder5.posY
for i in range(10):
    ladder = Ladder(x, y)
    ladders.append(ladder)
    y -= 6

ladder6 = Ladder(70, 50)
x = ladder6.posX
y = ladder6.posY
for i in range(10):
    ladder = Ladder(x, y)
    ladders.append(ladder)
    y -= 6

# CREATING THE PLATFORMS AS OBJECTS WITH THE CLASS PLATFORM CONSTRUCTOR, AND APPENDING THEM TO A LIST (platforms), 
    #FOR ABLE TO DRAW THEM
platforms = []

platform1 = Platform(0, 186)
x = platform1.posX
for i in range(32):
    platform = Platform(x, 186)
    platforms.append(platform)
    x += 8

platform2 = Platform(0, ladder1_0.posY)
x = platform2.posX
y = platform2.posY
for i in range(26):
    platform = Platform(x, y)
    platforms.append(platform)
    x += 8
    
platform3 = Platform(20, ladder2_0.posY)
x = platform3.posX
y = platform3.posY
for i in range(30):
    platform = Platform(x, y)
    platforms.append(platform)
    x += 8

platform4 = Platform(0, ladder3_0.posY)
x = platform4.posX
y = platform4.posY
for i in range(27):
    platform = Platform(x, y)
    platforms.append(platform)
    x += 8
    
platform5 = Platform(100, ladder4_0.posY)
x = platform5.posX
y = platform5.posY
for i in range(5):
    platform = Platform(x, y)
    platforms.append(platform)
    x += 8

# creating variables for creating the conditions inside the update function
widthMin = 0
widthMax = 256

# creating a list that contains all the barrels' objects
barrels = []

def update():
    
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    
    # MARIO'S MOVEMENT:
    
    # LEFT OR RIGHT MOVEMENT:
    if (player.posY  == platform1.posY - 16 or player.posY == platform2.posY - 16
        or player.posY  == platform3.posY - 16 or player.posY == platform4.posY - 16):
        player.changeDown(False)
        player.changeUp(False)
        
        if player.posX <= widthMax -16 :
            if pyxel.btn(pyxel.KEY_RIGHT):
                        player.moveR() 

        if player.posX >= widthMin:
            if pyxel.btn(pyxel.KEY_LEFT):
                    player.moveL()
    
    # GRAVITY MOVEMENT:
    if player.posX > 205 and player.posY >= 128 and player.posY < 170:
        player.gravity()
    elif player.posX < 10 and player.posY >= 82 and player.posY < 129:
        player.gravity()
    elif player.posX > 210 and player.posY >= 40 and player.posY < 82:
        player.gravity()
    elif player.posX > 134 and player.posY >= 10 and player.posY < 40:
        player.gravity()
    elif player.posX < 90 and player.posY >= 10 and player.posY < 40:
        player.gravity()
        
    # JUMPING MOVEMENT:
    if player.jumping == False:
        if pyxel.btnp(pyxel.KEY_SPACE):
            if (player.posY  == platform1.posY - 16 or player.posY == platform2.posY - 16
        or player.posY  == platform3.posY - 16 or player.posY == platform4.posY - 16):
                player.whenSetter = pyxel.frame_count
                player.jump()
                player.changeGravity(False)
    
    if player.jumping == True and pyxel.frame_count - player.when == 8:
        player.desjump()
        player.changeGravity(True)
        
        

    # UP AN DOWN MOVEMENT:
    if player.posX >= ladder1_7.posX -5 and player.posX <= ladder1_7.posX + 5:
        if player.posY <= ladder1_7.posY + 6 and player.posY >= ladder1_0.posY - 15:
            if pyxel.btn(pyxel.KEY_UP):
                player.moveU()

        if player.posY <= ladder1_7.posY - 11 and player.posY >= ladder1_0.posY - 18:
            if pyxel.btn(pyxel.KEY_DOWN):
                player.moveD()

    
    if player.posX >= ladder2_7.posX -5 and player.posX <= ladder2_7.posX + 5:
        if player.posY <= ladder2_7.posY + 6 and player.posY >= ladder2_0.posY - 15:
            if pyxel.btn(pyxel.KEY_UP):
                player.moveU()
                player.changeUp(True)

        if player.posY <= ladder2_7.posY - 11 and player.posY >= ladder2_0.posY - 18:
            if pyxel.btn(pyxel.KEY_DOWN):
                player.moveD()
                player.changeDown(True)
 
    
    if player.posX >= ladder3_7.posX -5 and player.posX <= ladder3_7.posX + 5:
        if player.posY <= ladder3_7.posY + 6 and player.posY >= ladder3_0.posY - 15:
            if pyxel.btn(pyxel.KEY_UP):
                player.moveU()
                player.changeUp(True)

        if player.posY <= ladder3_7.posY - 17 and player.posY >= ladder3_0.posY - 18:
            if pyxel.btn(pyxel.KEY_DOWN):
                player.moveD()
                player.changeDown(True)

    
    if player.posX >= ladder4_4.posX -5 and player.posX <= ladder4_4.posX + 5:
        if player.posY <= ladder4_4.posY + 6 and player.posY >= ladder4_0.posY - 15:
            if pyxel.btn(pyxel.KEY_UP):
                player.moveU()
                player.changeUp(True)

        if player.posY <= ladder4_4.posY - 11 and player.posY >= ladder4_0.posY - 18:
            if pyxel.btn(pyxel.KEY_DOWN):
                player.moveD()
                player.changeDown(True)
    
    
    #BARRELS' MOVEMENT (creating the path of the barrels):
    
    if pyxel.frame_count % mainBarrel.velocity == 0:
        if len(barrels) <= 10:
            barrel = Barrel(mainBarrel.posX, mainBarrel.posY, 'east', mainBarrel.velocity)
            barrels.append(barrel)
            
    for barrel in barrels:
        if barrel.posX >= widthMin and barrel.posX <= widthMax:
            barrel.move()
            
            if barrel.posX == ladder3_0.posX and barrel.posY == 46:
                i = random.randint(1, 1000)
                if i >= 1 and i <= 250:
                    barrel.changeDirection('south')

            if barrel.posX == 216 and barrel.posY == 46:
                barrel.changeDirection('gravity')
            
            if barrel.posY + 10 == platform3.posY:
                barrel.changeDirection('west')
            
            if barrel.posX == ladder2_0.posX and barrel.posY + 10 == platform3.posY:
                i = random.randint(1,1000)
                if i >= 1 and i <= 250:
                    barrel.changeDirection('south')
            
            if barrel.posX == 8 and barrel.posY + 10 == platform3.posY:
                barrel.changeDirection('gravity')
            
            if barrel.posY + 10 == platform2.posY:
                barrel.changeDirection('east')
            
            if barrel.posX == ladder1_0.posX and barrel.posY + 10 == platform2.posY:
                i = random.randint(1, 1000)
                if i >= 1 and i <= 250:
                    barrel.changeDirection('south')
            
            if barrel.posX == 208 and barrel.posY + 10 == platform2.posY:
                barrel.changeDirection('gravity')
            
            if barrel.posY + 10 == platform1.posY:
                barrel.changeDirection('west')

        else:
            barrels.remove(barrel)
        
        
        # RESET GAME WHEN BARREL TOUCHES MARIO
        if abs(player.posX - barrel.posX) <= 6 and abs((player.posY + 6) - barrel.posY) < 5:
            pyxel.play(3, 3, loop = False)
            player.update()
            bonus.reset()
            barrels.clear()
            player.changeUp(False)
            player.changeDown(False)
            

        
        # POINTS FOR JUMPING THE BARREL
        elif player.posX == barrel.posX and player.jumping == True:
            if player.posY - barrel.posY < abs(20): 
                score.changeScore()
                pyxel.play(1, 1, loop=False)
                
                
            
    # END GAME WHEN THERE IS NO LIVES
    if player.lives == 0:
        barrels.clear()
        pyxel.stop(0)
        if score.highScore < (score.score):
                score.changeHighScore(score.score)
        if pyxel.btn(pyxel.KEY_R):
            score.reset()
            player.startOver()
            pyxel.play(0, 0, loop = True)

        
    # UPDATING THE BONUS SCORE EVERY 150 FRAMES
    if pyxel.frame_count % 150 == 0:
        bonus.updateBonus()
            
    # RESET GAME WHEN MARIO REACHES THE TOP
    if player.posY == 10:
        pyxel.play(2, 2, loop = False)
        score.addBonus(bonus.bonus)
        player.reset()
        bonus.reset()
        barrels.clear()
        
    
        
def draw():
    
    #IMAGES WHEN MARIO STILL HAS LIVES
    if player.lives != 0:
    
        if player.posX > 90 and player.posX < 135 and player.posY <= 10:
            pyxel.cls(pyxel.frame_count % 5)
        else:
            pyxel.cls(0)
    
        # DRAW LADDERS
        for ladder in ladders:
            pyxel.blt(ladder.posX, ladder.posY, 0, 0, 18, 8, 6, colkey = 0)
        
        # DRAW STATIC BARRELS
        pyxel.blt(staticBarrel1.posX, staticBarrel1.posY, 0, 12, 103, 12, 15, colkey = 0) #STATIC BARREL 1
        pyxel.blt(staticBarrel2.posX, staticBarrel2.posY, 0, 12, 103, 12, 15, colkey = 0) #STATIC BARREL 2
        pyxel.blt(staticBarrel3.posX, staticBarrel3.posY, 0, 12, 103, 12, 15, colkey = 0) #STATIC BARREL 3
        pyxel.blt(staticBarrel4.posX, staticBarrel4.posY, 0, 12, 103, 12, 15, colkey = 0) #STATIC BARREL 4
        
        #DRAW EXTRAS
        pyxel.blt(oil.posX, oil.posY, 0, 8, 0, 15, 16, colkey = 0) # OIL
        
        if player.posY == 40:
            pyxel.blt(pExtra.helpX, pExtra.helpY, 0, 158, 182, 22, 7, colkey = 0) # HELP!
        if player.posX == 40 and player.posY == 170:
            pyxel.blt(pExtra.helpX, pExtra.helpY, 0, 158, 182, 22, 7, colkey = 0) # HELP!
            
        
        # DRAW BONUS BOARD
        pyxel.blt(bonus.posX, bonus.posY, 0, 181, 100, 43, 19, colkey = 0)
        
        # DRAWING THE LIVES
        x = 4
        y = 14
        for lives in range(player.lives):
            pyxel.blt(x, y, 0, 131, 8, 6, 7, colkey = 0)
            x += 8
        
        #DRAW PRINCESS
        pyxel.blt(princess.posX, princess.posY, 0, 31, 179, 14, 21, colkey = 0) # PRINCESS
        
        
        # DRAW BARRELS
        for barrel in barrels:
    
            if barrel.direction == 'south':
                if pyxel.frame_count % 4 != 0:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 129, 106, 15, 10, colkey = 0)
    
                elif pyxel.frame_count % 4 == 0:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 153, 106, 15, 10, colkey = 0)
                    
            elif barrel.direction == 'east':
                
                barrel.animation()
                
                if barrel.image == 0:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 35, 106, 12, 12, colkey = 0)
                elif barrel.image == 1:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 59, 106, 12, 12, colkey = 0)
                elif barrel.image == 2:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 83, 106, 12, 12, colkey = 0)
                elif barrel.image == 3:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 107, 106, 12, 12, colkey = 0)
            
            elif barrel.direction == 'west':
                
                barrel.animation()
                if barrel.image == 0:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 107, 106, 12, 12, colkey = 0)
                elif barrel.image == 1:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 83, 106, 12, 12, colkey = 0)
                elif barrel.image == 2:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 59, 106, 12, 12, colkey = 0)
                elif barrel.image == 3:
                    pyxel.blt(barrel.posX, barrel.posY, 0, 35, 106, 12, 12, colkey = 0)
                            
                       
            elif barrel.direction == 'gravity':
                pyxel.blt(barrel.posX, barrel.posY, 0, 35, 106, 12, 12, colkey = 0)
        
        # DRAW PLATFORMS
        for platform in platforms:
            pyxel.blt(platform.posX, platform.posY, 0, 0, 8, 8, 8, colkey = 0)
            
        # DRAWING MARIO
        
        if player.jumping == True:
            if player.east == True:
                pyxel.blt(player.posX, player.posY, 0, 29, 32, -15, 16, colkey = 0)
            elif player.east == False:
                pyxel.blt(player.posX, player.posY, 0, 29, 32, 15, 16, colkey = 0)
        elif player.jumping == False:
            if player.up == True or player.down == True:
                if pyxel.btn(pyxel.KEY_UP):
                    player.animation()
                    if player.image == 0:
                        pyxel.blt(player.posX, player.posY, 0, 78, 32, 15, 16, colkey = 0)
                    elif player.image == 1:
                        pyxel.blt(player.posX, player.posY, 0, 78, 32, -15, 16, colkey = 0)
                
                elif pyxel.btn(pyxel.KEY_DOWN):
                    player.animation()
                    if player.image == 0:
                        pyxel.blt(player.posX, player.posY, 0, 78, 32, 15, 16, colkey = 0)
                    elif player.image == 1:
                        pyxel.blt(player.posX, player.posY, 0, 78, 32, -15, 16, colkey = 0)
                else:
                    pyxel.blt(player.posX, player.posY, 0, 78, 32, 15, 16, colkey = 0)
                
                
            else:
                if pyxel.btn(pyxel.KEY_RIGHT):
                    player.animation()
                    
                    if player.image == 0:
                        pyxel.blt(player.posX, player.posY, 0, 29, 32, -15, 16, colkey = 0)
                    elif player.image == 1:
                        pyxel.blt(player.posX, player.posY, 0, 53, 32, -15, 16, colkey = 0)
    
                elif pyxel.btn(pyxel.KEY_LEFT):
                    player.animation()
                    
                    if player.image == 0:
                        pyxel.blt(player.posX, player.posY, 0, 29, 32, 15, 16, colkey = 0)
                    elif player.image == 1:
                        pyxel.blt(player.posX, player.posY, 0, 53, 32, 15, 16, colkey = 0)
    
                else:
                    if player.east == True:
                        pyxel.blt(player.posX, player.posY, 0, 6, 32, -15, 16, colkey = 0)
                    elif player.east == False:
                        pyxel.blt(player.posX, player.posY, 0, 6, 32, 15, 16, colkey = 0)
                        
                    
    
            
                    
        # DRAWING DONKEY KONG
        
        if pyxel.frame_count - donkey.time >= 0 and pyxel.frame_count - donkey.time < 15:
                pyxel.blt(donkey.posX, donkey.posY, 0, 53, 58, -39, 31, colkey = 0)
            
        elif pyxel.frame_count - donkey.time >= 15 and pyxel.frame_count - donkey.time < 30:
                pyxel.blt(donkey.posX, donkey.posY, 0, 104, 58, 39, 31, colkey = 0)
            
        elif pyxel.frame_count - donkey.time >= 30 and pyxel.frame_count - donkey.time < 45:
                pyxel.blt(donkey.posX, donkey.posY, 0, 53, 58, 39, 31, colkey = 0)
            
        elif pyxel.frame_count - donkey.time >= 45 and pyxel.frame_count - donkey.time <= 60:
                pyxel.blt(donkey.posX, donkey.posY + 1, 0, 8, 213, 39, 31, colkey = 0)
                
        if pyxel.frame_count % 60 == 0:
            donkey.changeTime()
            
    
        
        # DRAW SCORE AND HIGH SCORE
        s = "SCORE {:>4}".format(score.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)
        
        h = "HIGH SCORE {:>4}".format(score.highScore)
        pyxel.text(185, 4, h, 1)
        pyxel.text(184, 4, h, 7)
        
        b = bonus.stringBonus()
        pyxel.text(212, 29, b, 7)
        
        pyxel.blt(100, 125, 0,170, 129, 80, 10, colkey = 0)
    
    elif player.lives == 0:
        pyxel.cls(0)
        pyxel.text(113, 20, 'GAME OVER', 7)
        donkey.animation()
        if donkey.image == 0:
            pyxel.blt(110, 30, 0, 150, 58, 45, 31, colkey = 0)
        elif donkey.image == 1:
            pyxel.blt(110, 30, 0, 150, 58, -45, 31, colkey = 0)
        
        pyxel.blt(0, 0, 0, 179, 133, 11, 8)
        
        pyxel.text(100, 80, "HIGH SCORE {:>4}".format(score.highScore), 8)
        pyxel.text(112, 70, "SCORE {:>4}".format(score.score), 8)
        pyxel.text(100, 100, 'PRESS Q TO QUIT', 7)
        pyxel.text(95, 120, 'PRESS R TO RESTART', 7)
        
        if pyxel.frame_count % 60 == 0:
            donkey.changeTime()
    

#FUNCTION WHICH CONTAINS THE BACKGROUND MUSIC
def play_music():
    pyxel.play(0, 0, loop = True)
        


HEIGHT = 200
WIDTH = 256
CAPTION = 'DONKEY KONG'

pyxel.init(WIDTH, HEIGHT, caption = CAPTION)

pyxel.load("assets/mario_donkey.pyxres")


# SOUND EFECTS CREATED WITH THE SOUND CLASS OF PYXEL
pyxel.sound(0).set("c1c1c1e1e1g1a1g1","t","4", "vffn", 20)

pyxel.sound(1).set('b3e4', 't', '6', 'vffn', 10)

pyxel.sound(2).set('d4g4', 't', '6', 'vffn', 10)

pyxel.sound(3).set('g#2 a2 a#2', 't', '6', 'vffn', 5)
           

play_music()

pyxel.run(update, draw)

