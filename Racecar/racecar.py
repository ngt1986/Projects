import pygame, time, sys, random
from pygame.locals import *
from PIL import Image

pygame.init()
display_width = 800
display_height = 600

startbutton_width = 100
startbutton_height = 50
startbutton_pos=[display_width*(1/4)-startbutton_width/2,display_height*(3/4)]

quitbutton_width = 100
quitbutton_height = 50
quitbutton_pos=[display_width*(3/4)-quitbutton_width/2,display_height*(3/4)]

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0, 0, 255)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Racecar game')
clock = pygame.time.Clock()

carImg=pygame.image.load('car.png')
def things_dodged(count):
    font= pygame.font.SysFont(None, 25)
    text= font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0)
                     )
def getCarDims(): #using PIL import above
    im = Image.open('car.png')
    car_width=im.size[0] #.size from PIL
    car_height=im.size[1] #.size from PIL
    return car_width, car_height

car_width = getCarDims()[0]
car_height = getCarDims()[1]
car_speed = 10



def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color, [thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText, red)
    TextRect.center = ((display_width/2),(display_height)/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You crashed!')
    
#message, x pos, y pos, width, height, inactive color, active color, action (e.g., play, quit...)
def button(msg,x,y,w,h,inactive_color,active_color,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,w,h))
        if click[0] and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg,smallText,black)
    textRect.center = ((x+w/2),(y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',95)
        TextSurf, TextRect = text_objects("Racecar Game", largeText,blue)
        TextRect.center = ((display_width/2),(display_height)/2)
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",startbutton_pos[0],startbutton_pos[1],100,50,green, bright_green,game_loop)
        button("QUIT",quitbutton_pos[0],quitbutton_pos[1],100,50,red, bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)
        

def game_loop():
    x = (display_width*0.45)
    y = (display_height*0.8)

    x_change=0


    #initial values
    thing_x=random.randrange(0,display_width)
    thing_y=-600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    dodged = 0
    
    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit= True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                x_change=-car_speed
            else:
                if keys[pygame.K_RIGHT]:
                    x_change=car_speed
                else:
                    x_change=0
                    
##            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_LEFT:
##                    x_change +=-5
##                if event.key == pygame.K_RIGHT:
##                    x_change += 5
##            if event.type == pygame.KEYUP:
##                if event.key == pygame.K_LEFT:
##                    x_change += 5
##                if event.key == pygame.K_RIGHT:
##                    x_change += -5

        x += x_change
        gameDisplay.fill(white)

        #things(thingx,thingy,thingw,thingh,color):
        things(thing_x, thing_y, thing_width,thing_height, red)
        thing_y += thing_speed
        car(x,y)
        things_dodged(dodged)
        
        if x > display_width - car_width or x < 0:
            crash()
        
        if thing_y > display_height: #if block is below bottom of screen
            thing_y = 0 - thing_height
            thing_x = random.randrange(0,display_width)
            dodged += 1
            thing_speed+=1
            thing_width += (dodged*1.2)
            
        if y < thing_y + thing_height:
            if y+car_height > thing_y:
                if ((x > thing_x) and (x < thing_x + thing_width)) or (x+car_width > thing_x and x + car_width < thing_x + thing_width):
                    crash()
                    
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
