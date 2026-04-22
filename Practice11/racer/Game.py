#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE_E = 0
SCORE_C = 0 #Variable for coin

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
font_coin= pygame.font.SysFont("Verdana", 20) #Font for coin
background = pygame.image.load("AnimatedStreet.png")

#BG sound
pygame.mixer.music.load('BTS - Swim.mp3')
pygame.mixer.music.play(-1)

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
      def move(self):
        global SCORE_E
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE_E += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#New class for coins
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE_C
        self.rect.move_ip(0,SPEED)
        #если монетка ушла за экран удаляям ее
        if (self.rect.bottom > 600):
            self.kill()#удаляем монетку
      def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()#new coin sprite

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

#Creating Sprites for coins
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)#add coin to sprite

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# НОВО: событие для создания новых монет
SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 2000)  # create 2coins in 1second


#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.2 
        if event.type == SPAWN_COIN:  # НОВО: создаем новую монету
              new_coin = Coin()
              coins.add(new_coin)
              all_sprites.add(new_coin)     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE_E), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))


    #shows collection coins
    coinss= font_small.render(str(SCORE_C),True,BLACK)
    DISPLAYSURF.blit(coinss, (365,10))



    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    #проверяем сбор монет
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)  # True удаляет монету при сборе
    for coin in collected_coins:
        SCORE_C += 1
        # We also can app a coin-collecting sound
        # pygame.mixer.Sound('coin.wav').play()
        print(f"Coin collected! Total: {SCORE_C}")  # Для отладки
        
        # Создаем новую монету на месте собранной
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
#Show final score
          final_score = font_small.render(f"Coins collected: {SCORE_C}", True, WHITE)
          DISPLAYSURF.blit(final_score, (120, 350))

          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)