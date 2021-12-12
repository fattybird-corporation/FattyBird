import pygame, pygame_gui, sys, random

pygame.init()

aken = pygame.display.set_mode([750, 1334])
manager = pygame_gui.UIManager([750, 1334])

sulgenupp = pygame_gui.elements.UIButton(pygame.Rect((705, 125), (50, 50)),
                                         'Sulge',
                                         manager)

kell = pygame.time.Clock()
töötab = True

while töötab:
    dt = kell.tick() / 1000
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            if e.user_type == pygame_gui.UI_BUTTON_PRESSED: 
                if e.ui_element == sulgenupp:
                    print("test")
                    töötab = False
            
        manager.process_events(e)
    
    aken.fill([255, 255, 255])
    manager.update(dt) 
    manager.draw_ui(aken)
    pygame.display.flip()
pygame.quit()
sys.exit()