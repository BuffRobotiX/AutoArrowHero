from pyautogui import *
from PIL import ImageGrab as ig
from PIL import Image as im
from threading import *
from Queue import *
import time

#Load the images and grab the color from the center
right = im.open("right.png").load()[30, 30]
left = im.open("left.png").load()[30, 30]
up = im.open("up.png").load()[30, 30]
down = im.open("down.png").load()[30, 30]

#How far in each direction from the search location to look for the color.
searchdist = 6 #Too high is slow, too small is less stable.

#X, Y location of the search location on the screen in pixels.
pointx = 466 - searchdist//2
pointy = 209 - searchdist//2


queue = Queue()

#Optionally click on the web browser and restart the game.
#click(x=pointx, y=pointy)
#press('space')

#Thread for grabbing images and adding them to the queue
def grabThread():
    while True:
        img = ig.grab()
        queue.put_nowait(img.load())

#Thread for searching for color
def testThread():
    while True:
        try:
            img = queue.get_nowait()
            for i in range(searchdist):
                for j in range(searchdist):
                    p = img[pointx + i, pointy + j]
                    if p == right:
                        press('right')
                        break
                    elif p == left:
                        press('left')
                        break
                    elif p == up:
                        press('up')
                        break
                    elif p == down:
                        press('down')
                        break
        except Empty:
            pass

#Unthreaded loop, still works pretty good.
def play():
    while True:
        try:
            img = ig.grab()
            nimg = img.load()
            for i in range(searchdist):
                for j in range(searchdist):
                    p = nimg[pointx + i, pointy + j]
                    if p == right:
                        press('right')
                        break
                    elif p == left:
                        press('left')
                        break
                    elif p == up:
                        press('up')
                        break
                    elif p == down:                                                                            
                        press('down')
                        break
        except KeyboardInterrupt:
            break

#Threaded version
#Interesting thing about capturing too many images, see readme.
'''
for i in range(1): #Number of threads
    thread = Thread(target=grabThread)
    thread.daemon = True
    thread.start()     
for i in range(5): #Number of threads
    thread = Thread(target=testThread)
    thread.daemon = True
    thread.start()
    '''

#Unthreaded version.
play()
