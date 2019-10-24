"""
Title:
        Simulation of SEMBLR Robots
Authors:
        Rakin Chowdhury,
        Carys Rees,
        Caitlin Straw,
        Sam Richardson,
        Jonah Edmonds :)
Date:
        18/10/19
Description:
"""

#Requibrown external moduals: pygame3
import pygame
import sys

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
    win.fill((105,105,105))
    for y in range(h):
        for x in range(w):
            #rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            rect = pygame.Rect(x*(block_size+10), y*(block_size+1), block_size+9, block_size)
            pygame.draw.rect(win, ((255,255,255)), rect)
    #pygame.display.update()

    return

def drawBlock(brick, col):

    rect = pygame.Rect(brick.x*(block_size+10), brick.y*(block_size+1), block_size+9, block_size)
    pygame.draw.rect(win, col, rect)
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
    drawBlock(brick, brown)

    """
    rect = pygame.Rect(brick.x*(block_size+10), brick.y*(block_size+1), block_size+9, block_size)
    pygame.draw.rect(win, ((255,0,0)), rect)
    """

    return brick

def placeBot(id, Loc):
    """
    Desctiption:
        Draws Bot to screen
    Arg(s) in:
        id [INT] - Object identification number
        Loc [Tuple] - (x,y): Location of brick on screen
    Arg(s) out:
        Brick [Object]- Brick object
    """

    brick = Block(id, Loc[0], Loc[1])
    drawBlock(brick, green)
    #pygame.draw.circle(win,green,(brick.x*(block_size) ,brick.y*(block_size)),9)
    #pygame.draw.circle(win,green,(brick.x,brick.y),9)

    """
    rect = pygame.Rect(brick.x*(block_size+10), brick.y*(block_size+1), block_size+9, block_size)
    pygame.draw.rect(win, ((255,0,0)), rect)
    """

    return brick

def placePallet(id, Loc):

    for i in range(2):
        for j in range(2):
            brick = Block(id, Loc[0]+i, Loc[1]+j)
            drawBlock(brick,blue)

    return
def placeBoader():

    for i in range(6):
            rect = pygame.Rect(i*(block_size+9), h-10*(block_size), block_size+9, block_size)
            pygame.draw.rect(win, (0,0,0), rect)
    for i in range(9):
            rect = pygame.Rect(6*(block_size+9), (i+((h/block_size))-9 )*(block_size), block_size, block_size)
            pygame.draw.rect(win, (0,0,0), rect)

    return



def initialParameters():
    global win, block_size, w, h
    block_size = 9
    w = 600
    h = 500
    win = pygame.display.set_mode((w,h))

    #colours
    global brown, green, blue, white, grey
    brown = ((80,25,0))
    green = ((0,255,0))
    blue = ((135,206,235))
    white = (255,255,255)
    grey = (124,124,124)
    return

def Key():
    #messy code will clean up
    pygame.font.get_fonts()
    font = pygame.font.Font(pygame.font.get_default_font(), 24)

    text = font.render('Bricks      ', True, (0,0,0), brown)
    textRect= text.get_rect()
    textRect.x = (block_size*0)
    textRect.y = (h - block_size*9)
    win.blit(text,textRect)

    text = font.render('Supply    ', True, (0,0,0), blue)
    textRect= text.get_rect()
    textRect.x = (block_size*0)
    textRect.y = (h - block_size*6)
    win.blit(text,textRect)

    text = font.render('Brick Bot ', True, (0,0,0), green)
    textRect= text.get_rect()
    textRect.x = (block_size*0)
    textRect.y = (h - block_size*3)
    win.blit(text,textRect)

    return

def setStruc(type):
    wall1 = [(x+10,10) for x in range(8)]
    wall2 = [(10,11+x) for x in range(9)]

    wall3 = [(x+10,20) for x in range(8)]
    wall4 = [(17,11+x) for x in range(9)]

    wall5 = [(14,11+x) for x in range(9)]

    if type == 0:
        struc = wall1
    elif type == 1:
        struc = wall1 + wall2
    elif type == 2:
        struc = wall1 + wall2 + wall3 + wall4
    elif type == 3:
        struc = wall1 + wall2 + wall3 + wall5 + wall4



    return struc

def basicWall(struc):
    for i in struc:
        placeBrick(0,(i[0],i[1]))

    return struc



def simplePath(start, points):

    path = [start]

    for i in points:
        distx = abs(start[0] -  i[0])
        disty = abs(start[1] -  i[1])

        pathy = []
        pathx = []
        for y in range(disty):
            pathy.append((start[0],start[1]+(y+1)))
        for x in range(distx):
            pathx.append((start[0]+(x+1),start[1]++(y+1)))


        path = path + pathy + pathx
        pathy.reverse()
        pathx.reverse()
        path = path + pathx + pathy + [start]

    return path


def guiMain(pathType,strucType):
    runing = True



    pygame.init()
    clock = pygame.time.Clock()
    initialParameters()

    #testPath = [(10,8),(10,8),(10,9),(10,10),(10,9),(10,8),(10,9),(11,9),(11,10),(11,9),(10,9),(10,8),\
                #(10,9),(11,9),(12,9),(12,10),(12,9),(11,9),(10,9),(10,8),\
                #(10,9),(11,9),(12,9),(13,9),(13,10),(13,9),(12,9),(11,9),(10,9),(10,8)]

    MainLoop = True

    bricked = []
    wall = setStruc(int(strucType))
    testPath = simplePath((10,8), wall)



    x=0
    while MainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainLoop = False

        #drawGrid()


        if runing == True:
            win.fill((255,255,255))



            placePallet(0,(10,7))
            basicWall(bricked)
            Key()
            placeBoader()

            bot1 = placeBot(0,testPath[x])
            x = x+1

            f2 = pygame.font.Font(pygame.font.get_default_font(), 8)

            if x >= len(testPath):
                x=0
                bricked = []

            if testPath[x] in wall:
                bricked.append(testPath[x])
        else:
            f2 = pygame.font.Font(pygame.font.get_default_font(), 50)
            t3 = f2.render('Simulation Paused', True, (0,0,0), blue)
            win.blit(t3, (70, h/2 -70))









        clock.tick(20)
        pygame.display.flip()

    return

def help():
    print("""
    Help:

    Ussage:

    Key:


            """)

def main():
    strucModes = ("0","1","2","3")
    if __name__=='__main__':

        if len(sys.argv) != 3:
            help()
        elif sys.argv[1]  == "simple":
            if sys.argv[2] in strucModes:
                guiMain(0,sys.argv[2])
            else:
                help()

        else:
            print("Incorrect Ussage")
            help()


    return
main()
