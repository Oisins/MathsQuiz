# -*- coding: cp1252 -*-
#Setup start
import pygame, sys, time, random, os
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Oisin\'s Maths Quiz')

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
FPS = 10
fpsclock = pygame.time.Clock()
#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
BLUE         = (  0,   0, 255)
YELLOW       = (255, 255,   0)
'''started = False
numneednew = True
lbedit = False
qnum = 1
ticktodo = 0
at = 'plus'
points, pointsmine, pointsplus, pointstimes = 0, 0, 0, 0
nameinput, score, names, inputs = [], [], [], []'''
currentScreen = "configScreen"
name = ""
difficulty = 1
points = [0,0,0,0]
qnum = 1
#setup end

def terminate():
    pygame.quit()
    sys.exit()
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

class button:
    def __init__(self, text, color, x, y, hight, width, FONTSIZE = 20):
        self.text, self.color, self.x, self.y, self.hight, self.width = text, color, x, y, hight, width
        self.fontObj = pygame.font.Font('freesansbold.ttf', FONTSIZE)
        self.obj = None
    def update(self):
        self.obj = pygame.draw.rect(DISPLAYSURF, self.color, (self.x, self.y, self.width, self.hight))
        self.obj.topleft = (self.x, self.y)
        self.textSurfaceObj = self.fontObj.render(str(self.text), True, BLACK, self.color)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = self.obj.center
        DISPLAYSURF.blit(self.textSurfaceObj, self.textRectObj)
    def setColor(self, color):
        self.color = color

class introScreen:
    def __init__(self):
        self.buttons = {}
        #Font Setup
        self.leaderboard = pygame.draw.rect(DISPLAYSURF, BLACK, ((WINDOWWIDTH - 120, 0, WINDOWWIDTH - 110, 140)))
        self.trophy = pygame.image.load('images/Trophy.png')
        self.trophy = pygame.transform.scale(self.trophy, (100, 100))

        self.lbfont = pygame.font.Font('freesansbold.ttf', 15)
        self.lb = self.lbfont.render('Leaderboard', True, WHITE, BLACK)
        self.lbrect = self.lb.get_rect()
        self.lbrect.center = WINDOWWIDTH - 62, 130

        self.buttons["diff1"] = button('1', GREEN, WINDOWWIDTH / 2 - 70, WINDOWHEIGHT / 2 + 50, 50, 50, 20)
        self.buttons["diff2"] = button('2', YELLOW, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 50, 50, 50, 20)
        self.buttons["diff3"] = button('3', RED, WINDOWWIDTH / 2 + 70, WINDOWHEIGHT / 2 + 50, 50, 50, 20)
    def update(self):
        DISPLAYSURF.blit(self.trophy, (WINDOWWIDTH - 110, 10))
        DISPLAYSURF.blit(self.lb, self.lbrect)
        #Into Text
        text('This is a maths quiz.', WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 25, 15, WHITE)
        text('You will get 5 questions in addition, subtraction and multiplication.', WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 15, WHITE)
        text('What difficulty do you want?', WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 25, 15, WHITE)
        #Add Difficulty buttons
        self.buttons["diff1"].update()
        self.buttons["diff2"].update()
        self.buttons["diff3"].update()

    def mouseUp(self, pos):
        global difficulty
        #Check what difficulty user wants
        if self.buttons["diff1"].obj.collidepoint(pos):
            difficulty = 1
            gameloop.setScreen("nameSelect")
        elif self.buttons["diff2"].obj.collidepoint(pos):
            difficulty = 2
            gameloop.setScreen("nameSelect")
        elif self.buttons["diff3"].obj.collidepoint(pos):
            difficulty = 3
            gameloop.setScreen("nameSelect")
        elif self.leaderboard.collidepoint(pos):
            gameloop.setScreen("leaderboard")
    def keyUp(self, key):
        #No Key Events in Intro Screen
        pass

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
        if key == K_RETURN and len(self.name) > 0: #Confirm input and go the next screen
            name = self.name
            gameloop.setScreen("askQuestion")
        elif key == K_BACKSPACE: #If Backspace delete last Letter
            self.name = self.name[:-1]
        elif key >= 97 and key <= 122: #If Letter add it to the Name String
            self.name += pygame.key.name(key)
    def mouseUp(self, pos):
        pass
        
