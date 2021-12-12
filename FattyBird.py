import pygame, pygame_gui, sys, random

pygame.init()

aken = pygame.display.set_mode([576, 1024])
manager = pygame_gui.UIManager([576, 1024])

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