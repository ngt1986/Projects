import pygame, random
pygame.init()

#Grid Size and game board initialize
grid_n = int(input("Enter n for an n x n grid size: "))
game_board = [""] * (grid_n+grid_n-1)
for i in range (grid_n+grid_n-1):
    game_board[i] = [" "] * (grid_n+grid_n-1)

#add starting dot pattern to game board
for i in range(0,grid_n+grid_n-1):
    for j in range(0,grid_n+grid_n-1):
        if i % 2 == 0 and j % 2 == 0:
            game_board[i][j] = "o"

#Window Size
display_width = 800
display_height = display_width
display_margin_height = display_height/grid_n/2
display_margin_width = display_width/grid_n/2

#text sizes
player_turn_display_size = display_height/grid_n/3
box_initial_size = display_margin_height/2

#Dot and line Sizes
dot_size = int(4+(30/grid_n))
line_size = dot_size/2

#Players 1 and 2 Names
player_1 = input("Player 1 type name: ")
player_2 = input("Player 2 type name: ")

#randomize starting player
rand = random.randint(0,99)
if rand > 49:
    player_turn = player_1
else:
    player_turn = player_2

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
pygame.display.set_caption('Dots! - ' + player_turn + " 's turn.")

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def draw_lines(x,y,w,h,inactive_color,active_color,row,column):
    """show if line is available to be selected"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #if mouse is over line option
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF,active_color,(x,y,w,h))

        #if clicked a horizontal line which has height dot_size*2
        if click[0] and h == dot_size*2:
            game_board[row+row][column+column+1] = "-"
            pygame.draw.rect(DISPLAYSURF, inactive_color, (x, y, w, h))
            if makes_box(player_turn,row,column,h) == False:
                swap_player()
            else:
                makes_box(player_turn, row, column, h)

        #if clicked a vertical line which has width dot_size*2
        elif click[0] and w == dot_size*2:
            game_board[row+row+1][column+column] = "|"
            pygame.draw.rect(DISPLAYSURF, inactive_color, (x, y, w, h))
            if makes_box(player_turn, row, column, h) == False:
                swap_player()
            else:
                makes_box(player_turn, row, column, h)

    #if mouse not over line option
    else:
        pygame.draw.rect(DISPLAYSURF, inactive_color, (x,y,w,h))

def line_drawn(x,y,w,h, active_color):
    """draws lines that have been chosen by players"""
    pygame.draw.rect(DISPLAYSURF, active_color, (x, y, w, h))
    return

def player_display(player_turn):
    """displays who's turn it is"""
    largeText = pygame.font.SysFont("comicsansms", int(player_turn_display_size))
    TextSurf, TextRect = text_objects(player_turn + "'s turn.", largeText, white)
    TextRect.center = (display_width/2,display_margin_height/3)
    DISPLAYSURF.blit(TextSurf, TextRect)
    return

def swap_player():
    global player_turn
    if player_turn == player_1:
        player_turn = player_2
    else:
        player_turn = player_1
    return
def makes_box(player_turn,row,column,h):
    """Determine if the move makes a complete box"""
    #look for empty squares and check row-1, row+1, column -1, column + 1 for lines
    #if all there, put player letter in the empty square
    for j in range(1,grid_n+grid_n-2):
        for i in range(1,grid_n+grid_n-2):
            if game_board[i][j] == " ":
                if game_board[i+1][j] == "-" and game_board[i-1][j] == "-" and game_board[i][j-1] == "|" and game_board[i][j+1] == "|":
                    game_board[i][j] = player_turn
                    return True
    return False

def box_letter():
    """if a box is complete, draw the player's initial in the box"""
    for column in range(1,grid_n+grid_n-2):
        for row in range(1,grid_n+grid_n-2):
            if game_board[row][column] == player_1:
                largeText = pygame.font.SysFont("comicsansms", int(box_initial_size))
                TextSurf, TextRect = text_objects(player_1[0], largeText, white)
                TextRect.center = ((column+1)/2 * (display_width / grid_n),
                                   (row+1)/2 * (display_height / grid_n)+display_margin_height/2)
                DISPLAYSURF.blit(TextSurf, TextRect)
            elif game_board[row][column] == player_2:
                largeText = pygame.font.SysFont("comicsansms", int(box_initial_size))
                TextSurf, TextRect = text_objects(player_2[0], largeText, white)
                TextRect.center = ((column + 1) / 2 * (display_width / grid_n),
                                       (row + 1) / 2 * (display_height / grid_n)+display_margin_height/2)
                DISPLAYSURF.blit(TextSurf, TextRect)

