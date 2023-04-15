import os
#подключение модулей(pygame, random)
from pygame import *
from random import *

#Классы GameSprite и Player
     #класс gamesprite
class GameSprite(sprite.Sprite):
    def __init__(self, coord_x, coord_y, player_speed, widht, height, player_image):
        sprite.Sprite. __init__(self)
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
#перемещение ракеток вверх
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed


#перемещение ракеток вверх
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed


#перемещение ракеток вниз
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_s]:
            self.rect.y += self.speed


#перемещение ракеток вниз
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_s]:
            self.rect.y += self.speed


#перемещение ракеток вниз
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_DOWN]:
            self.rect.y += self.speed                      

#Описание игровой сцены, флаги состояний игры, надписи
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
print(os.path.isfile('galaxy.jpg'))
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
clock = time.Clock()
window.blit(background, (0,0))
game = True

#Создание игровых спрайтов

#Пока игра продолжается
while game:
    #Если нажата кнопка «Завершить игру»
    for ev in event.get():
        if ev.type == QUIT:
            #Закрыть приложение
             game = False
#Переместить ракетки

#Обновить спрайты и сцену
    display.update()
    clock.tick(40)