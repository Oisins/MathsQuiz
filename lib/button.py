import pygame


class BaseButton:
    def __init__(self, **kwargs):
        self.fontObj = pygame.font.Font('freesansbold.ttf', kwargs["fontsize"])
        self.obj = None
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.width = kwargs['width']
        self.height = kwargs['height']

    def update(self):
        self.obj = pygame.draw.rect(DISPLAYSURF, self.color, (self.x, self.y, self.width, self.hight))
        self.obj.topleft = (self.x, self.y)
        self.textSurfaceObj = self.fontObj.render(str(self.text), True, BLACK, self.color)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = self.obj.center
        DISPLAYSURF.blit(self.textSurfaceObj, self.textRectObj)

    def onClick(self):
        pass

class ToggleButton(BaseButton):

    def __init__(self, **kwargs):
        super(ToggleButton, self).__init__(kwargs)
        self.state = False
        self.color = kwargs["colors"][0]


    def onClick(self):
        if self.state:
            self.color = self.colors[1]
        else:
            self.color = self.colors[0]
        self.state != self.state