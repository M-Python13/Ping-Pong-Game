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
        if keys_pressed[K_w] and self.rect.y < 650:
            self.rect.y -= self.speed

    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y < 650:
            self.rect.y -= self.speed

    def paddle_reset(self):
        self.image = transform.scale(image.load("racket.png"),(20,85))
        window.blit(self.image,(self.rect.x, self.rect.y))

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Pong Game")
background = transform.scale(image.load("galaxy.jpg"), (700,500))

ball = GameSprite("ball.png", randint(200,win_width - 300),randint(100,win_height - 200),10)

Racket1 = Player("racket.png",550,50,3)
Racket2 = Player("racket.png",100,100,3)


clock = time.Clock()
FPS = 60
clock.tick(FPS)

font.init()
font = font.SysFont('Arial', 25)

game = True
finished = False

speed_x = 1
speed_y = 1

while game:

    for e in event.get():
        if e.type == QUIT:
            keys_pressed = key.get_pressed()
            game = False
        
    if finished != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        window.blit(background, (0,0))
        Racket1.update_1()
        Racket2.update_2()

        ball.reset()
        Racket1.paddle_reset()
        Racket2.paddle_reset()
        
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
            
        if sprite.collide_rect(Racket1, ball) or sprite.collide_rect(Racket2, ball):
            speed_x *= -1
        
        lose1 = font.render("Player2 Loses!", 1, (255,0,0))
        lose2 = font.render("Player1 Loses!", 1, (255,0,0))

        if ball.rect.x < 0:
            
            finished = True
            window.blit(lose1,(200, 200))
        
        if ball.rect.x > 600:
            finished = True
            window.blit(lose2,(200, 200))

        

    display.update()
