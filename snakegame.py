import random
import time
import pygame
import sys
from pygame.locals import *
FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
def snakegame():
	global MAINCLOCK, MAINSURF, BASICFONT
	pygame.init()
	MAINCLOCK = pygame.time.Clock()
    	MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    	pygame.display.set_caption('TRIPPY SNAKE')
	while True:
        	movingsnake()
        	GameOver()
def movingsnake():
	startx = random.randint(5, CELLWIDTH - 6)
    	starty = random.randint(5, CELLHEIGHT - 6)
    	snakeCoords = [(startx, starty), (startx-1, starty)]
	direction = RIGHT
	apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    			direction = LEFT
                		if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    			direction = RIGHT
                		if (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    			direction = UP
                		if (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    			direction = DOWN
               	 		if event.key == K_q:
					pygame.quit()
					sys.exit()
		if snakeCoords[0][0] == -1 or snakeCoords[0][0] == CELLWIDTH or snakeCoords[0][1] == -1 or snakeCoords[0][1] == CELLHEIGHT:
			return
		for snakeBody in snakeCoords[1:]:
			if (snakeCoords[0][0], snakeCoords[0][1]) == snakeBody:
                		return
		if snakeCoords[0][0] == apple[0] and snakeCoords[0][1] == apple[1]:	
			apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
	
		else:
            		snakeCoords.pop()
		if direction == UP:
            		snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] - 1))
        	elif direction == DOWN:
            		snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] + 1))
        	elif direction == LEFT:
            		snakeCoords.insert(0, (snakeCoords[0][0] - 1, snakeCoords[0][1]))
        	elif direction == RIGHT:
            		snakeCoords.insert(0, (snakeCoords[0][0] + 1, snakeCoords[0][1]))
		MAINSURF.fill((255,255,255))
        	drawSnake(snakeCoords)
        	drawApple(apple)
		pygame.display.update()
        	MAINCLOCK.tick(FPS)
def GameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, (0,0,0))
    overSurf = gameOverFont.render('Over', True, (0,0,0))
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    MAINSURF.blit(gameSurf, gameRect)
    MAINSURF.blit(overSurf, overRect)
    pygame.display.update()
    time.sleep(0.5)
def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord[0] * CELLSIZE
        y = coord[1] * CELLSIZE
        coordRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(MAINSURF, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), coordRect)
def drawApple(coord):
    x = coord[0] * CELLSIZE
    y = coord[1] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(MAINSURF,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), appleRect)
snakegame()
