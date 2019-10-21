"""
Title:
        Simulation of SEMBLR Robots
Authors:
        Rakin Chowdhury,
        Carys Rees,
        Caitlin Straw,
        Sam Richardson,
        Jonah Edmonds
Date:
        18/10/19
Description:
"""

#Required external moduals: pygame3
import pygame

#Width and Height Dimentions


global block_size, w, h
block_size = 9
w = 600
h = 500
win = pygame.display.set_mode((w,h))


class Bot:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.size = (3,1)
    v = 1
    def Right(self):
        self.x = self.x + self.v
    def Left(self):
        self.x = self.x - self.v
    def Up(self):
        self.y = self.y + self.v
    def Down(self):
        self.y = self.y - self.v

class Block:
    def __init__(self,id,x,y):
        self.id = id
        self.x = x
        self.y = y
        self.size = (1,1)

def drawGrid():

    """
    Description:
        Draws background grid
    Arg(s) in:
        w [INT] - screen width
        h [INT] - screen height
    Arg(s) out:
        none
    """

    for y in range(h):
        for x in range(w):
            #rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            rect = pygame.Rect(x*(block_size+10), y*(block_size+1), block_size+9, block_size)
            pygame.draw.rect(win, ((255,255,255)), rect)

    return

def placeBrick(id, Loc):
    """
    Desctiption:
        Draws Brick to screen
    Arg(s) in:
        id [INT] - Object identification number
        Loc [Tuple] - (x,y): Location of brick on screen
    Arg(s) out:
        Brick [Object]- Brick object
    """

    brick = Block(id, Loc[0], Loc[1])

    rect = pygame.Rect(brick.x*(block_size+10), brick.y*(block_size+1), block_size+9, block_size)
    pygame.draw.rect(win, ((255,0,0)), rect)



    return




"""
bot1 = Bot(1,0,0)
rect = pygame.Rect(bot1.x*(block_size+1), bot1.y*(block_size+1), block_size, block_size)
pygame.draw.rect(win, ((255,0,0)), rect)
bot1.Right()
rect = pygame.Rect(bot1.x*(block_size+1), bot1.y*(block_size+1), block_size, block_size)
pygame.draw.rect(win, ((255,0,0)), rect)


bot = [(1,1),(1,2),(2,1),(2,2)]

for x, y in bot:


    rect = pygame.Rect(x*(block_size+1), y*(block_size+1), block_size, block_size)
    pygame.draw.rect(win, ((255,0,0)), rect)
"""


MainLoop = True

drawGrid()
placeBrick(0,(2,3))
struc1 = [(x+5,5) for x in range(10)]
for i in struc1:
    placeBrick(0,(i[0],i[1]))


while MainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainLoop = False
    pygame.display.flip()
