from pygame import *

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
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_S] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_W] and self.rect.y < 595:
            self.rect.x += self.speed

    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_UP] and self.rect.x < 595:
            self.rect.x += self.speed
    

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter Game")
background = transform.scale(image.load("galaxy.jpg"), (700,500))


clock = time.Clock()
FPS = 60
clock.tick(FPS)


game = True

while game:

    for e in event.get():
        keys_pressed = key.get_pressed()
        if e.type == QUIT:
            game = False
        
        window.blit(background, (0,0))

        display.update()
