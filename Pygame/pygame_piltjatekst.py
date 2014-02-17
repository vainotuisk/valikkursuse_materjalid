##
## Pygame: pilt & tekst
## Väino Tuisk
##

import pygame,sys
pygame.init()

aken = pygame.display.set_mode([800,600])

valge = [255,255,255]
punane = [255,0,0]

aken.fill(valge)



pygame.display.flip()

while True:
   for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()
