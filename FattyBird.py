import pygame, pygame_gui, sys, random # Impordib vajalikud moodulid

pygame.init()

aken = pygame.display.set_mode([576, 1024]) # Teeb akna ja laeb pildid
manager = pygame_gui.UIManager([576, 1024])
lind = pygame.image.load("pildid/lind/lind1.png")
lindlangev = pygame.image.load("pildid/lind/lind2.png")
lindtõusev = pygame.image.load("pildid/lind/lind3.png")
taust1 = pygame.image.load("pildid/taust/taust.png")
taust2 = pygame.image.load("pildid/taust/taust2.png")
taust3 = pygame.image.load("pildid/taust/taust3.png")
alumine_post = pygame.image.load("pildid/post1.png")
power_tiib = pygame.image.load("pildid/power_up1.png")
power_kilp = pygame.image.load("pildid/power_up2.png")
põrand = pygame.image.load("pildid/põrand.png")
põranda_x = 0

taustanumber = random.randint(1,3) # Valib kolmest valikust suvalise tausta mida näidata
if taustanumber == 1:
    taust = taust1
elif taustanumber == 2:
    taust = taust2
elif taustanumber == 3:
    taust = taust3
    
def uus_põrand(): # Funktsioon põranda liigutamiseks
    aken.blit(põrand,(põranda_x,900))
    aken.blit(põrand,(põranda_x + 576,900))
    
def ehita_post(): # Funktsioon mis teeb joonistamiseks valmis uued postid
    juhuslik_kõrgus = random.choice(posti_kõrgus)
    all_post = alumine_post.get_rect(midtop = (700,juhuslik_kõrgus))
    üleval_post = alumine_post.get_rect(midbottom = (700,juhuslik_kõrgus - 300))
    return all_post, üleval_post

def liiguta_poste(postid): # Funktsioon mis liigutab poste
    for post in postid:
        post.centerx -= 5
    return postid

def joonista_postid(postid): # Funktsioon mis joonistab postid
    for post in postid:
        if post.bottom >= 800:
            aken.blit(alumine_post, post)
        else: # Keerab ülemise posti õiget pidi
            tagurpidi_post = pygame.transform.flip(alumine_post,False,True)
            aken.blit(tagurpidi_post,post)

posti_list = [] # List postide suurustega
UUSPOST = pygame.USEREVENT 
pygame.time.set_timer(UUSPOST,1200) # Kui mitme ms pärast tekib uus post
posti_kõrgus = [500,600,700] # Valik posti kõrgustest

kell = pygame.time.Clock()
töötab = True 

while töötab: # Mängu tsükkel
    dt = kell.tick(120) # FPS
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            töötab = False
        if e.type == UUSPOST:
            posti_list.extend(ehita_post())
            
        manager.process_events(e)
    
    aken.fill([255, 255, 255])
    aken.blit(taust,(0,0))
    
    # Postid
    posti_list = liiguta_poste(posti_list)
    joonista_postid(posti_list)
    
    # Põrand
    põranda_x -= 1
    uus_põrand()
    if põranda_x <= -576:
        põranda_x = 0
        
    manager.update(dt) 
    manager.draw_ui(aken)
    pygame.display.flip()
pygame.quit()
sys.exit()