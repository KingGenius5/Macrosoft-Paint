# PaintProject.py

#Will have to break down this code into multiple componenets and make it OOP. This is not efficient.

from pygame import *
from tkinter import *
from tkinter import filedialog
from random import *
from math import *
from pygame.locals import *
import pygame

root = Tk()
root.withdraw()  # removes the extra TK window
size = (1100, 900)
screen = display.set_mode(size)
font.init()
pygame.init()  # This initializes the music mixer

# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

###Set up for the menu screen###

beginning = True
# This boolean lets the while loop for the menu stay true

if beginning == True:
    # While beginning is true, play background music for the menu screen
    #theme = ("Hero's Theme.wav")
    #mixer.music.load(theme)
    #mixer.music.play(-1)  # This leaves the music on loop
    print("Still not working")

while beginning:

    mx, my = mouse.get_pos()  ###gets position of the mouse
    mb = mouse.get_pressed()

    # The rects below set up the menu screen that will load and stay until the DC button
    # is clicked which then takes you to the actual paint program

    newBackgroundRect = Rect(0, 0, 1096, 875)
    draw.rect(screen, (255, 255, 255), newBackgroundRect)
    coolBGPic = image.load("Images/coolBG.jpg")
    coolBGPicNew = transform.scale(coolBGPic, (1096, 875))
    screen.blit(coolBGPicNew, newBackgroundRect)

    coolLogoRect = Rect(400, 500, 320, 320)
    coolLogoPic = image.load("Images/coolLogo.png")
    screen.blit(coolLogoPic, coolLogoRect)

    if coolLogoRect.collidepoint(mx, my):
        # If the button is hovered over, the rect is highlighted
        draw.ellipse(screen, (255, 255, 255), coolLogoRect, 5)

    for evt in event.get():
        # If the close button is clicked, close the program
        if evt.type == QUIT:
            beginning = False
            quit()

        # If the button is clicked, beginning is set to False which breaks the while
        # loop for the menu screen and takes you to the main program
        if mb[0] == 1 and coolLogoRect.collidepoint(mx, my):
            beginning = False

    display.flip()

###############################


###Music List###

music = ["Justice League Theme.mp3", "An Ideal of Hope.mp3", "Is She With You.mp3",
         "BvS Theme.mp3", "BTAS Theme.mp3", "BAO Theme.mp3", "BAC Theme.mp3", "Flash Theme.mp3",
         "Teen Titans Theme.mp3"]
# By creating a list for the music, it makes it easier to toggle between each song
# when it comes to the song functions
song = 0
# Song at 0 is the placement of the song in the list meaning it plays the Justice League Theme first
#mixer.music.load(music[song])
#mixer.music.play(-1)
print("Music working")
# With the music player at -1, the song is on repeat forever

###################


###loading ALL images###

# Each picture has a use towards a variable
# The variable names are very straightforward, so you can link each picture to the function

wheelPic = image.load("Images/colwheel.png")

dcPic = image.load("Images/dc.jpg")
dc1Pic = image.load("Images/dc1.png")
dc2Pic = image.load("Images/dc2.png")
dc3Pic = image.load("Images/dc3.png")
dc4Pic = image.load("Images/dc4.png")

dcAPic = image.load("Images/dcA.jpg")
dc1APic = image.load("Images/dc1A.png")
dc2APic = image.load("Images/dc2A.png")
dc3APic = image.load("Images/dc3A.png")
dc4APic = image.load("Images/dc4A.png")

backPic = image.load("Images/embers.jpg")

pencilPic = image.load("Images/pencil.png")

eraserPic = image.load("Images/eraser.png")

clearPic = image.load("Images/clear.png")

savePic = image.load("Images/save.png")

openPic = image.load("Images/open.png")

logoPic = image.load("Images/logo.png")

undoPic = image.load("Images/undo.png")

redoPic = image.load("Images/redo.png")

markerPic = image.load("Images/marker.png")

arrowPic = image.load("Images/arrow.png")

buttonPic = image.load("Images/button.png")

paintbrushPic = image.load("Images/paintbrush.png")

sprayPic = image.load("Images/spray.png")

highlighterPic = image.load("Images/highlighter.png")

mpenPic = image.load("Images/mpen.png")

linePic = image.load("Images/line.png")

batmanLogoStampPic = image.load("Images/batmanLogoStamp.png")
myStamp = image.load("Images/batmanStamp.png")

supermanLogoStampPic = image.load("Images/supermanLogoStamp.png")
sStamp = image.load("Images/supermanStamp.png")

wwStampLogoPic = image.load("Images/wwLogoStamp.png")
wwStamp = image.load("Images/WWSTAMP.png")

aquamanLogoStampPic = image.load("Images/aquamanLogoStamp.png")
aquamanStamp = image.load("Images/aquamanStamp.png")

flashLogoStampPic = image.load("Images/flashLogoStamp.png")
flashStamp = image.load("Images/flashStamp.png")

cyborgLogoStampPic = image.load("Images/cyborgLogoStamp.png")
cyborgStamp = image.load("Images/cyborgStamp.png")

fillPic = image.load("Images/fill.png")

unfillPic = image.load("Images/unfill.png")

rectanglePic = image.load("Images/rectangle.png")

ellipsePic = image.load("Images/ellipse.png")

polygonPic = image.load("Images/polygon.png")

###The symbol pics are for the stamps that are the superhero logos when they are being blitted

bSymbolPic = image.load("Images/bSymbol.png")
symbolLogo1Pic = image.load("Images/symbolLogo1.jpg")

sSymbolPic = image.load("Images/sSymbol.png")
symbolLogo2Pic = image.load("Images/symbolLogo2.jpg")

wSymbolPic = image.load("Images/wSymbol.png")
symbolLogo3Pic = image.load("Images/symbolLogo3.jpg")

aSymbolPic = image.load("Images/aSymbol.png")
symbolLogo4Pic = image.load("Images/symbolLogo4.jpg")

fSymbolPic = image.load("Images/fSymbol.png")
symbolLogo5Pic = image.load("Images/symbolLogo5.jpg")

cSymbolPic = image.load("Images/cSymbol.png")
symbolLogo6Pic = image.load("Images/symbolLogo6.jpg")

###ump stands for Ultimate Magic Pen and ed for Eye-Dropper

umpPic = image.load("Images/ump.png")

edPic = image.load("Images/ed.png")

playPic = image.load("Images/play.png")

nextPic = image.load("Images/next.png")

prevPic = image.load("Images/prev.png")

###Transforming Images and Defaults###

# pic width height
##dcSmall=transform.scale(dcPic,(600 , 500))
backPicSmall = transform.scale(backPic, (1096, 875))
###dcFlip=transform.flip(dcSmall,True,False)#mirror image


col = BLACK  # default colour is black

tool = "no tool"
shape = "no shape"
stamp = "no stamp"

display.set_caption("DC Paint")

omx = 300
omy = 300

###Thickness of shapes###

# The thickness below are for each tool
t = 10
eraserRadius = 10
markerRadius = 10
circleThickness = 10
thickness = 10
r = 10

# The thicknesses below are for toggling between filled and unfilled shapes
polygonThickness = 1
rectangleTH = 1
circleTH = 1

########################

adjX = 125
adjY = 75

###Clicking Booleans###

# These clicking booleans are very important, they are for differentiating the highlighting
# of tools and checking to see if the menu buttons have been clicked
# c booleans are specifically for buttons blitting more menu options

c = False
c1 = False
c2 = False
c3 = False
c4 = False
c5 = False
c6 = False

c7 = False
c8 = False
c9 = False
c10 = False
c11 = False

# ac buttons are for main button menus to display; that's why they start as true and become
# false when you click on them

ac = True
ac2 = True
ac3 = True
ac4 = True

# mnC is false until the Stamp button is clicked, blitting the menus and making it true
# mnD is false until the Background button is clicked, blitting the backgrounds making it true

mnC = False
mnD = False

# music_clicked is for the pause/play music button, it starts out as false because it hasn't
# been clicked. When it is clicked, it becomes true pausing the music. When clicked again, the
# boolean becomes false, resuming the music from where it left off. The cycle continues on.

music_clicked = False

######################


###Background Lists###

# This first background list is for the clear button. When the clear button is clicked, it will
# blit whatever background you are on to the screen as opposed to a regular white screen

bgSTR = ["Images/dc.jpg", "Images/dc1.png", "Images/dc2.png", "Images/dc3.png",
         "Images/dc4.png"]  # the strings of the image
backgrounds = []
for name in bgSTR:
    pic = image.load(name)  # now loading the actual picture
    backgrounds.append(pic)
# loc is the index of the background list, it starts at 4 to ensure a white background
loc = 4

# The second background list below was originally meant for my erasing of images on top of
# backgrounds but I found a different solution to the problem. I left this to show my
# my understanding of the concept

##bgER=["Images/dc.jpg","Images/dc1.png","Images/dc2.png","Images/dc3.png","Images/dc4.png"]
##backgrounds2=[]
##for b in bgER:
##    picture=image.load(b)#now loading the actual picture
##    backgrounds2.append(picture)
##
pos = 4

######################

###Main title###
# dim 550x100
titleBar = Surface((550, 100), SRCALPHA)
arialFont = font.SysFont("Arial", 36)
myText = arialFont.render("WELCOME TO THE WORLD OF DC!", True, WHITE)

###############


###defining all RECTS in the program###

# The variable names are pretty straightforward, so an explanation is not needed. They correspond
# to functions that I will explain, rest assured.

