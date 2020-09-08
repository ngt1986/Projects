import pygame, time, sys, random
from pygame.locals import *
from PIL import Image

pygame.init()

#sounds/music
crash_sound  = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("Powerup.wav")

#window size
display_width = 1200
display_height = 1000


startbutton_width = 100
startbutton_height = 50
startbutton_pos=[display_width*(1/4)-startbutton_width/2,display_height*(3/4)]

quitbutton_width = 100
quitbutton_height = 50
quitbutton_pos=[display_width*(3/4)-quitbutton_width/2,display_height*(3/4)]

#colors
black = (0,0,0)
white = (255,255,255)
red = (155,0,0)
bright_red = (255,0,0)
green = (0,155,0)
bright_green = (0,255,0)
blue = (0, 0, 155)
bright_blue = (0, 0, 255)
yellow = (155, 155, 0)
bright_yellow = (255, 255, 0)
gray = (130,130,130)
#rand = (x,y,z)
easy, medium, hard = 1,2,3
pause = False

DISPLAYSURF = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('DODGER')
gameicon=pygame.image.load('D.png')
pygame.display.set_icon(gameicon)

face_up = pygame.image.load('up.png')
face_left = pygame.image.load('left.png')
face_right = pygame.image.load('right.png')
face_down = pygame.image.load('down.png')
face_upleft = pygame.image.load('upleft.png')
face_downleft = pygame.image.load('downleft.png')
face_upright = pygame.image.load('upright.png')
face_downright = pygame.image.load('downright.png')

clock = pygame.time.Clock()

def getPlayerDims(): #using PIL import
    im = Image.open('down.png')
    player_width=im.size[0]
    player_height = im.size[1]
    return player_width,player_height
    
def score(elapsed_time):
    font = pygame.font.SysFont("oomicsansms",25)
    text = font.render("Score: " + str(elapsed_time), True, white)
    DISPLAYSURF.blit(text, (2,2))

class Player():

    def __init__(self):
        self.width=getPlayerDims()[0] #using PIL import
        self.height =getPlayerDims()[1]
        self.x=display_width/2-self.width/2
        self.y=display_height/2-self.height/2
        self.speed = 8
        self.delta_x = 0
        self.delta_y = 0
        self.direction = face_down

#PLAYER
    def update(self):
        #raw_keys = pygame.key.get_pressed()
            #up, down, right, left
            #keys = [raw_keys[273],raw_keys[274],raw_keys[275],raw_keys[276]]
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.delta_x = -self.speed
            self.delta_y = 0
            self.direction = face_left
            if keys[pygame.K_DOWN]:
                self.delta_y = self.speed
                self.direction = face_downleft
            elif keys[pygame.K_UP]:
                self.delta_y = -self.speed
                self.direction = face_upleft
            
        elif keys[pygame.K_RIGHT]:
            self.delta_x = self.speed
            self.delta_y = 0
            self.direction = face_right
            if keys[pygame.K_DOWN]:
                self.delta_y = self.speed
                self.direction = face_downright
            elif keys[pygame.K_UP]:
                self.delta_y = -self.speed
                self.direction = face_upright
                
        elif keys[pygame.K_DOWN]:
            self.delta_x = 0
            self.delta_y = self.speed
            self.direction = face_down
            
        elif keys[pygame.K_UP]:
            self.delta_x = 0
            self.delta_y = -self.speed
            self.direction = face_up

        else:
            self.delta_x=0
            self.delta_y=0

        self.x += self.delta_x
        self.y += self.delta_y
        
    def draw(self,DISPLAYSURF):
        
        if self.direction == face_up:
            DISPLAYSURF.blit(face_up, (self.x,self.y))
        if self.direction == face_down:
            DISPLAYSURF.blit(face_down, (self.x,self.y))
        if self.direction == face_left:
            DISPLAYSURF.blit(face_left, (self.x,self.y))
        if self.direction == face_right:
            DISPLAYSURF.blit(face_right, (self.x,self.y))
        #diagonals
        if self.direction == face_upright:
            DISPLAYSURF.blit(face_upright, (self.x,self.y))
        if self.direction == face_downright:
            DISPLAYSURF.blit(face_downright, (self.x,self.y))
        if self.direction == face_upleft:
            DISPLAYSURF.blit(face_upleft, (self.x,self.y))
        if self.direction == face_downleft:
            DISPLAYSURF.blit(face_downleft, (self.x,self.y))

