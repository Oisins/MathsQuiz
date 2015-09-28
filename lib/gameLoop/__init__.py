import sys
import pygame


def terminate():
    pygame.quit()
    sys.exit()


class GameLoop:
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
                    screens[currentScreen].keyUp(event.key)  # Pass on the Event to the Current Screen
                if event.type == MOUSEBUTTONUP:
                    screens[currentScreen].mouseUp(event.pos)
            if self.hold == 0:
                DISPLAYSURF.fill(BLACK)
                screens[currentScreen].update()
                fpsclock.tick(FPS)
                pygame.display.update()
            else:
                pygame.event.get()
                self.hold -= 1
                fpsclock.tick(FPS)
                pygame.display.update()