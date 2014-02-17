'''
Pygame: algväärtustamine, akna loomine
Väino Tuisk
'''
import pygame,sys
pygame.init()

aken = pygame.display.set_mode([800,600])

valge = [255,255,255]
punane = [255,0,0]

aken.fill(valge)

pygame.draw.rect(aken,punane,[50,100,150,80],0)

pygame.draw.line(aken,[0,255,0],[400,300],[600,500],8)

pygame.draw.circle(aken,[0,0,255],[500,200],50,3)

pygame.display.flip()

while True:
   for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()
