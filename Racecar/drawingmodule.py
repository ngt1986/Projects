import pygame

pygame.init()

white=(255,255,255)
black= (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
x=0
y=0
z=0

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(black)
clock = pygame.time.Clock()
pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

pygame.draw.line(gameDisplay, blue, (300,400),(400,300), 5)

pygame.draw.rect(gameDisplay, red, (400,400,50,25))
pygame.draw.circle(gameDisplay, white, (150,150), 50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    randcolor=(x,y,z)
    pygame.draw.polygon(gameDisplay, randcolor, ((600,200), (700,300),(500,400), (600,250)))
    x+=1
    if x == 255:
        x=0
    pygame.display.update()
    clock.tick(60)    

    
