import pygame, time, sys, random
from pygame.locals import *
import numpy as np
#from PIL import Image

pygame.init()

#Grid Size and game board initialize
grid_n = 3
game_board = [""] * (grid_n+grid_n-1)
for i in range (grid_n+grid_n-1):
    game_board[i] = [" "] * (grid_n+grid_n-1)

#add starting dot pattern to game board
for i in range(0,grid_n+grid_n-1):
    for j in range(0,grid_n+grid_n-1):
        if i % 2 == 0 and j % 2 == 0:
            game_board[i][j] = "o"
game_board[0][1] = "-"
for row in range(0,grid_n+grid_n-1):
    print(game_board[row])

#Window Size
display_width = 100*grid_n
display_height = 100*grid_n
display_margin_height = display_height/grid_n/2
display_margin_width = display_width/grid_n/2

#Dot and line Sizes
dot_size = 10
line_size = dot_size/2

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

DISPLAYSURF = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dots!')

clock = pygame.time.Clock()

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def line_option(x,y,w,h,inactive_color,active_color):
    """show if line is available to be selected"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #if mouse is over line option
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF,active_color,(x,y,w,h))
        if click[0]:
            line_added(game_board,row,column)
    #if mouse not over line option
    else:
        pygame.draw.rect(DISPLAYSURF, inactive_color, (x,y,w,h))



def line_added(game_board,row,column):
    """if line is added by a player, update game_board"""
    return

def player_turn():
    """displays who's turn it is and keeps track internally"""
    return

def makes_box():
    """Determine if the move makes a complete box"""
    return

def draw_dots():
    """Draws the dots on the board"""
    for row in range(0, grid_n):
        for column in range(0, grid_n):
            pygame.draw.circle(DISPLAYSURF, white, (int((row + 1) * (display_height) / grid_n - display_margin_height),
                                                    int((column + 1) * (
                                                        display_width) / grid_n - display_margin_width)), dot_size)

def draw_lines(game_board, active_color):
    """draws lines that have been chosen by players"""
    for row in game_board:
        for column in row:
            if column == "-":
                pygame.draw.rect(DISPLAYSURF, active_color, board_to_dots_horiz(row,column))
    return

def board_to_dots_horiz(row,column):
    """draws horizontal lines when game_board has '-' symbol"""
    x = display_margin_width+row*(display_width/grid_n)+dot_size
    y = display_margin_height+column*(display_height/grid_n)-dot_size
    w = display_width/grid_n-dot_size*2
    h = dot_size*2
    return (x,y,w,h)

def main_loop():
    game_exit = False

    while not game_exit: #event handling

        #allow exit command (clickling 'red' x, for example) to quit the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #draw the dots, which never change
        draw_dots()

        draw_lines(game_board, blue)

        pygame.display.update()


main_loop()
pygame.quit()
quit()