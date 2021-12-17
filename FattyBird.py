import pygame, pygame_gui, sys, random

pygame.init()

aken = pygame.display.set_mode([576, 1024])
manager = pygame_gui.UIManager([576, 1024])
lind = pygame.image.load("lind1.png")
lindlangev = pygame.image.load("lind2.png")
lindtõusev = pygame.image.load("lind3.png")
taust1 = pygame.image.load("taust.png")
taust2 = pygame.image.load("taust2.png")
taust3 = pygame.image.load("taust3.png")

kell = pygame.time.Clock()
töötab = True

while töötab:
    dt = kell.tick() / 1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            töötab = False
            
        manager.process_events(e)
    
    aken.fill([255, 255, 255])
    manager.update(dt) 
    manager.draw_ui(aken)
    pygame.display.flip()
pygame.quit()
sys.exit()