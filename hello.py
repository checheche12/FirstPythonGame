import os
import random
import pygame
import sys
from pygame.locals import *

class GameBoard():
    def __init__(self) :
        numberList = [i for i in range(16)]
        random.shuffle(numberList)
        count = 0
        while count<4 :
            self.gameBoard[count]=[numberList[4*count],numberList[4*count+1],numberList[4*count+2],numberList[4*count+3]]
            count+=1

    def move(self,clickX,clickY):
        if clickX>=1 and self.gameBoard[clickY][clickX-1] == 0 :
            self.gameBoard[clickY][clickX-1], self.gameBoard[clickY][clickX] = self.gameBoard[clickY][clickX], self.gameBoard[clickY][clickX-1]
        if clickY>=1 and self.gameBoard[clickY-1][clickX] == 0 :
            self.gameBoard[clickY-1][clickX], self.gameBoard[clickY][clickX] = self.gameBoard[clickY][clickX], self.gameBoard[clickY-1][clickX]
        if clickX<=2 and self.gameBoard[clickY][clickX+1] == 0 :
            self.gameBoard[clickY][clickX+1], self.gameBoard[clickY][clickX] = self.gameBoard[clickY][clickX], self.gameBoard[clickY][clickX+1]
        if clickY<=2 and self.gameBoard[clickY+1][clickX] == 0 :
            self.gameBoard[clickY+1][clickX], self.gameBoard[clickY][clickX] = self.gameBoard[clickY][clickX], self.gameBoard[clickY+1][clickX]

    def complete(self):
        if self.gameBoard == self.completeGameBoard :
            return 1
        else :
            return 0
    gameBoard = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    completeGameBoard = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

    def printGameBoard(self):
        i=0
        while i<4 :
            j=0
            while j<4 :
                screen.blit(img[self.gameBoard[i][j]],(j*100,i*100))
                j+=1
            i+=1
    wrongKey = 0


TARGET_FPS = 30
clock = pygame.time.Clock()
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
LEFT = 1

pygame.init()
screen = pygame.display.set_mode((400, 400), DOUBLEBUF)
loadImage = 0
img=[]

while loadImage<16 :
    tempImage = pygame.image.load("Image/"+str(loadImage)+".png")
    img.append(tempImage)
    loadImage+=1

gameBoard = GameBoard()
while True :
    if gameBoard.wrongKey == 1 :
        print("제시된 네가지의 방향키중 하나만 눌러주십시오")
        gameBoard.wrongKey=0
    if gameBoard.wrongKey == 2 :
        print("이동불가능한 장소로의 이동입니다.")
        gameBoard.wrongKey=0
    if gameBoard.complete() :
        break;
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == LEFT :
            li = event.pos
            x = li[0]//100
            y = li[1]//100
            gameBoard.move(x,y)

    screen.fill(WHITE)
    gameBoard.printGameBoard()
    pygame.display.flip()
    clock.tick(TARGET_FPS)
    '''key = input("a 왼쪽 s 아래쪽 d 오른쪽 w 위쪽 으로 0 이 이동합니다.")
    if key == "a" :
        gameBoard.left()
    elif key == "s" :
        gameBoard.down()
    elif key == "d" :
        gameBoard.right()
    elif key == "w" :
        gameBoard.up()
    else :
        gameBoard.wrongKey=1'''

print("congraturation")
