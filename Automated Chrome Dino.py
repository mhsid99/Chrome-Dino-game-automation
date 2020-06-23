# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 01:32:06 2020

@author: Hamza
"""

import pyautogui # pip install pyautogui
from PIL import ImageGrab as ig # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(720,750):
        for j in range(241,330):
            if data[i, j]<100:
                hit("down")
                return
    #for cactus
    for i in range(700,840):
        for j in range(340,385):
            if data[i,j]<100:
                hit("up")
                return
    return

print("game starts in...")
for i in range(4,1):
    print(i)
    print("\n")
time.sleep(3)
hit("up") 
while True:
    image=ig.grab().convert("L")  
    data=image.load()
    isCollide(data)

'''
        # print(asarray(image))

        # Draw the rectangle for cactus
    for i in range(700, 840): #width 50
        for j in range(340,385): #height 87
            data[i, j] = 0
        
        # Draw the rectangle for birds
    for i in range(720, 750):#50 width
        for j in range(241,330):#153 height
            data[i, j] = 171

    image.show()
    break

'''
