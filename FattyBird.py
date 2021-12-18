import pygame, sys, random # Impordib vajalikud moodulid

pygame.init()

aken = pygame.display.set_mode([576, 1024]) # Teeb akna

lindkesk = pygame.image.load("pildid/lind/lind1.png") # Laeb linnu pildid
lindlangev = pygame.image.load("pildid/lind/lind2.png")
lindtõusev = pygame.image.load("pildid/lind/lind3.png")

lindkesk = pygame.transform.scale(lindkesk, (101, 33)) # Teeb linnu pildid õigeks suuruseks
lindlangev = pygame.transform.scale(lindlangev, (101, 33.5))
lindtõusev = pygame.transform.scale(lindtõusev, (101, 44))

lind_kaader = [lindlangev, lindkesk, lindtõusev]
lind_kord = 0
lind = lind_kaader[lind_kord]
linnu_ruut = lind.get_rect(center = (100, 512))

LINDLEHVITA = pygame.USEREVENT + 1
pygame.time.set_timer(LINDLEHVITA, 200)

taust1 = pygame.image.load("pildid/taust/taust.png") # Laeb tausta pildid
taust2 = pygame.image.load("pildid/taust/taust2.png")
taust3 = pygame.image.load("pildid/taust/taust3.png")

alumine_post = pygame.image.load("pildid/post1.png") # Laeb posti pildi

power_tiib = pygame.image.load("pildid/power_up1.png") # Laeb powerup pildid
power_kilp = pygame.image.load("pildid/power_up2.png")

põrand = pygame.image.load("pildid/põrand.png") # Laeb põranda pildi
põranda_x = 0
mängu_font = pygame.font.Font("font/04B_19.ttf",40) # Määrab mängu kirjastiili

# Mängu muutujad
kell = pygame.time.Clock()
töötab = True
elus = True
skoor = 0
kõrgeim_skoor = 0
gravitatsioon = 0.5
linnu_liikumine = 0

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

def kuva_skoor(mängu_olek):
    if mängu_olek == "elus":
        skoor_pind = mängu_font.render(str(int(skoor)),True,(255,255,255))
        skoor_rect = skoor_pind.get_rect(center = (288,100))
        aken.blit(skoor_pind,skoor_rect)
    if mängu_olek == "läbi":
        skoor_pind = mängu_font.render(f"Skoor: {int(skoor)}",True,(255,255,255))
        skoor_rect = skoor_pind.get_rect(center = (288,100))
        aken.blit(skoor_pind,skoor_rect)
        
        kõrgeim_skoor_pind = mängu_font.render(f"Kõrgeim skoor: {int(kõrgeim_skoor)}",True,(255,255,255))
        kõrgeim_skoor_rect = kõrgeim_skoor_pind.get_rect(center = (288,850))
        aken.blit(kõrgeim_skoor_pind,skoor_rect)

def uuenda_skoori(skoor, kõrgeim_skoor):
    if skoor > kõrgeim_skoor:
        kõrgeim_skoor = skoor
    return kõrgeim_skoor
        
def vaata_puudet(postid): # Vaatab kas lind puutub kokku postidega
    global töötab
    
    for post in postid:
        if linnu_ruut.colliderect(post):
            return False
            
    if linnu_ruut.top <= -100 or linnu_ruut.bottom >= 900:
        return False
    
    return True
                
def pööre_lind(lind): # Linnu pööramine
    uus_lind = pygame.transform.rotozoom(lind, -linnu_liikumine * 1.2, 1)
    return uus_lind

def linnu_animatsioon(): # Linnu animatsioon
    uus_lind = lind_kaader[lind_kord]
    uus_lind_ruut = uus_lind.get_rect(center = (100, linnu_ruut.centery))
    return uus_lind, uus_lind_ruut

posti_list = [] # List postide suurustega
UUSPOST = pygame.USEREVENT 
pygame.time.set_timer(UUSPOST,1200) # Kui mitme ms pärast tekib uus post
posti_kõrgus = [500,600,700] # Valik posti kõrgustest

while töötab: # Mängu tsükkel
    dt = kell.tick(120) # FPS
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            töötab = False
        if e.type == UUSPOST:
            posti_list.extend(ehita_post())
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and elus: # Kui vajutatakse tühikut
                linnu_liikumine = 0
                linnu_liikumine -= 12
            if e.key == pygame.K_SPACE and elus == False:
                elus = True
                posti_list.clear()
                linnu_ruut.center = (100, 512)
                
        if e.type == LINDLEHVITA:
            if lind_kord < 2:
                lind_kord += 1
            else:
                lind_kord = 0
                
            lind, linnu_ruut = linnu_animatsioon()
    
    aken.fill([255, 255, 255])
    aken.blit(taust,(0,0))
    
    if elus:
        # Lind
        linnu_liikumine += gravitatsioon
        pööratud_lind = pööre_lind(lind)
        linnu_ruut[1] += linnu_liikumine
        elus = vaata_puudet(posti_list)
        aken.blit(pööratud_lind, linnu_ruut)
        
        # Postid
        posti_list = liiguta_poste(posti_list)
        joonista_postid(posti_list)
    
        skoor += 0.01
        kuva_skoor("elus")
    else:
        kõrgeim_skoor = uuenda_skoori(skoor,kõrgeim_skoor)
        kuva_skoor("läbi")

    
    # Põrand
    põranda_x -= 1
    uus_põrand()
    if põranda_x <= -576:
        põranda_x = 0
        
    pygame.display.flip()
pygame.quit()
sys.exit()