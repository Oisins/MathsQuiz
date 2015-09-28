import pygame
from button.Push import Push as button
from definitions.colors import *
from screen.BaseScreen import BaseScreen


class Intro(BaseScreen):
    def __init__(self, DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT):
        self.DISPLAYSURF = DISPLAYSURF
        self.WINDOWWIDTH = WINDOWWIDTH
        self.buttons = {}
        # Font Setup
        self.leaderboard = pygame.draw.rect(DISPLAYSURF, BLACK, ((WINDOWWIDTH - 120, 0, WINDOWWIDTH - 110, 140)))
        self.trophy = pygame.image.load('images/Trophy.png')
        self.trophy = pygame.transform.scale(self.trophy, (100, 100))

        self.lbfont = pygame.font.Font('freesansbold.ttf', 15)
        self.lb = self.lbfont.render('Leaderboard', True, WHITE, BLACK)
        self.lbrect = self.lb.get_rect()
        self.lbrect.center = WINDOWWIDTH - 62, 130

        self.buttons["diff1"] = button(text='1', color=GREEN, x=WINDOWWIDTH / 2 - 70, y=WINDOWHEIGHT / 2 + 50, width=50, height=50, fontsize=20, surf=DISPLAYSURF)
        self.buttons["diff2"] = button(text='2', color=YELLOW, x=WINDOWWIDTH / 2, y=WINDOWHEIGHT / 2 + 50, width=50, height=50, fontsize=20, surf=DISPLAYSURF)
        self.buttons["diff3"] = button(text='3', color=RED, x=WINDOWWIDTH / 2 + 70, y=WINDOWHEIGHT / 2 + 50, width=50, height=50, fontsize=20, surf=DISPLAYSURF)

    def update(self):
        self.DISPLAYSURF.blit(self.trophy, (self.WINDOWWIDTH - 110, 10))
        self.DISPLAYSURF.blit(self.lb, self.lbrect)
        # Into Text
        #text('This is a maths quiz.', WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 25, 15, WHITE)
        #text('You will get 5 questions in addition, subtraction and multiplication.', WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 15, WHITE)
        #text('What difficulty do you want?', WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 25, 15, WHITE)
        # Add Difficulty buttons
        self.buttons["diff1"].update()
        self.buttons["diff2"].update()
        self.buttons["diff3"].update()

    def mouseUp(self, pos):
        global difficulty
        # Check what difficulty user wants
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