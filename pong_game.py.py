from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self,image_player,x_player, y_player,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(65,65))
        self.speed = player_speed
        self.rect  = self.image.get_rect()
        self.rect.x= x_player 
        self.rect.y= y_player

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y < 595:
            self.rect.y -= self.speed

    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y < 595:
            self.rect.y -= self.speed

class Ball(GameSprite):
    pass

    

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Pong Game")
background = transform.scale(image.load("galaxy.jpg"), (700,500))

ball = GameSprite("ball.png", randint(200,win_width - 300),randint(100,win_height - 200),10)

Racket1 = Player("racket.png",550,100,30 )
Racket2 = Player("racket.png",100,100,30 )


clock = time.Clock()
FPS = 60
clock.tick(FPS)


game = True
finished = False


while game:

    for e in event.get():
        keys_pressed = key.get_pressed()
        if e.type == QUIT:
            game = False
        
        if finished != True:
            window.blit(background, (0,0))
            Racket1.update_1()
            Racket2.update_2()

    
            ball.reset()
            Racket1.reset()
            Racket2.reset()
        

    display.update()