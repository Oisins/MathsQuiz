# -*- coding: cp1252 -*-
import pygame
import sys
import random
from lib.screens import intro as Screen
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Oisin\'s Maths Quiz')

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
FPS = 10
fpsclock = pygame.time.Clock()
'''#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
BLUE         = (  0,   0, 255)
YELLOW       = (255, 255,   0)


currentScreen = "introScreen"
name = ""
difficulty = 1
points = [0, 0, 0, 0]
qnum = 1'''
#setup end





def text(text, x, y, fontsize, color):
    fontObj = pygame.font.Font('freesansbold.ttf', int(fontsize))
    textSurfaceObj = fontObj.render(str(text), True, color, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = x, y
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

'''def button(text, color, x, y, hight, width, FONTSIZE = 20):
    fontObj = pygame.font.Font('freesansbold.ttf', FONTSIZE)
    button = pygame.draw.rect(DISPLAYSURF, color, (x, y, width, hight))
    button.topleft = (x, y)
    textSurfaceObj = fontObj.render(str(text), True, BLACK, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = button.center
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    return button'''


class Button:

    def __init__(self, text, color, x, y, hight, width, FONTSIZE = 20):
        self.text, self.color, self.x, self.y, self.hight, self.width = text, color, x, y, hight, width
        self.fontObj = pygame.font.Font('freesansbold.ttf', FONTSIZE)
        self.obj = None

    def update(self):
        self.obj = pygame.draw.rect(DISPLAYSURF, self.color, (self.x, self.y, self.width, self.hight))
        self.obj.topleft = (self.x, self.y)
        textSurfaceObj = self.fontObj.render(str(self.text), True, BLACK, self.color)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = self.obj.center
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    def setColor(self, color):
        self.color = color


class nameSelect():    
    def __init__(self):
        self.name = ""

    def update(self):
        text('Enter Your name to begin:', WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 50, 20, WHITE)
        text(''.join(self.name).title(), WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 20, WHITE)
        pygame.draw.line(DISPLAYSURF, BLUE, (200, WINDOWHEIGHT / 2 + 7),(WINDOWWIDTH - 200, WINDOWHEIGHT / 2 + 7) ,2)
        text('(Then press Enter)', WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 50, 20, WHITE)

    def keyUp(self, key):
        global name
        if key == K_RETURN and len(self.name) > 0: # Confirm input and go the next screen
            name = self.name
            gameloop.setScreen("askQuestion")
        elif key == K_BACKSPACE: # If Backspace delete last Letter
            self.name = self.name[:-1]
            # key >= 97 and key <= 122
        elif 97 >= key <= 122 and key <= 122: # If Letter add it to the Name String
            self.name += pygame.key.name(key)
    def mouseUp(self, pos):
        pass


class questionGen():
    def __init__(self):
        self.numGen = [(10,50),(30,150),(100,1000)]

    def addition(self):
        global difficulty
        num1 = random.randint(self.numGen[difficulty - 1][0], self.numGen[difficulty - 1][1])
        num2 = random.randint(self.numGen[difficulty - 1][0], self.numGen[difficulty - 1][1])
        answer = num1 + num2
        return num1, num2, answer

    def subtraction(self):
        global difficulty
        num1 = random.randint(self.numGen[difficulty - 1][0], self.numGen[difficulty - 1][1])
        num2 = random.randint(self.numGen[difficulty - 1][0], self.numGen[difficulty - 1][1])
        answer = num1 + num2
        return answer, num1, answer - num2


class askQuestion():
    def __init__(self):
        self.num1 = None
        self.operation = "+"
        self.num2 = None
        self.totalPoints = 0
        self.num1, self.num2, self.answer = self.genQuestion("+")
        self.input = []
        self.qnum = 1

    def keyUp(self, key):
        # key >= 48 and key <= 57
        if 48 <= key <= 57 and len(self.input) < self.anslen:
            self.input.append(chr(key))
        if key == K_BACKSPACE:
            self.input.pop((len(self.input) - 1))

    def mouseUp(self, pos):
        pass

    def update(self):
        global difficulty, points, gameloop
        self.totalpoints = points[0] + points[1] + points[2] + points[3]
        button('Question: ' + str(self.qnum), GREEN, 10, 10, 50, 90, 15)
        button('Difficulty: ' + str(difficulty), GREEN, WINDOWWIDTH - 100, 10, 50, 90, 15)
        button('Points: ' + str(self.totalpoints), GREEN, WINDOWWIDTH / 2 - 45, 10, 50, 90, 15)
    
        text('What is %s %s %s?' %(self.num1, self.operation, self.num2), WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 100, 20, WHITE)
        self.anslen = len(str(self.answer))
        self.left = WINDOWWIDTH / 2 - (self.anslen-1) * 25 + 5
        for i in range(0,self.anslen):
            self.x = self.left + i * 50 - 25
            pygame.draw.line(DISPLAYSURF, RED, (self.x, WINDOWHEIGHT / 2 + 100), (self.x + 40, WINDOWHEIGHT / 2 + 100), 3)

        for c in range(0, len(self.input)):
            x = self.left + c * 50 - 25
            text(self.input[c], x + 20, WINDOWHEIGHT / 2 + 85, 20, WHITE)
        if len(self.input) == self.anslen:
            if int("".join(self.input)) == int(self.answer):
                self.totalPoints =+ 1
                r = pygame.image.load('right.png')
                r = pygame.transform.scale(r, (100, 100))
                DISPLAYSURF.blit(r, (WINDOWWIDTH - 150, WINDOWHEIGHT / 2))
                text("Correct! It is %s" % self.answer, WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 20, WHITE)
                gameloop.pause(1.5)
            else:
                n = pygame.image.load('red.png')
                n = pygame.transform.scale(n, (100, 100))
                DISPLAYSURF.blit(n, (WINDOWWIDTH - 150, WINDOWHEIGHT / 2))
                text("No it was %s not %s" % (self.answer, ''.join(self.input)), WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 20, WHITE)
                gameloop.pause(1.5)
            self.qnum += 1
            print(self.qnum)
            self.input = []
            if self.qnum <= 5:
                self.operation = "+"
            elif self.qnum <= 10:
                self.operation = "-"
            elif self.qnum <= 15:
                self.operation = "+"
            #else:
             #   gameloop.setScreen("introScreen")
            self.num1, self.num2, self.answer = self.genQuestion(self.operation)
            

    def genQuestion(self, operation):
        if operation == "+":
            return questionGen().addition()
        elif operation == "-":
            return questionGen().subtraction()
            

class leaderboard():
    def __init__(self):
        self.Back = pygame.font.Font('freesansbold.ttf', 15)
        # Backrect = pygame.draw.rect(DISPLAYSURF, RED, ((10, 10, 60, 30)))
        self.Backtext = self.Back.render('Back', True, WHITE, BLACK)
        self.Backobj = self.Backtext.get_rect()
        self.Backobj.center = 30, 20
        self.title = pygame.font.Font('freesansbold.ttf', 25)
        self.namesfont = pygame.font.Font('freesansbold.ttf', 20)
        self.textSurfaceObj = self.title.render('Leaderboard', True, WHITE, BLACK)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = WINDOWWIDTH / 2, 50

    def mouseUp(self, pos):
        if self.Backobj.collidepoint(pos):
            gameloop.setScreen("introScreen")

    def update(self):
        DISPLAYSURF.blit(self.Backtext, self.Backobj)
        DISPLAYSURF.blit(self.textSurfaceObj, self.textRectObj)
        self.readFile()
        for n in range(0,len(self.names)):
            self.tmp = self.namesfont.render('Rank ' + str(n+1) + ': ' + str(self.names[n]) + '    --> ' +  str(self.score[n]) + ' Points', True, WHITE, BLACK)
            self.tmpb = self.tmp.get_rect()
            self.tmpb.topleft = 60, 85 + 50*n
            DISPLAYSURF.blit(self.tmp, self.tmpb)

    def readFile(self):
        row = 0
        with open('settings.txt', 'r') as doc:
            lbcontent = doc.readlines()
            self.names = []
            self.score = []
            for self.row in lbcontent:
                eq = self.row.find('=')
                if self.eq > 0:
                    self.score.append(int(row[eq + 1:]))
                    self.names.append(str(row[:eq - 1]))


class configScreen():
    def __init__(self):
        self.buttons = {}
        print("init")
        self.config = ConfigHandler()
        self.lb = self.config.getParameter("Leaderboard")
        print("Var: " + str(self.lb))
        if self.lb == "on":
            self.lbcolor = GREEN
        else:
            self.lbcolor = RED
        #self.buttons["leaderboard"] = button('Leaderboard', self.lbcolor, 20, 20, 50, 200)
        #self.buttons["save"] = button('Save', YELLOW, WINDOWWIDTH / 2 - 50, WINDOWHEIGHT - 80, 60, 100)
    def update(self):
        self.buttons["leaderboard"].update()
        self.buttons["save"].update()
        text(self.config.getParameterDesc("Leaderboard"), 400, 45, 20, WHITE)
    def keyUp(self, key):
        pass
    def mouseUp(self, pos):
        if self.buttons["leaderboard"].obj.collidepoint(pos):
            if self.lbcolor == GREEN:
                self.lbcolor = RED
                self.config.setParameter("Leaderboard", "off", "Disable the Leaderboard Here")
            else:
                self.lbcolor = GREEN
                self.config.setParameter("Leaderboard", "on", "Disable the Leaderboard Here")
            self.buttons["leaderboard"].setColor(self.lbcolor)
        elif self.buttons["save"].obj.collidepoint(pos):
            self.config.write()


class ConfigHandler:
    def __init__(self):
        self.doc = None
        self.fileLines = {}      
        self.descLines = {}
        self.loadFile()

    def loadFile(self):
        print("Loading File")
        self.doc = open('config/settings.txt', 'r')
        for self.line in self.doc.readlines():
            self.eq = self.line.find('=')
            desc = self.line.find("//")
            
            varName = str(self.line[:self.eq - 1])
            varContent = str(self.line[self.eq + 1:desc - 1])
            self.descLines[varName] = str(self.line[desc + 2:])
            self.fileLines[varName] = varContent
        print("End Load")

    def getParameter(self, parameter):       
        if parameter in self.fileLines:
            desc = self.fileLines[parameter].find("//")
            return self.fileLines[parameter][:desc - 1]

    def getParameterDesc(self, parameter):
        if parameter in self.fileLines:
            return self.descLines[parameter]

    def setParameter(self, parameter, value, description):
        self.fileLines[parameter] = value + " //" + description

    def write(self):
        with open('settings.txt', 'w') as doc:
            output = ""
            for self.i in range(len(self.fileLines)):
                output += self.fileLines.keys()[self.i]
                output += " = "
                output += self.fileLines.values()[self.i]
            doc.write(output)





screens = {"leaderboard": leaderboard(),
           "introScreen": Screen.Intro(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT),
           "nameSelect": nameSelect(),
           "askQuestion": askQuestion(),
           "configScreen": configScreen()}
gameloop = GameLoop()
gameloop.start()
