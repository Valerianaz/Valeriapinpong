from pygame import *
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed,wight,height):
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
while game: