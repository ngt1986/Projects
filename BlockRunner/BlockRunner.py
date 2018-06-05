#Block Runner
#Nick Thomas

import pygame, sys, random
from pygame.locals import *

BOARDWIDTH = 20
BOARDHEIGHT = 20
TILESIZE = 20
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
FPS = 30

#R G B
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)
GOLD = (232,226,44)
RED = (204,0,0)
GRAY = (192,192,192)
DARKTURQUOISE = (3, 54, 73)

BGCOLOR = DARKTURQUOISE
PLAYERCOLOR = BLUE
ENEMYCOLOR = RED
COINCOLOR = GOLD
TILECOLOR = GRAY
TEXTCOLOR = WHITE
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE*BOARDWIDTH+(BOARDWIDTH-1)))/2)
YMARGIN = int((WINDOWHEIGHT -(TILESIZE*BOARDHEIGHT+(BOARDHEIGHT-1)))/2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK,DISPLAYSURF, BASICFONT, PLAYAGAIN_SURF, QUIT_SURF

    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Block Runner')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    #store the 'play again' and 'quit' buttons and their rectangles
    PLAYAGAIN_SURF = makeText('Play Again?', TEXTCOLOR,TILECOLOR, WINDOWWIDTH/4, WINDOWHEIGHT/4)
    QUIT_SURF = makeText('QUIT?',TEXTCOLOR,TILECOLOR, WINDOWWIDTH*(3/4), WINDOWHEIGHT/4)

    while True: #main game loop
        moveTo=None

        #che

        drawGrid()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

def getStartingPoint()
    startx = floor(BOARDWIDTH/2)
    starty = floor(BOARDHEIGHT/2)


def makeText(text,color,bgcolor,top,left):
    #create the surface and rect objects for some text
    textSurf = BASICFONT.render(text,True,color,bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf,textRect)

def getLeftTopOfTile(tileX,tileY):
    left = XMARGIN + (tileX*TILESIZE)+(tileX-1)
    top = YMARGIN + (tileY*TILESIZE)+(tileY-1)
    return (left, top)

def drawTile(tilex,tiley):
    left, top = getLeftTopOfTile(tilex,tiley)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left, top, TILESIZE, TILESIZE))

def drawGrid():
    DISPLAYSURF.fill(BGCOLOR)

    for tilex in range(BOARDWIDTH):
        for tiley in range(BOARDHEIGHT):
            drawTile(tilex,tiley)

    #if game is over, call a different draw function to draw only the play again and quit buttons
    
if __name__=='__main__':
    main()











