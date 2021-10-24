
import pygame
import menu

pygame.init()
screenWidth=1000
screenHeight=600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('PyBeat')                             #Title of the window

pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

class animation:
    def __init__(self,x,y,imglist):
        self.pos=pygame.Vector2(x,y)
        self.frames=[]
        for img in imglist:
            self.frames.append(pygame.image.load(img))
        self.counter=0
        self.frame_num=len(imglist)
    def next(self):
        self.counter=(self.counter+1)%self.frame_num
    def clear(self):
        for i in range(self.frame_num):
            self.frames[i]=None

class background(animation):
    def __init__(self,imglist):
        self.frames=[]
        for img in imglist:
            self.frames.append(pygame.image.load(img))
        self.counter=0
        self.frame_num=len(imglist)

class logo(pygame.sprite.Sprite):
	def __init__(self, imagepath):
		self.image=pygame.image.load(imagepath)
		self.rect = self.image.get_rect()


def drawStartScreen():
	screen.blit(bg.frames[bg.counter], (0,0))
	screen.blit(gamelogo.image, (170,100))
	screen.blit(continue_text.frames[continue_text.counter],continue_text.pos)
	pygame.display.update()

gamelogo=logo('PyBeat_logo.png')
bg=background([f'background0/bg{i}.png' for i in range(52)])
continue_text=animation(500,500, [f'continue_text/text{i}.png' for i in range(20)])

def startScreen():
	startscreen_run=True
	delay=0
	while startscreen_run:
		delay=(delay+1)%3
		if delay==0:
			bg.next()
			continue_text.next()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				startscreen_run=False
		drawStartScreen()
	bg.clear()
	menu.startmenu()

if __name__=='__main__':
	startScreen()