#ENEMY
class Enemy():
    
    def __init__(self):
        #1=top,2=right,3=bot,4=left

        self.dir = random.randrange(1,5)
        self.speed=random.randrange(5,15)
        self.width = random.randrange(25,50)
        self.color=bright_red
        
        if self.dir == 1:
            self.x = random.randrange(0,display_width-self.width)
            self.y = 0-self.width
        elif self.dir == 3:
            self.x = random.randrange(0,display_width-self.width)
            self.y = display_height
        elif self.dir == 2:
            self.x = display_width
            self.y = random.randrange(0,display_height-self.width)
        elif self.dir == 4:
            self.x = 0-self.width
            self.y = random.randrange(0,display_height-self.width)


    def update(self):
        #1=down, 2=left, 3=up, 4=right
        if self.dir == 1:
            self.y+= self.speed
        elif self.dir == 2:
            self.x+= -self.speed
        elif self.dir == 3:
            self.y+= -self.speed
        elif self.dir == 4:
            self.x+= self.speed

    def draw(self,DISPLAYSURF):
        pygame.draw.rect(DISPLAYSURF,self.color,[self.x,self.y,self.width,self.width])

def paused():
    global pause
    pygame.mixer.music.pause()
    DISPLAYSURF.fill(black)
    largeText = pygame.font.SysFont("comicsansms",95,white)
    TextSurf, TextRect = text_objects("Paused", largeText,blue)
    TextRect.center = ((display_width/2),(display_height)/2)
    DISPLAYSURF.blit(TextSurf, TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    pygame.mixer.music.unpause()

               
        button("Resume",startbutton_pos[0],startbutton_pos[1],100,50,green, bright_green,unpaused,None)
        button("QUIT",quitbutton_pos[0],quitbutton_pos[1],100,50,red, bright_red,quitgame,None)
        
        pygame.display.update()
        clock.tick(15)
        
def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    
def crash(elapsed_time):
    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(crash_sound)
    
    #play again text
    font = pygame.font.SysFont("oomicsansms",25)
    text = font.render("Click or Press P to play again... ", True, white)
    DISPLAYSURF.blit(text, (startbutton_pos[0]-100,startbutton_pos[1]+70))

    #you crashed text
    largeText = pygame.font.SysFont("comicsansms",95,white)
    TextSurf, TextRect = text_objects("You Crashed!", largeText,blue)
    TextRect.center = ((display_width/2),(display_height)/2)
    DISPLAYSURF.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_intro()
                       
        button("Play Again",startbutton_pos[0],startbutton_pos[1],100,50,green, bright_green,game_intro,None)
        button("QUIT",quitbutton_pos[0],quitbutton_pos[1],100,50,red, bright_red,quitgame,None)
        score(elapsed_time)
        pygame.display.update()
        clock.tick(15)
    

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,inactive_color,active_color,action,difficulty):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #if mouse is over button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF,active_color,(x,y,w,h))
        if click[0] and (action != None):
            if difficulty == easy:
                action(easy)
            elif difficulty == medium:
                action(medium)
            elif difficulty == hard:
                action(hard)    
            elif difficulty == None:
                action()
    #if mouse not over button      
    else:
        pygame.draw.rect(DISPLAYSURF, inactive_color, (x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg,smallText,black)
    textRect.center = ((x+w/2),(y+(h/2)))
    DISPLAYSURF.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()
    

def game_intro():
    pygame.mixer.music.play(-1)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    main_loop(easy)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    main_loop(medium)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    main_loop(hard)
                    
        DISPLAYSURF.fill(black)
        #play again text
        font = pygame.font.SysFont("oomicsansms",25)
        text = font.render("Click or Press 'e' for easy...", True, gray)
        DISPLAYSURF.blit(text, (display_width/2-100,display_height/3+165))
        font = pygame.font.SysFont("oomicsansms",25)
        text = font.render("Click or Press 'm' for medium...", True, gray)
        DISPLAYSURF.blit(text, (display_width/2-100,display_height/3+275))
        font = pygame.font.SysFont("oomicsansms",25)
        text = font.render("Click or Press 'h' for hard...", True, gray)
        DISPLAYSURF.blit(text, (display_width/2-100,display_height/3+385))
        
        largeText = pygame.font.SysFont("comicsansms",155)
        TextSurf, TextRect = text_objects("Dodger", largeText,blue)
        TextRect.center = ((display_width/2),(display_height)/5)
        DISPLAYSURF.blit(TextSurf, TextRect)

        button("Easy",display_width/2-50,display_height/3+110,100,50,green, bright_green,main_loop,easy)
        button("Medium",display_width/2-50,display_height/3 + 220,100,50,yellow, bright_yellow,main_loop,medium)
        button("Hard",display_width/2-50,display_height/3 + 330,100,50,red, bright_red,main_loop,hard)
        button("Quit",display_width/2-50,display_height/3 + 440,100,50,blue, bright_blue,quitgame,None)

        #add E,M,H underlined and starts game, Q for QUIT
        #add message at bottom of screen saying above
        #and add messaged at bottom saying press p to pause

        pygame.display.update()
        clock.tick(15)

#0=x , 1=y , 2=width, 3=height
def collision(enemy,player):
    if player.x + player.width > enemy.x > player.x  and player.y + player.width > enemy.y > player.y:
        return True
    elif player.x + player.width > enemy.x + enemy.width > player.x  and player.y + player.width > enemy.y > player.y:
        return True
    elif player.x + player.width > enemy.x > player.x  and player.y + player.width > enemy.y+enemy.width > player.y:
        return True
    elif player.x + player.width > enemy.x + enemy.width > player.x  and player.y + player.width > enemy.y + enemy.width> player.y:
        return True

#MAIN
def main_loop(difficulty):
    pygame.mixer.music.unpause()
    player=Player()
    enemies=[]
    enemy_color = red
    
    elapsed_time = 0
    gameExit = False
    global pause
    
    while not gameExit:
        #game timer / score
        elapsed_time +=1
        
       #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
              
        DISPLAYSURF.fill(black)

        #update/draw player position
        player.update()
        player.draw(DISPLAYSURF)

        #check for player out of bounds
        if player.x - player.width > display_width or player.x < 0 or player.y < 0 or player.y-player.width > display_height:
            crash(elapsed_time)
        
        #spawn enemy every 25 frames
        if difficulty == easy:
            if elapsed_time % 25 == 0:
                enemies.append(Enemy())
        elif difficulty == medium:
            if elapsed_time %12 == 0:
                enemies.append(Enemy())
        elif difficulty == hard:
            if elapsed_time %6 == 0:
                enemies.append(Enemy())
        #check for enemy out of bounds (and remove if so)
        for enemy in enemies:
            if enemy.x < 0-enemy.width or enemy.x > display_width or enemy.y < 0-enemy.width or enemy.y > display_height:
                enemies.remove(enemy)
        #print(len(enemies))
        
        #update enemy positions    
        for enemy in enemies:
            enemy.update()
        #draw enemy positions
        for enemy in enemies:
            enemy.draw(DISPLAYSURF)
            
        #check for collision
        for enemy in enemies:
            if collision(enemy,player):
                crash(elapsed_time)
                


        print           
        score(elapsed_time)
        pygame.display.update()
        clock.tick(60)

game_intro()
pygame.quit()
quit()