canvasRect = Rect(180, 100, 600, 500)

fourButtonBorderRect = Rect(835, 10, 250, 70)

pencilRect = Rect(195, 660, 50, 50)
eraserRect = Rect(255, 660, 50, 50)
markerRect = Rect(315, 660, 50, 50)
paintbrushRect = Rect(375, 660, 50, 50)
sprayRect = Rect(435, 660, 50, 50)
highlighterRect = Rect(495, 660, 50, 50)
mpenRect = Rect(555, 660, 50, 50)

bgRect = Rect(185, 657, 430, 56)
bg1Rect = Rect(185, 717, 250, 56)
bg2Rect = Rect(30, 210, 110, 340)

lineRect = Rect(195, 720, 50, 50)
rectangleRect = Rect(255, 720, 50, 50)
ellipseRect = Rect(315, 720, 50, 50)
polygonRect = Rect(375, 720, 50, 50)

wheelRect = Rect(880, 585, 200, 200)
wheelBorderRect = Rect(875, 580, 210, 210)
backRect = Rect(0, 0, 1024, 768)

openRect = Rect(1025, 20, 50, 50)
saveRect = Rect(965, 20, 50, 50)
clearRect = Rect(800, 560, 50, 50)  # clear the canvas

titleRect = Rect(0, 0, 550, 40)  # relative to the titleBar surface
logoRect = Rect(11, 0, 256, 256)

undoRect = Rect(845, 20, 50, 50)
redoRect = Rect(905, 20, 50, 50)

expandRect = Rect(10, 670, 35, 150)

batmanStampRect = Rect(35, 215, 100, 100)
supermanStampRect = Rect(35, 335, 100, 100)
wwStampRect = Rect(35, 445, 100, 100)

aquamanStampRect = Rect(35, 215, 100, 100)
flashStampRect = Rect(35, 335, 100, 100)
cyborgStampRect = Rect(35, 445, 100, 100)

bStampRect = Rect(35, 215, 100, 100)
sStampRect = Rect(35, 335, 100, 100)
wStampRect = Rect(35, 445, 100, 100)

aStampRect = Rect(35, 215, 100, 100)
fStampRect = Rect(35, 335, 100, 100)
cStampRect = Rect(35, 445, 100, 100)

stampRect = Rect(35, 160, 100, 40)

fillRect = Rect(905, 235, 50, 75)
unfillRect = Rect(965, 235, 50, 75)

umpRect = Rect(845, 235, 50, 50)
edRect = Rect(1025, 235, 50, 50)

toolRect = Rect(60, 670, 100, 35)
shapeRect = Rect(60, 730, 100, 35)

mnRect = Rect(30, 560, 20, 20)
mn1Rect = Rect(60, 560, 20, 20)
mn2Rect = Rect(90, 560, 20, 20)
mn3Rect = Rect(120, 560, 20, 20)

mn4Rect = Rect(650, 840, 30, 30)
mn5Rect = Rect(690, 840, 30, 30)
mn6Rect = Rect(730, 840, 30, 30)
mn7Rect = Rect(770, 840, 30, 30)
mn8Rect = Rect(810, 840, 30, 30)

backgroundRect = Rect(645, 630, 200, 40)

dcRect = Rect(645, 680, 200, 150)
dc1Rect = Rect(645, 680, 200, 150)
dc2Rect = Rect(645, 680, 200, 150)
dc3Rect = Rect(645, 680, 200, 150)
dc4Rect = Rect(645, 680, 200, 150)

playRect = Rect(935, 325, 50, 50)
nextRect = Rect(995, 325, 50, 50)
prevRect = Rect(875, 325, 50, 50)

colorRect = Rect(880, 800, 50, 50)

posRect = Rect(20, 610, 120, 40)

###Drawing the Rects and Blitting the images###

screen.blit(backPicSmall, backRect)
draw.rect(screen, WHITE, canvasRect)
draw.rect(screen, BLACK, canvasRect, 3)
draw.rect(screen, WHITE, canvasRect, 5)

draw.rect(screen, WHITE, wheelBorderRect)

draw.rect(screen, WHITE, fourButtonBorderRect, 5)

screen.blit(wheelPic, wheelRect)

screen.blit(clearPic, clearRect)
screen.blit(savePic, saveRect)
screen.blit(openPic, openRect)
screen.blit(undoPic, undoRect)
screen.blit(redoPic, redoRect)

draw.rect(screen, (225, 225, 225), expandRect)
screen.blit(arrowPic, expandRect)
draw.rect(screen, WHITE, expandRect, 2)

draw.rect(screen, (10, 127, 203), stampRect)
draw.rect(screen, WHITE, stampRect, 2)

draw.rect(screen, (10, 127, 203), backgroundRect)
draw.rect(screen, WHITE, backgroundRect, 2)

draw.rect(screen, (9, 154, 248), posRect)
draw.rect(screen, WHITE, posRect, 2)

draw.rect(screen, col, colorRect)
draw.rect(screen, WHITE, colorRect, 2)

############################################


###Displaying Text without subsurfaces###

tnrFont = font.SysFont("Times", 30)
displayTextPic = tnrFont.render("Stamps", True, WHITE)
screen.blit(displayTextPic, (40, 160))

tnrFont = font.SysFont("Times", 30)
displayTextPic = tnrFont.render("Backgrounds", True, WHITE)
screen.blit(displayTextPic, (665, 632))

tnrFont = font.SysFont("Times", 30)
displayTextPic = tnrFont.render("Position", True, WHITE)
screen.blit(displayTextPic, (30, 610))

#########################################

###Setting up the highlighter tool###

eraserHead = Surface((40, 40), SRCALPHA)  # make blank Surface
draw.circle(eraserHead, (255, 255, 255, 10), (20, 20), 20)  # draw using alpha
brushHead = Surface((20, 20), SRCALPHA)
draw.circle(brushHead, (255, 255, 0, 44), (10, 10), 10)

####################################


###Info Box Set Up###

infoRect = Rect(800, 100, 285, 125)
draw.rect(screen, (9, 154, 248), infoRect)
draw.rect(screen, WHITE, infoRect, 5)
draw.rect(screen, BLUE, infoRect, 2)

tnrFont = font.SysFont("Times", 28)
displayTextPic = tnrFont.render("LET'S GET PAINTING", True, WHITE)
displayTextPic1 = tnrFont.render("IN THE WORLD OF", True, WHITE)
displayTextPic2 = tnrFont.render("DC!", True, WHITE)
screen.blit(displayTextPic, (810, 110))
screen.blit(displayTextPic1, (820, 140))
screen.blit(displayTextPic2, (920, 175))

##############

###Polygon tool variables###

# The done and polygon_start booleans are for the program to understand when the user starts
# drawing the polygon on screen. When you actually click on screen using the polygon tool
# the booleans are true and the code runs
done = False
polygon_start = False
# Since the polygon tool is dealing with many points, a list is needed to keep track of said points
points = []
# snap_x and snap_y are variables used to find the distance between the polygon points. The
# distance is then drawn out using a line
snap_x = 0
snap_y = 0

###########################

# picCopy is a picture of the screen, specifically the canvasRect, this must be done to
# add the picCopy to the undo list. The undo list keeps all of the pictures that are taken of
# the canvasRect, with the canvas being a subsurface that is the canvasRect (named just for
# simplicity). The redo function is an empty list and won't have anything appended to it until
# the function calls for it

picCopy = screen.subsurface(canvasRect).copy()
canvas = screen.subsurface(canvasRect)
undo = [picCopy]
redo = []

