import pygame, sys
from pygame.locals import QUIT

GLOBALS = {
    "DISPLAYSURF": None,
    "E_Resolution": (),
}

def start():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((320, 240))
    GLOBALS["DISPLAYSURF"]  = DISPLAYSURF
    GLOBALS["E_Resolution"] = (320, 240)
    pygame.display.set_caption('E Computer V1')
def frame():
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()
