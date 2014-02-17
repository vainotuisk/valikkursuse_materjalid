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

pilt = pygame.image.load("pingviin.png")
# aken.blit(pilt, (40, 60))
xy = pilt.get_rect().size
print (xy[0],xy[1])


pygame.display.flip()

while True:
   for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()
