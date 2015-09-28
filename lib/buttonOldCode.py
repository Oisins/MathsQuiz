__author__ = 'Oisin Smith'

class baseButton:
    #, text=text, color=color, x=x, y=y, hight=hight, width=width, FONTSIZE = 20
    def __init__(self, **kwargs):
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


class toggleButton(baseButton):

    def __init__(self, **kwargs):
        super(toggleButton, self).__init__(kwargs)
        self.state = False
        self.color = kwargs["colors"][0]


    def onClick(self):
        if self.state:
            self.color = self.colors[1]
        else:
            self.color = self.colors[0]
        self.state != self.state