def draw_dots():
    """Draws the dots on the board"""
    for row in range(0, grid_n):
        for column in range(0, grid_n):
            pygame.draw.circle(DISPLAYSURF, green, (int((column + 1) * (display_width) / grid_n - display_margin_width),
                        int((row + 1) * (display_height) / grid_n - display_margin_height/2)), dot_size)

def game_over():
    """check if all squares are filled"""
    for column in range(1,grid_n+grid_n-2):
        for row in range(1,grid_n+grid_n-2):
            if game_board[row][column] == " ":
                return False
    return True

def game_over_screen():
    """update the screen with the results of the game"""
    count_player1 = 0
    count_player2 = 0
    for column in range(1,grid_n+grid_n-2):
        for row in range(1,grid_n+grid_n-2):
            if game_board[row][column] == player_1:
                count_player1 += 1
            elif game_board[row][column] == player_2:
                count_player2 += 1
    if count_player1 > count_player2:
        largeText = pygame.font.SysFont("comicsansms", int(player_turn_display_size/2))
        TextSurf, TextRect = text_objects(player_1 + " WINS!", largeText, bright_yellow)
        TextRect.center = (display_width/2,display_height/2)
        DISPLAYSURF.blit(TextSurf, TextRect)
    elif count_player2 > count_player1:
        largeText = pygame.font.SysFont("comicsansms", int(player_turn_display_size/2))
        TextSurf, TextRect = text_objects(player_2 + " WINS!", largeText, bright_yellow)
        TextRect.center = (display_width / 2, display_height/2)
        DISPLAYSURF.blit(TextSurf, TextRect)
    else:
        largeText = pygame.font.SysFont("comicsansms", int(player_turn_display_size/2))
        TextSurf, TextRect = text_objects("GAME ENDS IN A DRAW!", largeText, bright_yellow)
        TextRect.center = (display_width / 2, display_height/2)
        DISPLAYSURF.blit(TextSurf, TextRect)

def main():
    """Main game loop."""
    game_exit = False
    while not game_exit: #event handling

        #allow exit command (clickling 'red' x, for example) to quit the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #draw the dots, which never change
        DISPLAYSURF.fill(black)
        draw_dots()

        #draw line options
        for column in range(0, grid_n):
            for row in range(0, grid_n):

                # if no line is drawn yet
                #HORIZONTAL
                if column < grid_n-1 and row < grid_n and game_board[row+row][column+column+1] == " ":
                    draw_lines((display_margin_width+column*(display_width/grid_n)+dot_size),
                                (display_margin_height*1.5+row*(display_height/grid_n)-dot_size),
                                display_width/grid_n-dot_size*2,dot_size*2,black,gray,row,column)
                #VERTICAL
                # if no line is drawn yet
                if row < grid_n-1 and column < grid_n and game_board[row+row+1][column+column] == " ":
                    draw_lines((display_margin_width+column*(display_width/grid_n)-dot_size),
                                (display_margin_height*1.5+row*(display_height/grid_n)+dot_size),dot_size*2,
                                display_width/grid_n-dot_size*2,black,gray,row,column)

                #if line is drawn already
                #HORIZONTAL
                if column < grid_n-1 and row < grid_n and game_board[row + row][column + column + 1] == "-":
                    line_drawn((display_margin_width + column * (display_width / grid_n) + dot_size),
                               (display_margin_height*1.5 + row * (display_height / grid_n) - line_size/2),
                               display_width / grid_n - dot_size * 2, line_size, blue)
                #VERTICAL
                if row < grid_n-1 and column < grid_n and game_board[row+row+1][column+column] == "|":
                    line_drawn((display_margin_width+column*(display_width/grid_n)-line_size/2),
                            (display_margin_height*1.5+row*(display_height/grid_n)+dot_size),line_size,
                            display_width/grid_n-dot_size*2,blue)
        box_letter()
        player_display(player_turn)
        pygame.display.update()
        pygame.display.set_caption('Dots! - ' + player_turn + " 's turn.")
        if game_over():
            break

if __name__ == '__main__':
    main()

#if game_over() == True
game_over_screen()
pygame.display.update()
pygame.time.wait(5000)
# play_again = input("Play again (Y/N): ")
# if play_again == "Y" or play_again == "y":
#     #clear game board and reconstruct
#     game_board = [""] * (grid_n + grid_n - 1)
#     for i in range(grid_n + grid_n - 1):
#         game_board[i] = [" "] * (grid_n + grid_n - 1)
#
#     # add starting dot pattern to game board
#     for i in range(0, grid_n + grid_n - 1):
#         for j in range(0, grid_n + grid_n - 1):
#             if i % 2 == 0 and j % 2 == 0:
#                 game_board[i][j] = "o"
#     main_loop()

pygame.quit()
quit()