running = True
while running:

    mx, my = mouse.get_pos()  ###gets position of the mouse
    mb = mouse.get_pressed()  ###if mb --- mousebutton
    keys = key.get_pressed()

    click = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False

        # The color rect is drawn here to be updated whenever a color is changed, this happens
        # because the rect is in the while running loop
        draw.rect(screen, col, colorRect)
        draw.rect(screen, WHITE, colorRect, 2)

        if evt.type == MOUSEBUTTONDOWN:
            print("Mouse Down")
            click = True
            sx, sy = evt.pos  # (sx,sy) tuple-the position where you clicked
            backPic = screen.subsurface(canvasRect).copy()  # taking a screenshot

            if evt.button == 5:  # scrolling down
                # When the mouse is scrolled down, all of these thicknesses decrease by 1
                thickness -= 1
                t -= 1
                r -= 1
                eraserRadius -= 1
                markerRadius -= 1
                circleThickness -= 1

            if evt.button == 4:  # scrolling up
                # When the mouse is scrolled up, all of these thicknesses increase by 1
                thickness += 1
                t += 1
                r += 1
                eraserRadius += 1
                markerRadius += 1
                circleThickness += 1

            # However, if the thicknesses reach a certain radius/thickness, they have set limits
            # to avoid any errors. To maintain consistency, all of the tools have the same
            # limits, if the thickness is 36, subtract 1 to keep it 35. If the thickness is
            # 0, add 1 to keep it at 1.

            if thickness == 0 or t == 0 or r == 0 or eraserRadius == 0 or markerRadius == 0 or circleThickness == 0:
                thickness += 1
                t += 1
                r += 1
                eraserRadius += 1
                markerRadius += 1
                circleThickness += 1

            if thickness == 36 or t == 36 or r == 36 or eraserRadius == 36 or markerRadius == 36 or circleThickness == 36:
                thickness -= 1
                t -= 1
                r -= 1
                eraserRadius -= 1
                markerRadius -= 1
                circleThickness -= 1

            # Whenever there is a left click (especially on the canvas) a picture is taken.
            # I already explained that canvas is short for canvas. This happens so it can
            # be added to the undo list
            if mb[0] == 1:
                canvas.copy()

            if shape == "polygon" and canvasRect.collidepoint(mx, my):
                # When you use the polygon tool and start drawing you are not done, so
                # you add to the points array. When you let go, you are done and that is when
                # points get appended and compared to your mx,my coordinates. Your next point
                # is then connected to by a line and the cycle continues until you want to
                # finish drawing your polygon shape
                if done == True:
                    points = []
                    done = False
                elif polygon_start == True:
                    points.append((mx, my))
                    if len(points) >= 1:
                        draw.line(screen, col, points[len(points) - 1], (mx, my), 5)

            # When you click on the next button, the next song in the music list plays
            if evt.button == 1 and nextRect.collidepoint(mx, my) and song <= len(music):
                # The song index is added onto by 1
                song = song + 1

                try:
                    # The mixer then load the next song using the new updated index
                    #mixer.music.load(music[song])
                    print("Should work")

                except:
                    # Only if the previous button is not clicked and you go backwards
                    # nor keep moving forward in the list and start at the beginning of the list
                    song -= 1
                    #mixer.music.load(music[song])
                    print("Should not be working")
                # You then play this song forever
                mixer.music.play(-1)

            # When you click on the previous button, the previous song plays
            if evt.button == 1 and prevRect.collidepoint(mx, my) and song <= len(music):
                # If the song index number is greater than 0, subtract 1 from it
                if song >= 0:
                    song -= 1
                    # However if the song index is less than zero or -1, add 1 to it
                    if song == -1:
                        song += 1
                # Then load the previous song and play it
                #mixer.music.load(music[song])
                #mixer.music.play(-1)
                print("Why is this not wokring!")

            if evt.button == 1 and playRect.collidepoint(mx,
                                                         my) and music_clicked == False:  ## check if play is clicked and the choice is false
                #mixer.music.pause()  ## pause music
                print("Garabge!")
                music_clicked = True  ## set it to true so it can be clicked again

            elif evt.button == 1 and playRect.collidepoint(mx,
                                                           my) and music_clicked == True:  ## check if play is clicked and choice is true
                #mixer.music.unpause()  ## play from the point where paused (or unpause)
                print("Sometimes")
                music_clicked = False  ## set it to false to when clicked again, it is true

        if evt.type == MOUSEBUTTONUP:
            print("Mouse Up")
            # When the canvas is clicked on, the picture being taken of it is appended to
            # the undo list
            if mb[0] == 1:
                if canvasRect.collidepoint((mx, my)):
                    undo.append(canvas.copy())

            # When the undo button is clicked on, it blits the last item appended into the list
            # onto the screen
            if mb[0] == 1 and undoRect.collidepoint(mx, my):
                if len(undo) > 1:
                    redo.append(undo.pop())
                    canvas.blit(undo[-1], (0, 0))

            # On the other hand, when the redo button is clicked, it blits the last item taken
            # off of the screen that was blitted into the undo list and blits it back onto
            # the canvasRect screen
            if mb[0] == 1 and redoRect.collidepoint(mx, my):
                if len(redo) > 0:
                    undo.append(redo.pop())
                    canvas.blit(undo[-1], (0, 0))

    # When the fill button is clicked, it turns these thicknesses into zero which draws
    # a full shape for each of the following
    if mb[0] == 1 and fillRect.collidepoint(mx, my):
        polygonThickness = 0
        rectangleTH = 0
        circleTH = 0

    # When the unfill button is clicked, it returns the full thicknesses into 1 which draws
    # an unfilled shape for each of the following
    if mb[0] == 1 and unfillRect.collidepoint(mx, my):
        polygonThickness = 1
        rectangleTH = 1
        circleTH = 1

    ###Displaying positions and colour selection on screen###

    comicFont = font.SysFont("Saiyan-Sans", 28)  ## this is the font used for the texts

    # The variables below are to help display the x and y position of the mouse onto the screen
    # It takes the string of the int mouse values and turns them into pictures that can be
    # blitted onto the screen

    xpositionText = comicFont.render("X ~", True, BLACK)
    ypositionText = comicFont.render("Y ~", True, BLACK)
    xText = comicFont.render(str(mx), True, BLACK)
    yText = comicFont.render(str(my), True, BLACK)

    xpositionPic = xpositionText
    ypositionPic = ypositionText
    xPic = xText
    yPic = yText

    draw.rect(screen, (255, 215, 0), Rect(155, 615, 200, 30))
    draw.rect(screen, WHITE, Rect(155, 615, 200, 30), 2)
    screen.blit(xpositionPic, (165, 620))
    screen.blit(xPic, (200, 620))
    screen.blit(ypositionPic, (270, 620))
    screen.blit(yPic, (305, 620))

    # Below, the variables are turning the string of color code into a picture you can
    # blit on screen

    cmFont = font.SysFont("Saiyan-Sans", 24)  ## this is the font used for the texts
    clText = cmFont.render(str(col), True, WHITE)
    clPic = clText
    draw.rect(screen, (1, 120, 240), Rect(935, 810, 155, 30))
    draw.rect(screen, WHITE, Rect(935, 810, 155, 30), 2)
    screen.blit(clPic, (940, 815))

    # Same for below, except this is for displaying the radius and thickness of the tools

    cm1Font = font.SysFont("Saiyan-Sans", 24)  ## this is the font used for the texts
    cm2Font = font.SysFont("Saiyan-Sans", 30)  ## this is the font used for the texts
    c2Text = cm2Font.render(str(thickness), True, BLACK)
    c3Text = cm1Font.render("Radius/Thickness: ", True, BLACK)
    c2Pic = c2Text
    c3Pic = c3Text
    draw.rect(screen, (255, 215, 0), Rect(855, 390, 210, 40))
    draw.rect(screen, WHITE, Rect(855, 390, 210, 40), 2)
    screen.blit(c2Pic, (1010, 400))
    screen.blit(c3Pic, (860, 400))

    #####################################################

    ###Getting the expand button to work###

    # When the expand button is clicked, it blits two more buttons: tools and shapes
    # These do not appear unless the expand button is clicked

    if expandRect.collidepoint(mx, my) and ac4 == True:
        draw.rect(screen, GREEN, expandRect, 2)

        if mb[0] == 1 and expandRect.collidepoint(mx, my):
            c = True
            ac4 = False

            # ac4 then becomes false to stop the highlighting of the expand button
            # It also draws tools and shapes

            draw.rect(screen, (69, 162, 222), toolRect)
            draw.rect(screen, WHITE, toolRect, 2)
            tnrFont = font.SysFont("Arial", 25)
            toolPic = tnrFont.render("TOOLS", True, WHITE)
            screen.blit(toolPic, (73, 670))

            draw.rect(screen, (144, 46, 242), shapeRect)
            draw.rect(screen, WHITE, shapeRect, 2)
            tnrFont = font.SysFont("Arial", 25)
            shapePic = tnrFont.render("SHAPES", True, WHITE)
            screen.blit(shapePic, (67, 730))

    else:
        draw.rect(screen, (14, 111, 174), expandRect, 2)
        # This is just in case the mouse has not made contact with the button, it helps with
        # the highlighting function

    ##########################################

    ###Getting both the tool, shape, stamp buttons to work as well as the menu buttons###

    # Below are the highlighting of the tool,shape,stamp, and menu buttons
    # The way it works is if the mouse collides with the button, it highlights it a different
    # color. When the mosue is not colliding, it sets it back to its default color
    # The reason for the boolean variables are to ensure that the buttons don't highlight
    # when you hover above them right before the expand button is clicked
    # The same goes for the stamp button and the menu buttons

    if toolRect.collidepoint(mx, my) and c == True:
        draw.rect(screen, GREEN, toolRect, 2)

    elif c == True:
        draw.rect(screen, WHITE, toolRect, 2)

    if shapeRect.collidepoint(mx, my) and c == True:
        draw.rect(screen, GREEN, shapeRect, 2)

    elif c == True:
        draw.rect(screen, WHITE, shapeRect, 2)

    if stampRect.collidepoint(mx, my) and ac == True:
        draw.rect(screen, GREEN, stampRect, 2)

    else:
        draw.rect(screen, WHITE, stampRect, 2)

    if mnRect.collidepoint(mx, my) and mnC == True:
        draw.rect(screen, (107, 177, 246), mnRect, 2)

    elif mnC == True:
        draw.rect(screen, WHITE, mnRect, 2)

    if mn1Rect.collidepoint(mx, my) and mnC == True:
        draw.rect(screen, (107, 177, 246), mn1Rect, 2)

    elif mnC == True:
        draw.rect(screen, WHITE, mn1Rect, 2)

    if mn2Rect.collidepoint(mx, my) and mnC == True:
        draw.rect(screen, (107, 177, 246), mn2Rect, 2)

    elif mnC == True:
        draw.rect(screen, WHITE, mn2Rect, 2)

    if mn3Rect.collidepoint(mx, my) and mnC == True:
        draw.rect(screen, (107, 177, 246), mn3Rect, 2)

    elif mnC == True:
        draw.rect(screen, WHITE, mn3Rect, 2)

    if backgroundRect.collidepoint(mx, my) and ac3 == True:
        draw.rect(screen, GREEN, backgroundRect, 2)

    else:
        draw.rect(screen, WHITE, backgroundRect, 2)

    if mn4Rect.collidepoint(mx, my) and mnD == True:
        draw.rect(screen, (107, 177, 246), mn4Rect, 2)

    elif mnD == True:
        draw.rect(screen, WHITE, mn4Rect, 2)

    if mn5Rect.collidepoint(mx, my) and mnD == True:
        draw.rect(screen, (107, 177, 246), mn5Rect, 2)

    elif mnD == True:
        draw.rect(screen, WHITE, mn5Rect, 2)

    if mn6Rect.collidepoint(mx, my) and mnD == True:
        draw.rect(screen, (107, 177, 246), mn6Rect, 2)

    elif mnD == True:
        draw.rect(screen, WHITE, mn6Rect, 2)

    if mn7Rect.collidepoint(mx, my) and mnD == True:
        draw.rect(screen, (107, 177, 246), mn7Rect, 2)

    elif mnD == True:
        draw.rect(screen, WHITE, mn7Rect, 2)

    if mn8Rect.collidepoint(mx, my) and mnD == True:
        draw.rect(screen, (107, 177, 246), mn8Rect, 2)

    elif mnD == True:
        draw.rect(screen, WHITE, mn8Rect, 2)

    #################################################

    ###Setting up the c1 boolean to be true when clicked###

    if mb[0] == 1 and toolRect.collidepoint(mx, my) and c == True:
        c1 = True

    ####################################################

    ###Getting tools to be blitted when the tool button is clicked###
    if mb[0] == 1 and toolRect.collidepoint(mx, my) and c1 == True:
        # Only after the expand button has been clicked and only after the tool button has
        # been clicked, the actual tools are blitted on screen

        draw.rect(screen, BLACK, bgRect)
        draw.rect(screen, WHITE, bgRect, 2)

        draw.rect(screen, GREEN, pencilRect, 2)
        screen.blit(pencilPic, pencilRect)

        draw.rect(screen, GREEN, eraserRect, 2)
        screen.blit(eraserPic, eraserRect)

        draw.rect(screen, GREEN, markerRect, 2)
        screen.blit(markerPic, markerRect)

        draw.rect(screen, GREEN, paintbrushRect, 2)
        screen.blit(paintbrushPic, paintbrushRect)

        draw.rect(screen, GREEN, sprayRect, 2)
        screen.blit(sprayPic, sprayRect)

        draw.rect(screen, GREEN, highlighterRect, 2)
        screen.blit(highlighterPic, highlighterRect)

        draw.rect(screen, GREEN, mpenRect, 2)
        screen.blit(mpenPic, mpenRect)

    ###############################################################

    ###Setting up c2 boolean###

    if mb[0] == 1 and shapeRect.collidepoint(mx, my) and c == True:
        c2 = True

    ##########################

    ###Getting shapes to be blitted when shape button is clicked

    if mb[0] == 1 and shapeRect.collidepoint(mx, my) and c2 == True:
        # The same applies to the shapes
        # Only after the expand button has been clicked and only after the shapes button has
        # been clicked, the actual shapes are blitted on screen

        draw.rect(screen, BLACK, bg1Rect)
        draw.rect(screen, WHITE, bg1Rect, 2)

        draw.rect(screen, GREEN, lineRect, 2)
        screen.blit(linePic, lineRect)

        draw.rect(screen, GREEN, rectangleRect, 2)
        screen.blit(rectanglePic, rectangleRect)

        draw.rect(screen, GREEN, ellipseRect, 2)
        screen.blit(ellipsePic, ellipseRect)

        draw.rect(screen, GREEN, polygonRect, 2)
        screen.blit(polygonPic, polygonRect)

    ###########################################################

    ###Getting stamps to be blitted when button is clicked###

    if stampRect.collidepoint(mx, my) and mb[0] == 1 and ac2 == True:
        # The same case is true for the stamps as is the tools and shapes, but it's a little
        # different. When stamps is clicked, the first page of stamps are blitted
        # As well, the four menus that lead to all the other stamp pages are blitted

        c3 = True
        c4 = False
        mnC = True
        ac = False
        ac2 = False

        # The booleans dictate whether the stamps get highlighted, only if the the stamp button
        # is clicked as well as to not confuse it with the other tools and shapes

        draw.rect(screen, (94, 13, 246), mnRect)
        draw.rect(screen, WHITE, mnRect, 2)

        draw.rect(screen, (94, 13, 246), mn1Rect)
        draw.rect(screen, WHITE, mn1Rect, 2)

        draw.rect(screen, (94, 13, 246), mn2Rect)
        draw.rect(screen, WHITE, mn2Rect, 2)

        draw.rect(screen, (94, 13, 246), mn3Rect)
        draw.rect(screen, WHITE, mn3Rect, 2)

        draw.rect(screen, (46, 120, 242), bg2Rect)
        draw.rect(screen, WHITE, bg2Rect, 2)

        screen.blit(batmanLogoStampPic, batmanStampRect)
        draw.rect(screen, BLACK, batmanStampRect, 2)

        screen.blit(supermanLogoStampPic, supermanStampRect)
        draw.rect(screen, BLACK, supermanStampRect, 2)

        screen.blit(wwStampLogoPic, wwStampRect)
        draw.rect(screen, BLACK, wwStampRect, 2)

    if mb[0] == 1 and mnRect.collidepoint(mx, my) and mnC == True:
        c3 = True
        c4 = False
        c5 = False
        c6 = False

        # If the first menu button is clicked, the first page of stamps are blitted on screen
        # All the other menu pages are made false since each page is on top of each other
        # This is to not confuse the program and get different stamps
        # The booleans help tell the difference between each stamp page and stamp respectively

        draw.rect(screen, (138, 64, 237), mnRect)
        draw.rect(screen, WHITE, mnRect, 2)

        draw.rect(screen, (138, 64, 237), mn1Rect)
        draw.rect(screen, WHITE, mn1Rect, 2)

        draw.rect(screen, (138, 64, 237), mn2Rect)
        draw.rect(screen, WHITE, mn2Rect, 2)

        draw.rect(screen, (138, 64, 237), mn3Rect)
        draw.rect(screen, WHITE, mn3Rect, 2)

        draw.rect(screen, (46, 120, 242), bg2Rect)
        draw.rect(screen, WHITE, bg2Rect, 2)

        screen.blit(batmanLogoStampPic, batmanStampRect)
        draw.rect(screen, BLACK, batmanStampRect, 2)

        screen.blit(supermanLogoStampPic, supermanStampRect)
        draw.rect(screen, BLACK, supermanStampRect, 2)

        screen.blit(wwStampLogoPic, wwStampRect)
        draw.rect(screen, BLACK, wwStampRect, 2)

    if mb[0] == 1 and mn1Rect.collidepoint(mx, my) and mnC == True:
        c3 = False
        c5 = False
        c6 = False
        c4 = True

        # If the second menu button is clicked, the second page of stamps are blitted on screen

        draw.rect(screen, (245, 135, 243), bg2Rect)
        draw.rect(screen, WHITE, bg2Rect, 2)

        screen.blit(aquamanLogoStampPic, aquamanStampRect)
        draw.rect(screen, BLACK, aquamanStampRect, 2)

        screen.blit(flashLogoStampPic, flashStampRect)
        draw.rect(screen, BLACK, flashStampRect, 2)

        screen.blit(cyborgLogoStampPic, cyborgStampRect)
        draw.rect(screen, BLACK, cyborgStampRect, 2)

    if mb[0] == 1 and mn2Rect.collidepoint(mx, my) and mnC == True:
        c3 = False
        c4 = False
        c6 = False
        c5 = True

        # If the third menu button is clicked, the third page of stamps are blitted on screen

        draw.rect(screen, (241, 99, 73), bg2Rect)
        draw.rect(screen, WHITE, bg2Rect, 2)

        screen.blit(symbolLogo1Pic, bStampRect)
        draw.rect(screen, BLACK, bStampRect, 2)

        screen.blit(symbolLogo2Pic, sStampRect)
        draw.rect(screen, BLACK, sStampRect, 2)

        screen.blit(symbolLogo3Pic, wStampRect)
        draw.rect(screen, BLACK, wStampRect, 2)

    if mb[0] == 1 and mn3Rect.collidepoint(mx, my) and mnC == True:
        c3 = False
        c4 = False
        c5 = False
        c6 = True

        # If the fourth menu button is clicked, the fourth page of stamps are blitted on screen

        draw.rect(screen, (30, 245, 173), bg2Rect)
        draw.rect(screen, WHITE, bg2Rect, 2)

        screen.blit(symbolLogo4Pic, aStampRect)
        draw.rect(screen, BLACK, aStampRect, 2)

        screen.blit(symbolLogo5Pic, fStampRect)
        draw.rect(screen, BLACK, fStampRect, 2)

        screen.blit(symbolLogo6Pic, cStampRect)
        draw.rect(screen, BLACK, cStampRect, 2)

    if mb[0] == 1 and backgroundRect.collidepoint(mx, my) and ac3 == True:
        c7 = True
        mnD = True
        ac3 = False

        # Here the background button is clicked and blits the different backgrounds right on
        # top of each other. To differentiate between eack background, the menu buttons are also
        # blitted to correspond to each respective background

        screen.blit(dcAPic, dcRect)
        draw.rect(screen, GREEN, dcRect, 2)

        draw.rect(screen, (138, 64, 237), mn4Rect)
        draw.rect(screen, WHITE, mn4Rect, 2)

        draw.rect(screen, (138, 64, 237), mn5Rect)
        draw.rect(screen, WHITE, mn5Rect, 2)

        draw.rect(screen, (138, 64, 237), mn6Rect)
        draw.rect(screen, WHITE, mn6Rect, 2)

        draw.rect(screen, (138, 64, 237), mn7Rect)
        draw.rect(screen, WHITE, mn7Rect, 2)

        draw.rect(screen, (138, 64, 237), mn8Rect)
        draw.rect(screen, WHITE, mn8Rect, 2)

    if mb[0] == 1 and mn4Rect.collidepoint(mx, my) and mnD == True:
        c7 = True
        c8 = False
        c9 = False
        c10 = False
        c11 = False

        # If the first menu button is clicked, the first page of backgrounds will be blitted

        screen.blit(dcAPic, dcRect)
        draw.rect(screen, GREEN, dcRect, 2)

    if mb[0] == 1 and mn5Rect.collidepoint(mx, my) and mnD == True:
        c7 = False
        c8 = True
        c9 = False
        c10 = False
        c11 = False

        # If the second menu button is clicked, the second page of backgrounds will be blitted

        screen.blit(dc1APic, dc1Rect)
        draw.rect(screen, GREEN, dc1Rect, 2)

    if mb[0] == 1 and mn6Rect.collidepoint(mx, my) and mnD == True:
        c7 = False
        c8 = False
        c9 = True
        c10 = False
        c11 = False

        # If the third menu button is clicked, the third page of backgrounds will be blitted

        screen.blit(dc2APic, dc2Rect)
        draw.rect(screen, GREEN, dc2Rect, 2)

    if mb[0] == 1 and mn7Rect.collidepoint(mx, my) and mnD == True:
        c7 = False
        c8 = False
        c9 = False
        c10 = True
        c11 = False

        # If the fourth menu button is clicked, the fourth page of backgrounds will be blitted

        screen.blit(dc3APic, dc3Rect)
        draw.rect(screen, GREEN, dc3Rect, 2)

    if mb[0] == 1 and mn8Rect.collidepoint(mx, my) and mnD == True:
        c7 = False
        c8 = False
        c9 = False
        c10 = False
        c11 = True

        # If the fifth menu button is clicked, the fifth page of backgrounds will be blitted

        screen.blit(dc4APic, dc4Rect)
        draw.rect(screen, GREEN, dc4Rect, 2)

    #######################################################

    ###Setting up the MAIN TITLE###

    #  r   g   b   a
    draw.rect(titleBar, (69, 205, 242, 3), titleRect)
    # draws a grey rectangle onto the titleBar surface
    titleBar.blit(myText, (30, 0))  # writes DC on the TITLEBAR surface (not on the screen)
    #################relative to the titleBar surface

    screen.blit(titleBar, (150, 40))  # this actually blits the text on the screen
    screen.blit(logoPic, logoRect)
    draw.line(screen, (228, 240, 243), (147, 40), (700, 40), 5)
    draw.line(screen, (228, 240, 243), (155, 80), (700, 80), 5)
    draw.line(screen, (228, 240, 243), (700, 40), (700, 80), 5)

    ################################

    ###Drawing the rest of the rects
    ###These rects are separated depending upon the order they are to
    ###be blitted on screen

    # The rest of these rects are blitted here because they have a tool function but don't need
    # to be blitted via a special menu, so they get the regular treatment

    draw.rect(screen, GREEN, clearRect, 2)
    draw.rect(screen, GREEN, openRect, 2)
    draw.rect(screen, GREEN, saveRect, 2)
    draw.rect(screen, GREEN, undoRect, 2)
    draw.rect(screen, GREEN, redoRect, 2)

    screen.blit(fillPic, fillRect)
    draw.rect(screen, GREEN, fillRect, 2)

    screen.blit(unfillPic, unfillRect)
    draw.rect(screen, GREEN, unfillRect, 2)

    screen.blit(umpPic, umpRect)
    draw.rect(screen, GREEN, umpRect, 2)

    screen.blit(edPic, edRect)
    draw.rect(screen, GREEN, edRect, 2)

    screen.blit(playPic, playRect)
    draw.rect(screen, GREEN, playRect, 2)

    screen.blit(prevPic, prevRect)
    draw.rect(screen, GREEN, prevRect, 2)

    screen.blit(nextPic, nextRect)
    draw.rect(screen, GREEN, nextRect, 2)

    ###############################

    ########selecting the TOOLS

    # Here, each of the tools are selected via by being highlighted. Also, some of the tool
    # also have info being blitted onto the info box about their functionality

    if pencilRect.collidepoint(mx, my) and c1 == True:
        draw.rect(screen, YELLOW, pencilRect, 2)

    elif eraserRect.collidepoint(mx, my) and c1 == True:
        draw.rect(screen, YELLOW, eraserRect, 2)

    elif markerRect.collidepoint(mx, my) and c1 == True:
        draw.rect(screen, YELLOW, markerRect, 2)

    elif paintbrushRect.collidepoint(mx, my) and c1 == True:
        draw.rect(screen, YELLOW, paintbrushRect, 2)

    elif sprayRect.collidepoint(mx, my) and c1 == True:
        draw.rect(screen, YELLOW, sprayRect, 2)

    elif highlighterRect.collidepoint(mx, my) and c1 == True:
        draw.rect(screen, YELLOW, highlighterRect, 2)

    elif mpenRect.collidepoint(mx, my) and c1 == True:
        draw.rect(screen, YELLOW, mpenRect, 2)

    elif clearRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, clearRect, 2)

    elif undoRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, undoRect, 2)

        # Specifically, for this tool, the info rect is blitted with the info about the tool
        # on it, each with a name and description of what it does. Every tool has this.

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        uPic = tnrFont.render("UNDO", True, WHITE)
        screen.blit(uPic, (875, 100))

        tnrFont = font.SysFont("Times", 18)
        u1Pic = tnrFont.render("Undo your past action.", True, WHITE)
        screen.blit(u1Pic, (810, 150))

    elif redoRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, redoRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        rPic = tnrFont.render("REDO", True, WHITE)
        screen.blit(rPic, (875, 100))

        tnrFont = font.SysFont("Times", 18)
        r1Pic = tnrFont.render("Redo your past action.", True, WHITE)
        screen.blit(r1Pic, (810, 150))

    elif saveRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, saveRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        saPic = tnrFont.render("SAVE", True, WHITE)
        screen.blit(saPic, (875, 100))

        tnrFont = font.SysFont("Times", 18)
        sa1Pic = tnrFont.render("Save your masterpiece.", True, WHITE)
        screen.blit(sa1Pic, (810, 150))

    elif openRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, openRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        oPic = tnrFont.render("OPEN", True, WHITE)
        screen.blit(oPic, (875, 100))

        tnrFont = font.SysFont("Times", 18)
        o1Pic = tnrFont.render("Load a picture.", True, WHITE)
        screen.blit(o1Pic, (810, 150))

    elif fillRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, fillRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        uPic = tnrFont.render("FILL", True, WHITE)
        screen.blit(uPic, (900, 100))

        tnrFont = font.SysFont("Times", 18)
        u1Pic = tnrFont.render("I think this is self-explanatory.", True, WHITE)
        screen.blit(u1Pic, (810, 150))

    elif unfillRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, unfillRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        uPic = tnrFont.render("UNFILL", True, WHITE)
        screen.blit(uPic, (875, 100))

        tnrFont = font.SysFont("Times", 18)
        u1Pic = tnrFont.render("This is also self-explanatory.", True, WHITE)
        screen.blit(u1Pic, (810, 150))

    elif umpRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, umpRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 30)
        uPic = tnrFont.render("ULTIMATE MAGIC PEN", True, WHITE)
        screen.blit(uPic, (815, 100))

        tnrFont = font.SysFont("Times", 18)
        u1Pic = tnrFont.render("Unleash your magic artistic power.", True, WHITE)
        screen.blit(u1Pic, (810, 150))

    elif edRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, edRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        uPic = tnrFont.render("EYE~DROPPER", True, WHITE)
        screen.blit(uPic, (825, 100))

        tnrFont = font.SysFont("Times", 18)
        u1Pic = tnrFont.render("Click anywhere to select a color.", True, WHITE)
        screen.blit(u1Pic, (810, 150))

    elif playRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, playRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        uPic = tnrFont.render("PLAY/PAUSE", True, WHITE)
        screen.blit(uPic, (845, 100))

        tnrFont = font.SysFont("Times", 18)
        u1Pic = tnrFont.render("Click here to pause or play music.", True, WHITE)
        screen.blit(u1Pic, (810, 150))

    elif nextRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, nextRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        uPic = tnrFont.render("NEXT", True, WHITE)
        screen.blit(uPic, (900, 100))

        tnrFont = font.SysFont("Times", 18)
        u1Pic = tnrFont.render("Click here for the next song.", True, WHITE)
        screen.blit(u1Pic, (810, 150))

    elif prevRect.collidepoint(mx, my):
        draw.rect(screen, YELLOW, prevRect, 2)

        draw.rect(screen, (9, 154, 248), infoRect)
        draw.rect(screen, WHITE, infoRect, 5)
        draw.rect(screen, BLUE, infoRect, 2)

        tnrFont = font.SysFont("Arial", 40)
        uPic = tnrFont.render("PREVIOUS", True, WHITE)
        screen.blit(uPic, (855, 100))

        tnrFont = font.SysFont("Times", 18)
        u1Pic = tnrFont.render("Click here for the previous song.", True, WHITE)
        screen.blit(u1Pic, (810, 150))

    elif c1 == True:
        draw.rect(screen, GREEN, pencilRect, 2)
        draw.rect(screen, GREEN, eraserRect, 2)
        draw.rect(screen, GREEN, markerRect, 2)
        draw.rect(screen, GREEN, paintbrushRect, 2)
        draw.rect(screen, GREEN, sprayRect, 2)
        draw.rect(screen, GREEN, highlighterRect, 2)
        draw.rect(screen, GREEN, mpenRect, 2)

    #print(tool)

    ###############################

    ###Selecting the Stamps###

    # Here, each of the stamps are selected via by being highlighted. None of the stamps have
    # any info being displayed about them

    if batmanStampRect.collidepoint(mx, my) and c3 == True:
        draw.rect(screen, YELLOW, batmanStampRect, 2)

    elif supermanStampRect.collidepoint(mx, my) and c3 == True:
        draw.rect(screen, YELLOW, supermanStampRect, 2)

    elif wwStampRect.collidepoint(mx, my) and c3 == True:
        draw.rect(screen, YELLOW, wwStampRect, 2)

    elif c3 == True:
        # If the mouse is not colliding with any of the stamps, the rect's border is the default
        # color. Every stamp has this along with it's corresponding boolean to separate it from
        # the rest of the stamps and their pages
        draw.rect(screen, BLACK, batmanStampRect, 2)
        draw.rect(screen, BLACK, supermanStampRect, 2)
        draw.rect(screen, BLACK, wwStampRect, 2)

    elif aquamanStampRect.collidepoint(mx, my) and c4 == True:
        draw.rect(screen, YELLOW, aquamanStampRect, 2)

    elif flashStampRect.collidepoint(mx, my) and c4 == True:
        draw.rect(screen, YELLOW, flashStampRect, 2)

    elif cyborgStampRect.collidepoint(mx, my) and c4 == True:
        draw.rect(screen, YELLOW, cyborgStampRect, 2)

    elif c4 == True:
        draw.rect(screen, BLACK, aquamanStampRect, 2)
        draw.rect(screen, BLACK, flashStampRect, 2)
        draw.rect(screen, BLACK, cyborgStampRect, 2)

    elif bStampRect.collidepoint(mx, my) and c5 == True:
        draw.rect(screen, YELLOW, bStampRect, 2)

    elif sStampRect.collidepoint(mx, my) and c5 == True:
        draw.rect(screen, YELLOW, sStampRect, 2)

    elif wStampRect.collidepoint(mx, my) and c5 == True:
        draw.rect(screen, YELLOW, wStampRect, 2)

    elif c5 == True:
        draw.rect(screen, BLACK, bStampRect, 2)
        draw.rect(screen, BLACK, sStampRect, 2)
        draw.rect(screen, BLACK, wStampRect, 2)

    elif aStampRect.collidepoint(mx, my) and c6 == True:
        draw.rect(screen, YELLOW, aStampRect, 2)

    elif fStampRect.collidepoint(mx, my) and c6 == True:
        draw.rect(screen, YELLOW, fStampRect, 2)

    elif cStampRect.collidepoint(mx, my) and c6 == True:
        draw.rect(screen, YELLOW, cStampRect, 2)

    elif c6 == True:
        draw.rect(screen, BLACK, aStampRect, 2)
        draw.rect(screen, BLACK, fStampRect, 2)
        draw.rect(screen, BLACK, cStampRect, 2)

    if dcRect.collidepoint(mx, my) and c7 == True:
        draw.rect(screen, YELLOW, dcRect, 2)

    # These stamps are a little different, these stamps are actually the backgrounds from the
    # the background button, but they still work the same way

    elif c7 == True:
        draw.rect(screen, GREEN, dcRect, 2)

    elif dc1Rect.collidepoint(mx, my) and c8 == True:
        draw.rect(screen, YELLOW, dc1Rect, 2)

    elif c8 == True:
        draw.rect(screen, GREEN, dc1Rect, 2)

    elif dc2Rect.collidepoint(mx, my) and c9 == True:
        draw.rect(screen, YELLOW, dc2Rect, 2)

    elif c9 == True:
        draw.rect(screen, GREEN, dc2Rect, 2)

    elif dc3Rect.collidepoint(mx, my) and c10 == True:
        draw.rect(screen, YELLOW, dc3Rect, 2)

    elif c10 == True:
        draw.rect(screen, GREEN, dc3Rect, 2)

    elif dc4Rect.collidepoint(mx, my) and c11 == True:
        draw.rect(screen, YELLOW, dc4Rect, 2)

    elif c11 == True:
        draw.rect(screen, GREEN, dc4Rect, 2)

    ###Selecting the shapes###

    if lineRect.collidepoint(mx, my) and c2 == True:
        draw.rect(screen, YELLOW, lineRect, 2)

    elif rectangleRect.collidepoint(mx, my) and c2 == True:
        draw.rect(screen, YELLOW, rectangleRect, 2)

    elif ellipseRect.collidepoint(mx, my) and c2 == True:
        draw.rect(screen, YELLOW, ellipseRect, 2)

    elif polygonRect.collidepoint(mx, my) and c2 == True:
        draw.rect(screen, YELLOW, polygonRect, 2)

    elif c2 == True:
        draw.rect(screen, GREEN, lineRect, 2)
        draw.rect(screen, GREEN, rectangleRect, 2)
        draw.rect(screen, GREEN, ellipseRect, 2)
        draw.rect(screen, GREEN, polygonRect, 2)

    ##########################

    ###Checking left click on tools###

    # Each of the tools are checked to see if they are being clicked on by the left mouse button
    # If they are, the tool selected gets update via the tool string (tool="") and the info
    # rect is displayed with their description

    if mb[0] == 1 and c1 == True:  ##checking left click
        if pencilRect.collidepoint(mx, my):
            tool = "pencil"
            stamp = "no stamp"
            shape = "no shape"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            pPic = tnrFont.render("PENCIL", True, WHITE)
            screen.blit(pPic, (875, 100))

            tnrFont = font.SysFont("Times", 18)
            p1Pic = tnrFont.render("Draw, man, draw!", True, WHITE)
            screen.blit(p1Pic, (810, 150))

        elif eraserRect.collidepoint(mx, my):
            tool = "eraser"
            stamp = "no stamp"
            shape = "no shape"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            ePic = tnrFont.render("ERASER", True, WHITE)
            screen.blit(ePic, (875, 100))

            tnrFont = font.SysFont("Times", 18)
            e1Pic = tnrFont.render("Erase all those bo-boos.", True, WHITE)
            e1Pic2 = tnrFont.render("Scroll up/down to change thickness.", True, WHITE)
            screen.blit(e1Pic, (810, 150))
            screen.blit(e1Pic2, (810, 170))

        elif markerRect.collidepoint(mx, my):
            tool = "marker"
            stamp = "no stamp"
            shape = "no shape"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            mPic = tnrFont.render("MARKER", True, WHITE)
            screen.blit(mPic, (875, 100))

            tnrFont = font.SysFont("Times", 18)
            m1Pic = tnrFont.render("I will mark you up.", True, WHITE)
            m1Pic2 = tnrFont.render("Scroll up/down to change radius.", True, WHITE)
            screen.blit(m1Pic, (810, 150))
            screen.blit(m1Pic2, (810, 170))

        elif paintbrushRect.collidepoint(mx, my):
            tool = "paintbrush"
            stamp = "no stamp"
            shape = "no shape"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            pbPic = tnrFont.render("PAINT BRUSH", True, WHITE)
            screen.blit(pbPic, (845, 100))

            tnrFont = font.SysFont("Times", 18)
            pb1Pic = tnrFont.render("Paint to your heart's desire.", True, WHITE)
            screen.blit(pb1Pic, (810, 150))

        elif sprayRect.collidepoint(mx, my):
            tool = "spray"
            stamp = "no stamp"
            shape = "no shape"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            sPic = tnrFont.render("SPRAY CAN", True, WHITE)
            screen.blit(sPic, (855, 100))

            tnrFont = font.SysFont("Times", 18)
            s1Pic = tnrFont.render("You are now a street artist.", True, WHITE)
            s1Pic2 = tnrFont.render("Scroll up/down to change radius.", True, WHITE)
            screen.blit(s1Pic, (810, 150))
            screen.blit(s1Pic2, (810, 170))

        elif highlighterRect.collidepoint(mx, my):
            tool = "highlighter"
            stamp = "no stamp"
            shape = "no shape"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            hPic = tnrFont.render("HIGHLIGHTER", True, WHITE)
            screen.blit(hPic, (835, 100))

            tnrFont = font.SysFont("Times", 18)
            h1Pic = tnrFont.render("Highlight it all!", True, WHITE)
            screen.blit(h1Pic, (810, 150))

        elif mpenRect.collidepoint(mx, my):
            tool = "magic pen"
            stamp = "no stamp"
            shape = "no shape"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            mpPic = tnrFont.render("MAGIC PEN", True, WHITE)
            screen.blit(mpPic, (845, 100))

            tnrFont = font.SysFont("Times", 18)
            mp1Pic = tnrFont.render("It's a magic pen, whohoo!", True, WHITE)
            screen.blit(mp1Pic, (810, 150))

    if umpRect.collidepoint(mx, my) and mb[0] == 1:
        tool = "ultimate magic pen"
        stamp = "no stamp"
        shape = "no shape"


    elif edRect.collidepoint(mx, my) and mb[0] == 1:
        tool = "eye-dropper"
        stamp = "no stamp"
        shape = "no shape"

    #################################

    ###Checking left click on Stamps###

    # The same that was happening for the block of code selecting the tools, the same is
    # happening but for the stamps instead

    if mb[0] == 1 and c3 == True:

        if batmanStampRect.collidepoint(mx, my):
            stamp = "batmanStamp"
            tool = "no tool"
            shape = "no shape"

        elif supermanStampRect.collidepoint(mx, my):
            stamp = "supermanStamp"
            tool = "no tool"
            shape = "no shape"

        elif wwStampRect.collidepoint(mx, my):
            stamp = "wwStamp"
            tool = "no tool"
            shape = "no shape"

    if mb[0] == 1 and c4 == True:

        if aquamanStampRect.collidepoint(mx, my):
            stamp = "aquamanStamp"
            tool = "no tool"
            shape = "no shape"

        elif flashStampRect.collidepoint(mx, my):
            stamp = "flashStamp"
            tool = "no tool"
            shape = "no shape"

        elif cyborgStampRect.collidepoint(mx, my):
            stamp = "cyborgStamp"
            tool = "no tool"
            shape = "no shape"

    if mb[0] == 1 and c5 == True:

        if bStampRect.collidepoint(mx, my):
            stamp = "bLogo"
            tool = "no tool"
            shape = "no shape"

        elif sStampRect.collidepoint(mx, my):
            stamp = "sLogo"
            tool = "no tool"
            shape = "no shape"

        elif wStampRect.collidepoint(mx, my):
            stamp = "wLogo"
            tool = "no tool"
            shape = "no shape"

    if mb[0] == 1 and c6 == True:

        if aStampRect.collidepoint(mx, my):
            stamp = "aLogo"
            tool = "no tool"
            shape = "no shape"

        elif fStampRect.collidepoint(mx, my):
            stamp = "fLogo"
            tool = "no tool"
            shape = "no shape"

        elif cStampRect.collidepoint(mx, my):
            stamp = "cLogo"
            tool = "no tool"
            shape = "no shape"

    if mb[0] == 1 and c7 == True:

        if dcRect.collidepoint(mx, my):
            stamp = "dc1"
            tool = "no tool"
            shape = "no shape"
            pos = 0

    if mb[0] == 1 and c8 == True:

        if dc1Rect.collidepoint(mx, my):
            stamp = "dc2"
            tool = "no tool"
            shape = "no shape"
            pos = 1

    if mb[0] == 1 and c9 == True:

        if dc2Rect.collidepoint(mx, my):
            stamp = "dc3"
            tool = "no tool"
            shape = "no shape"
            pos = 2

    if mb[0] == 1 and c10 == True:

        if dc3Rect.collidepoint(mx, my):
            stamp = "dc4"
            tool = "no tool"
            shape = "no shape"
            pos = 3

    if mb[0] == 1 and c11 == True:

        if dc4Rect.collidepoint(mx, my):
            stamp = "dc5"
            tool = "no tool"
            shape = "no shape"
            pos = 4

    ###############################

    ###Selecting the Shapes###

    # Likewise, what was happening for the tools and stamps, is happening to the shapes as well
    # I decided to split them up to make a little whitespace and better organize each of the
    # functions dealing with separate tools, stamps, and shapes

    if mb[0] == 1 and c2 == True:
        if lineRect.collidepoint(mx, my):
            shape = "line"
            stamp = "no stamp"
            tool = "no tool"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            lPic = tnrFont.render("LINE", True, WHITE)
            screen.blit(lPic, (900, 100))

            tnrFont = font.SysFont("Times", 18)
            l1Pic = tnrFont.render("Stretch them lines.", True, WHITE)
            u1Pic2 = tnrFont.render("Scroll up/down to change thickness.", True, WHITE)
            screen.blit(l1Pic, (810, 150))
            screen.blit(u1Pic2, (810, 170))

        if rectangleRect.collidepoint(mx, my):
            shape = "rectangle"
            stamp = "no stamp"
            tool = "no tool"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            uPic = tnrFont.render("RECTANGLE", True, WHITE)
            screen.blit(uPic, (835, 100))

            tnrFont = font.SysFont("Times", 18)
            u1Pic = tnrFont.render("Use this to draw squarish rectangles.", True, WHITE)
            u1Pic2 = tnrFont.render("Scroll up/down to change thickness.", True, WHITE)
            screen.blit(u1Pic, (810, 150))
            screen.blit(u1Pic2, (810, 170))

        if ellipseRect.collidepoint(mx, my):
            shape = "ellipse"
            stamp = "no stamp"
            tool = "no tool"

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            uPic = tnrFont.render("CIRCLE", True, WHITE)
            screen.blit(uPic, (875, 100))

            tnrFont = font.SysFont("Times", 18)
            u1Pic = tnrFont.render("This draws ellipses AKA circles.", True, WHITE)
            u1Pic2 = tnrFont.render("Scroll up/down to change radius.", True, WHITE)
            screen.blit(u1Pic, (810, 150))
            screen.blit(u1Pic2, (810, 170))

        if polygonRect.collidepoint(mx, my):
            shape = "polygon"
            stamp = "no stamp"
            tool = "no tool"
            points = []
            polygon_start = True

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            uPic = tnrFont.render("POLYGON", True, WHITE)
            screen.blit(uPic, (875, 100))

            tnrFont = font.SysFont("Times", 18)
            u1Pic = tnrFont.render("This draws a polygon.", True, WHITE)
            u1Pic2 = tnrFont.render("To fully connect this polygon,", True, WHITE)
            u1Pic3 = tnrFont.render("drag your line to the first point.", True, WHITE)
            screen.blit(u1Pic, (810, 150))
            screen.blit(u1Pic2, (810, 170))
            screen.blit(u1Pic3, (810, 190))

    #print(shape)

    #######################

    ###using the TOOLS
    
    ###will need to update or get rid of music player
    if mb[0] == 1:
        if canvasRect.collidepoint(mx, my):  # if the tools are clicked and the canvas is clicked
            screen.set_clip(canvasRect)  # only the canvas can be "updated"

            if tool == "pencil":
                draw.line(screen, col, (omx, omy), (mx, my), 3)  # draws a line from a beginning position
                # to the ending position via mouse

            if tool == "eraser":

                if pos == 4:
                    # If the screen is a white background, which is what pos==4 is, use the regular
                    # eraser which is the white circle being drawn on top
                    dx = mx - omx  # horizontal distance
                    dy = my - omy  # vertical distance
                    dist = int(sqrt(dx ** 2 + dy ** 2))
                    for i in range(1, dist + 1):
                        cx = int(omx + i * dx / dist)
                        cy = int(omy + i * dy / dist)
                        draw.circle(screen, WHITE, (cx, cy), eraserRadius)

                else:
                    # However, if the background is not a white screen,draw the background's
                    # pixel's depending on mouse location without erasing the background
                    # I decided to use this method instead of the other because it used only
                    # one line and didn't need the background lists.
                    screen.blit(backgrounds[loc], (mx, my), pygame.Rect(mx - 180, my - 100, eraserRadius, eraserRadius))

                    # However, I still know how to use the method you taught us, if you were to
                    # comment out the other way above, and use the one below, they both work

                    # erasing=backgrounds2[pos].subsurface((mx-180,my-100,50,50))
                    # screen.blit(erasing,(mx,my))

            if tool == "marker":
                dx = mx - omx  # horizontal distance
                dy = my - omy  # vertical distance
                dist = int(sqrt(dx ** 2 + dy ** 2))  # using distance formula to find distance between points
                for i in range(1, dist + 1):  # drawing multiple circle to fill in gaps
                    cx = int(omx + i * dx / dist)
                    cy = int(omy + i * dy / dist)
                    draw.circle(screen, col, (cx, cy), markerRadius)

            if shape == "line":
                screen.blit(backPic, (180, 100))  # drawing the background
                # start  #current
                draw.line(screen, col, (sx, sy), (mx, my), thickness)

            if shape == "rectangle":
                screen.blit(backPic, (180, 100))

                distx = mx - sx  # Finding distance relative to mx,my
                disty = my - sy

                if t % 2 == 0:  # if the thickness has no remainders, add 1 to fill it up
                    t += 1

                # When the actual rectangle is being drawn, the coordinates match up through sx,sy
                draw.rect(screen, col, Rect(sx, sy, distx, disty), t)

                ### to add the squares to the end of the rectangle
                # these little squares fill up the corners of the rectangle that is being drawn
                draw.rect(screen, col, Rect(sx - (t / 2) + 1, sy - (t / 2) + 1, t, t), 0)
                draw.rect(screen, col, Rect((sx + distx) - (t / 2) - (1 / 2), sy - (t / 2) + 1, t, t), 0)
                draw.rect(screen, col, Rect(sx - (t / 2) + 1, (sy + disty) - (t / 2) - (1 / 2), t, t), 0)
                draw.rect(screen, col, Rect((sx + distx) - (t / 2), (sy + disty) - (t / 2), t, t), 0)

                if rectangleTH == 0:
                    # When the fill button is clicked, draw a rectangle with a full shape
                    draw.rect(screen, col, Rect(sx, sy, distx, disty), 0)

            if shape == "ellipse":
                # backPic (or background) is blitted to draw one point on the background
                # and keep it there so it can be "remembered" and connected to more points
                # whether it be through the rectangle, line, ellipse or polygon
                screen.blit(backPic, (180, 100))

                distanceX = (mx - sx)  # Distance relative to mx,my
                distanceY = (my - sy)

                # This is a interesting way I found to draw an ellipse, in which you take a
                # rectangle and its corners and curve them to make an ellipse, that's what the
                # normalize function does

                try:
                    for i in range(4):
                        # As for the multiple rects, it's to fill up the dots in the circle
                        # when they become normalized
                        ellRect = Rect(sx + i, sy, distanceX, distanceY)
                        ellRect = Rect(sx - i, sy, distanceX, distanceY)
                        ellRect = Rect(sx, sy + i, distanceX, distanceY)
                        ellRect = Rect(sx, sy - i, distanceX, distanceY)
                        ellRect.normalize()

                        draw.ellipse(screen, col, ellRect, circleThickness)

                    if circleTH == 0:
                        draw.ellipse(screen, col, ellRect)
                        # If the fill button is clicked, draw an ellipse with full shape

                except:
                    # This is to prevent the program from crashing when the ellipse does not
                    # have an existent radius
                    pass

            if tool == "paintbrush":
                dx = mx - omx  # horizontal distance
                dy = my - omy  # vertical distance
                dist = int(sqrt(dx ** 2 + dy ** 2))
                for i in range(1, dist + 1):  # filling in the gaps for the circle
                    cx = int(omx + i * dx / dist)
                    cy = int(omy + i * dy / dist)
                    for dx in range(-5, 6, 5):  ###-20 -10 0 10 20
                        # With multiple circles and layers and without gaps,
                        # it gives the paintbrush tool an effect that is similar
                        # to that of an actual paintbrush
                        draw.circle(screen, col, (cx + dx, cy - 5), 2, 0)  ###top 5 circles
                        draw.circle(screen, col, (cx + dx, cy + 5), 2, 0)  ##bottom 5 circles
                display.flip()

            if tool == "spray":
                for i in range(10):
                    x = randint(-1 * r, r)  # This is taking random x locations to blit the mini circles
                    ydist = int((r ** 2 - x ** 2) ** (0.5))  # Finding distance between points
                    y = randint((-1) * ydist, ydist)
                    xpos = x + mx
                    ypos = y + my
                    screen.set_at((xpos, ypos), col)  # drawing those mini circles at the mouse position
                    # with the color I have selected

            if tool == "highlighter":
                if mx != omx or my != omy:  # checking if there is movement
                    if mb[0] == 1:
                        screen.blit(brushHead, (mx - 10, my - 10))  # this is where it uses the alpha
                    if mb[2] == 1:
                        screen.blit(eraserHead, (mx - 20, my - 20))

            if tool == "magic pen":
                dist = ((mx - 400) ** 2 + (my - 300) ** 2) ** 0.5
                dx = mx - omx  # horizontal distance
                dy = my - omy  # vertical distance
                distF = int(sqrt(dx ** 2 + dy ** 2))  # filling the gaps made by the circles
                for i in range(1, distF + 1):
                    cx = int(omx + i * dx / distF)
                    cy = int(omy + i * dy / distF)
                    draw.circle(screen, col, (cx, cy), int(dist / 20))

            if tool == "ultimate magic pen":
                dist = ((mx - 400) ** 2 + (my - 300) ** 2) ** 0.5
                dx = mx - omx  # horizontal distance
                dy = my - omy  # vertical distance
                distF = int(sqrt(dx ** 2 + dy ** 2))
                rc = (randint(0, 255), randint(0, 255), randint(0, 255))  # random colour
                for i in range(1, distF + 1):  # Filling in the gaps
                    cx = int(omx + i * dx / distF)
                    cy = int(omy + i * dy / distF)
                    draw.circle(screen, rc, (cx, cy), int(dist / 10))

            # For each of the stamps, the program uses the backPic (or background) to create
            # image that doesn't leave a trail and stops when you let go of the left click
            # As for the backgrounds, they are blitted on screen when clicked on

            if stamp == "batmanStamp":
                screen.blit(backPic, (180, 100))
                screen.blit(myStamp, (mx - adjX, my - adjY))  # drawing Batman

            if stamp == "supermanStamp":
                screen.blit(backPic, (180, 100))
                screen.blit(sStamp, (mx - adjX, my - adjY))  # drawing Superman

            if stamp == "wwStamp":
                screen.blit(backPic, (180, 100))
                screen.blit(wwStamp, (mx - adjX, my - adjY))  # drawing Wonder Woman

            if stamp == "aquamanStamp":
                screen.blit(backPic, (180, 100))
                screen.blit(aquamanStamp, (mx - adjX, my - adjY))  # drawing Aquaman

            if stamp == "flashStamp":
                screen.blit(backPic, (180, 100))
                screen.blit(flashStamp, (mx - adjX, my - adjY))  # drawing Flash

            if stamp == "cyborgStamp":
                screen.blit(backPic, (180, 100))
                screen.blit(cyborgStamp, (mx - adjX, my - adjY))  # drawing Cyborg

            if stamp == "bLogo":
                screen.blit(backPic, (180, 100))
                screen.blit(bSymbolPic, (mx - adjX, my - adjY))  # drawing Batman logo

            if stamp == "sLogo":
                screen.blit(backPic, (180, 100))
                screen.blit(sSymbolPic, (mx - adjX, my - adjY))  # drawing Superman logo

            if stamp == "wLogo":
                screen.blit(backPic, (180, 100))
                screen.blit(wSymbolPic, (mx - adjX, my - adjY))  # drawing Wonder Woman logo

            if stamp == "aLogo":
                screen.blit(backPic, (180, 100))
                screen.blit(aSymbolPic, (mx - adjX, my - adjY))  # drawing Aquaman logo

            if stamp == "fLogo":
                screen.blit(backPic, (180, 100))
                screen.blit(fSymbolPic, (mx - adjX, my - adjY))  # drawing Flash logo

            if stamp == "cLogo":
                screen.blit(backPic, (180, 100))
                screen.blit(cSymbolPic, (mx - adjX, my - adjY))  # drawing Cyborg logo

            screen.set_clip(None)  # modify everything

        ###Blitting backgrounds###

        if stamp == "dc1":
            screen.blit(dcPic, canvasRect)
            loc = 0

        if stamp == "dc2":
            screen.blit(dc1Pic, canvasRect)
            loc = 1

        if stamp == "dc3":
            screen.blit(dc2Pic, canvasRect)
            loc = 2

        if stamp == "dc4":
            screen.blit(dc3Pic, canvasRect)
            loc = 3

        if stamp == "dc5":
            screen.blit(dc4Pic, canvasRect)
            loc = 4

        ##########################

    # 1-step tools
    if click:
        if clearRect.collidepoint(mx, my):
            screen.blit(backgrounds[loc], canvasRect)  # clear the canvas
            # It clears the canvas in regard to the index location of loc corresponding to the
            # backgrounds list near the beginning of the program
            print("clearing the canvas")

            draw.rect(screen, (9, 154, 248), infoRect)
            draw.rect(screen, WHITE, infoRect, 5)
            draw.rect(screen, BLUE, infoRect, 2)

            tnrFont = font.SysFont("Arial", 40)
            cPic = tnrFont.render("CLEAR", True, WHITE)
            screen.blit(cPic, (875, 100))

            tnrFont = font.SysFont("Times", 18)
            c1Pic = tnrFont.render("Clearing the canvas!", True, WHITE)
            screen.blit(c1Pic, (810, 150))

        if saveRect.collidepoint(mx, my):

            fname = filedialog.asksaveasfilename(defaultextension=".png")
            # asks the user to enter the file name they would like to save as
            image.save(screen.subsurface(canvasRect), fname)

            '''
            try:
                fname = filedialog.asksaveasfilename(defaultextension=".png")
                # asks the user to enter the file name they would like to save as
                image.save(screen.subsurface(canvasRect), fname)

                #####if the user hits CANCEL don't try to save the image

            except:
                print("saving error")
                # pass #prevent crashing
            '''
            
        ###Still broken...need to wrap up quick
        
        #################YOU NEED TO FINISH open
        if openRect.collidepoint(mx, my):
            try:
                fname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
                print(fname)
                fnamePic = image.load(fname)
                newfnamePic = transform.scale(fnamePic, (200, 200))
                screen.subsurface(canvasRect).blit(newfnamePic, (225, 100))
                ########instead of just printing the filename
                ### load the image and show it in the canvas area
                ####if the picture is larger than the canvas
                ####scale the picture, so the user can see the entire picture
            except:
                print("Loading error")

    ###changing the colour
    if mb[0] == 1:
        if wheelRect.collidepoint(mx, my):
            col = screen.get_at((mx, my))  # get the color of the pixels the mouse is at
            print(col)

        screen.set_clip(None)

    if shape == "polygon" and canvasRect.collidepoint(mx, my):
        if len(points) >= 1:
            screen.blit(backPic, (180, 100))
            snap_x, snap_y = points[0]  # finding distance between all the points to close polygon shape
            if hypot(snap_x - mx, snap_y - my) < 10:  # calculating distance between points
                omx, omy = snap_x, snap_y
                if len(points) >= 3:  # If the number of points (points array) is greater than or equal
                    # to three, done is then True which means the polygon can take shape. Otherwise,
                    # you can't make a shape with only two points, that would make done false
                    done = True
                    if polygonThickness == 0:
                        # if the fill button is pressed, draw a polygon with a full shape
                        draw.polygon(screen, col, points, 0)
            # otherwise, just draw anti-aliasing lines which are much smoother
            draw.aaline(screen, col, points[len(points) - 1], (omx, omy), 5)

    if tool == "eye-dropper" and mb[0] == 1:
        col = screen.get_at((mx, my))  # takes the color of the pixels the mouse it at

    omx = mx
    omy = my

    display.flip()
quit()  # closes out pygame window
sys.exit()

