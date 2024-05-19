from pygame import *
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс описывающий ракетки
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5 :
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        global loste
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80,win_width - 80)
            self.rect.y = 0
            loste = loste + 1
#игровая сцена
back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
#cоздание спрайтов
racket1 = Player('racketka1.png',30,200,4,50,150)
racket2 = Player('racketka1.png',520,200,4,50,150)
ball = GameSprite('ball1.png',200,200,4,50,50)
xx = 2
yy = 2
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not  finish :
        ball.rect.x += xx 
        ball.rect.y += yy
        racket1.update_r()
        racket2.update_l()
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            xx *= -1
            yy *= 1
        if ball.rect.y > win_height -50 or ball.rect.y <0 :
            yy += -1
        if ball.rect.x < 0:
            finish = True
            game_over = True
    ball.reset()      
    racket1.reset()
    racket2.reset()
    display.update()
    time.delay(30)
