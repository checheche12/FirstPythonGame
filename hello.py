import os
import random
import pygame
import sys
from pygame.locals import *

class GameBoard():
    def __init__(self) :
        numberList = [i for i in range(16)]
        while True :
            random.shuffle(numberList)
            reverse_number_count = 0
            reverse_check = 0
            zero=0
            while reverse_check < 15 :
                if(numberList[reverse_check]==0) :
                    zero = reverse_check
                    reverse_check+=1
                    continue
                reverse_check2 = reverse_check + 1
                while reverse_check2 < 16 :
                    if(numberList[reverse_check2]==0) :
                        reverse_check2+=1
                        continue
                    elif(numberList[reverse_check] > numberList[reverse_check2]) :
                        reverse_check2+=1
                        reverse_number_count+=1
                        continue
                    reverse_check2+=1
                reverse_check+=1

            if(numberList[15]==0):
                zero = 15
            print(reverse_number_count+((zero//4)+1))
            if (reverse_number_count+((zero//4)+1))%2 == 0 :
                break;

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

        reverse_number_count = 0
        reverse_check = 0
        zero = 0
        gBr = self.gameBoard[0]+self.gameBoard[1]+self.gameBoard[2]+self.gameBoard[3]
        while reverse_check < 15 :
            if(gBr[reverse_check]==0) :
                zero = reverse_check
                reverse_check+=1
                continue
            reverse_check2 = reverse_check + 1
            while reverse_check2 < 16 :
                if(gBr[reverse_check2]==0) :
                    reverse_check2+=1
                    continue
                elif(gBr[reverse_check] > gBr[reverse_check2]) :
                    reverse_check2+=1
                    reverse_number_count+=1
                    continue
                reverse_check2+=1
            reverse_check+=1
        if(gBr[15]==0):
            zero = 15

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
RIGHT = 3

pygame.init()
screen = pygame.display.set_mode((400, 400), DOUBLEBUF)
loadImage = 0
img=[]
cong = pygame.image.load("Image/congraturation.png")

while loadImage<16 :
    tempImage = pygame.image.load("Image/"+str(loadImage)+".png")
    img.append(tempImage)
    loadImage+=1


gameStatus = True
gamePlay = True
while gameStatus :
    gameBoard = GameBoard()
    while gamePlay :
        if gameBoard.complete() :
            gamePlay = False
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

    aaa = True;
    while aaa :
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == LEFT :
                gamePlay = True
                aaa = False
                break;
            elif event.type == MOUSEBUTTONDOWN and event.button == RIGHT :
                pygame.quit()
                sys.exit()
        screen.blit(cong,(100,100))
        pygame.display.flip()
        clock.tick(5)
