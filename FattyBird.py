import pygame, pygame_gui, sys, random # Impordib vajalikud moodulid

pygame.init()

aken = pygame.display.set_mode([576, 1024]) # Teeb akna ja laeb pildid
manager = pygame_gui.UIManager([576, 1024])
lind = pygame.image.load("lind1.png")
lindlangev = pygame.image.load("lind2.png")
lindtõusev = pygame.image.load("lind3.png")
taust1 = pygame.image.load("taust.png")
taust2 = pygame.image.load("taust2.png")
taust3 = pygame.image.load("taust3.png")
alumine_post = pygame.image.load("post1.png")
ülemine_post = pygame.image.load("post2.png")
power_tiib = pygame.image.load("power_up1.png")
power_kilp = pygame.image.load("power_up2.png")

taustanumber = random.randint(1,3) # Valib kolmest valikust suvalise tausta mida näidata
if taustanumber == 1:
    taust = taust1
elif taustanumber == 2:
    taust = taust2
elif taustanumber == 3:
    taust = taust3

kell = pygame.time.Clock()
töötab = True

while töötab:
    dt = kell.tick() / 1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            töötab = False
            
        manager.process_events(e)
    
    aken.fill([255, 255, 255])
    aken.blit(taust,(0,0))
    manager.update(dt) 
    manager.draw_ui(aken)
    pygame.display.flip()
pygame.quit()
sys.exit()