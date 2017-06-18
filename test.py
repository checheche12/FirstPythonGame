import pygame
from pygame.locals import *
import sys

numberList = [3,5,11,2,10,4,15,1,8,0,7,14,13,6,12,9]
reverse_number_count = 0
reverse_check = 0
while reverse_check < 15 :
    if(numberList[reverse_check]==0) :
        reverse_check+=1
        continue
    reverse_check2 = reverse_check + 1
    while reverse_check2 < 16 :
        if(numberList[reverse_check2]==0) :
            reverse_check2+=1
            continue
        if(numberList[reverse_check] > numberList[reverse_check2]) :
            reverse_check2+=1
            reverse_number_count+=1
            continue
        reverse_check2+=1
    reverse_check+=1


print(reverse_number_count)
