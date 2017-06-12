import os
import random

class GameBoard():
    def __init__(self) :
        numberList = [" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "," 10"," 11"," 12"," 13"," 14"," 15"," 0 "]
        random.shuffle(numberList)
        count = 0
        while count<4 :
            self.gameBoard[count]=[numberList[4*count],numberList[4*count+1],numberList[4*count+2],numberList[4*count+3]]
            count+=1

    def findZero(self):
        i,j = (0,0)
        while i<4 :
            while j<4 :
                if self.gameBoard[i][j] == " 0 " :
                    return 4*i+j
                j+=1
            i+=1
            j=0

    def left(self):
        dontMove = [0,4,8,12]
        zeroPosition = self.findZero()
        if zeroPosition in dontMove :
            self.wrongKey = 2
        else :
            self.gameBoard[zeroPosition//4][zeroPosition%4], self.gameBoard[zeroPosition//4][zeroPosition%4-1] = self.gameBoard[zeroPosition//4][zeroPosition%4-1], self.gameBoard[zeroPosition//4][zeroPosition%4]
    def right(self):
        dontMove = [3,7,11,15]
        zeroPosition = self.findZero()
        if self.findZero() in dontMove :
            self.wrongKey = 2
        else :
            self.gameBoard[zeroPosition//4][zeroPosition%4], self.gameBoard[zeroPosition//4][zeroPosition%4+1] = self.gameBoard[zeroPosition//4][zeroPosition%4+1], self.gameBoard[zeroPosition//4][zeroPosition%4]
    def up(self):
        dontMove = [0,1,2,3]
        zeroPosition = self.findZero()
        if self.findZero() in dontMove :
            self.wrongKey = 2
        else :
            self.gameBoard[zeroPosition//4][zeroPosition%4], self.gameBoard[zeroPosition//4-1][zeroPosition%4] = self.gameBoard[zeroPosition//4-1][zeroPosition%4], self.gameBoard[zeroPosition//4][zeroPosition%4]
    def down(self):
        dontMove = [12,13,14,15]
        zeroPosition = self.findZero()
        if self.findZero() in dontMove :
            self.wrongKey = 2
        else :
            self.gameBoard[zeroPosition//4][zeroPosition%4], self.gameBoard[zeroPosition//4+1][zeroPosition%4] = self.gameBoard[zeroPosition//4+1][zeroPosition%4], self.gameBoard[zeroPosition//4][zeroPosition%4]

    def complete(self):
        if self.gameBoard == self.completeGameBoard :
            return 1
        else :
            return 0
    gameBoard = [[" 1 "," 2 "," 3 "," 4 "],[" 5 "," 6 "," 7 "," 8 "],
    [" 9 "," 10"," 11"," 12"],[" 13"," 14"," 15"," 0 "]]
    completeGameBoard = [[" 1 "," 2 "," 3 "," 4 "],[" 5 "," 6 "," 7 "," 8 "],
    [" 9 "," 10"," 11"," 12"],[" 13"," 14"," 15"," 0 "]]

    def printGameBoard(self):
        i=0
        while i<4 :
            print(self.gameBoard[i])
            i+=1
    wrongKey = 0


gameBoard = GameBoard()
i=0
while i < 1 :
    os.system('cls' if os.name == 'nt' else 'clear')
    if gameBoard.wrongKey == 1 :
        print("제시된 네가지의 방향키중 하나만 눌러주십시오")
        gameBoard.wrongKey=0
    if gameBoard.wrongKey == 2 :
        print("이동불가능한 장소로의 이동입니다.")
        gameBoard.wrongKey=0
    gameBoard.printGameBoard()
    if gameBoard.complete() :
        break;
    key = input("a 왼쪽 s 아래쪽 d 오른쪽 w 위쪽 으로 0 이 이동합니다.")
    if key == "a" :
        gameBoard.left()
    elif key == "s" :
        gameBoard.down()
    elif key == "d" :
        gameBoard.right()
    elif key == "w" :
        gameBoard.up()
    else :
        gameBoard.wrongKey=1

print("congraturation")