class questionGen():
    def __init__(self):
        self.numGen = [(10,50),(30,150),(100,1000)]
    def addition(self):
        global difficulty
        self.num1 = random.randint(self.numGen[difficulty - 1][0], self.numGen[difficulty - 1][1])
        self.num2 = random.randint(self.numGen[difficulty - 1][0], self.numGen[difficulty - 1][1])
        self.answer = self.num1 + self.num2
        return self.num1, self.num2, self.answer
    def subtraction(self):
        global difficulty
        self.num1 = random.randint(self.numGen[difficulty - 1][0], self.numGen[difficulty - 1][1])
        self.num2 = random.randint(self.numGen[difficulty - 1][0], self.numGen[difficulty - 1][1])
        self.answer = self.num1 + self.num2
        return self.answer, self.num1, self.answer - self.num2
        
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
        if key >= 48 and key <= 57 and len(self.input) < self.anslen:
            self.key = key
            self.input.append(chr(self.key))
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
            self.x = self.left + c * 50 - 25
            text(self.input[c], self.x + 20, WINDOWHEIGHT / 2 + 85, 20, WHITE)
        if len(self.input) == self.anslen:
            if int("".join(self.input)) == int(self.answer):
                self.totalPoints =+ 1
                r = pygame.image.load('right.png')
                r = pygame.transform.scale(r, (100, 100))
                DISPLAYSURF.blit(r, (WINDOWWIDTH - 150, WINDOWHEIGHT / 2))
                text("Correct! It is %s" %(self.answer), WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 20, WHITE)
                gameloop.pause(1.5)
            else:
                n = pygame.image.load('red.png')
                n = pygame.transform.scale(n, (100, 100))
                DISPLAYSURF.blit(n, (WINDOWWIDTH - 150, WINDOWHEIGHT / 2))
                text("No it was %s not %s" %(self.answer, ''.join(self.input)), WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 20, WHITE)
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
        #Backrect = pygame.draw.rect(DISPLAYSURF, RED, ((10, 10, 60, 30)))
        self.Backtext = self.Back.render('Back', True, WHITE, BLACK)
        self.Backobj = self.Backtext.get_rect()
        self.Backobj.center = 30, 20
        self.title = pygame.font.Font('freesansbold.ttf', 25)
        self.namesfont = pygame.font.Font('freesansbold.ttf', 20)
        self.textSurfaceObj = self.title.render('Leaderboard', True, WHITE, BLACK)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = WINDOWWIDTH / 2, 50
    def keyUp(self, key):
        pass
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
        self.row = 0
        self.doc = open('settings.txt', 'r')
        self.lbcontent = self.doc.readlines()
        self.names = []
        self.score = []
        for self.row in self.lbcontent:
            self.eq = self.row.find('=')
            if self.eq > 0: 
                self.score.append(int(self.row[self.eq + 1:]))
                self.names.append(str(self.row[:self.eq - 1]))
        
class configScreen():
    def __init__(self):
        self.buttons = {}
        print("init")
        self.config = configHandler()
        self.lb = self.config.getParameter("Leaderboard")
        print("Var: " + str(self.lb))
        if self.lb == "on":
            self.lbcolor = GREEN
        else:
            self.lbcolor = RED
        self.buttons["leaderboard"] = button('Leaderboard', self.lbcolor, 20, 20, 50, 200)
        self.buttons["save"] = button('Save', YELLOW, WINDOWWIDTH / 2 - 50, WINDOWHEIGHT - 80, 60, 100)
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
    
class configHandler():
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
            self.desc = self.line.find("//")
            
            self.varName = str(self.line[:self.eq - 1])
            self.varContent = str(self.line[self.eq + 1:self.desc - 1])
            self.descLines[self.varName] = str(self.line[self.desc + 2:])
            self.fileLines[self.varName] = self.varContent
        print("End Load")
    def getParameter(self, parameter):       
        if parameter in self.fileLines:
            self.desc = self.fileLines[parameter].find("//")
            return self.fileLines[parameter][:self.desc - 1]
    def getParameterDesc(self, parameter):       
        if parameter in self.fileLines:
            return self.descLines[parameter]
    def setParameter(self, parameter, value, description):
        self.fileLines[parameter] = value + " //" + description
    def write(self):
        self.doc = open('settings.txt', 'w')
        self.output = ""
        self.outputLines = []
        for self.i in range(len(self.fileLines)):
            self.output += self.fileLines.keys()[self.i]
            self.output += " = "
            self.output += self.fileLines.values()[self.i]
        self.doc.write(self.output)
        self.doc.close()
        print("File Closed")
    
class gameLoop():
    def __init__(self):
        self.currentScreen = None
        self.hold = 0
    def setScreen(self, screen):
        self.currentScreen = screen
    def pause(self, time):
        self.hold = time * 10
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    terminate()
                elif event.type == KEYUP: 
                    screens[currentScreen].keyUp(event.key) # Pass on the Event to the Current Screen
                if event.type == MOUSEBUTTONUP:
                    screens[currentScreen].mouseUp(event.pos)
            if self.hold == 0:
                DISPLAYSURF.fill(BLACK)
                screens[currentScreen].update()
                fpsclock.tick(FPS) 
                pygame.display.update()
            else:
                pygame.event.get()
                self.hold = self.hold - 1
                fpsclock.tick(FPS) 
                pygame.display.update()
        
            


screens = {"leaderboard": leaderboard(),
           "introScreen": introScreen(),
           "nameSelect": nameSelect(),
           "askQuestion": askQuestion(),
           "configScreen": configScreen()}
gameloop = gameLoop()
gameloop.start()
