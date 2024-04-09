# создай игру "Лабиринт"!
from pygame import *
from random import random, uniform


window = display.set_mode((1200, 500))
display.set_caption('Project')

window.fill((55, 55, 100))

font.init()
font2 = font.Font(None, 46)
font3 = font.Font(None, 46)

FPS = 0
game = True
clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, image1, cord_x, cord_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image1), (55, 155))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class GameSprite2(sprite.Sprite):
    def __init__(self, image1, cord_x, cord_y, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(image1), (55, 55))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprite2):
    def update(self):

        self.rect.y += self.speed_y
        self.rect.x += self.speed_x


class Player(GameSprite):

    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        pass


class Player2(GameSprite):

    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
        pass


player2 = Player2('racket.png', 1150, 300, 3)
game = True
finish = False

ball = Ball('tenis_ball.png', 545, 245, 2, 1)

player = Player('racket.png', -10, 300, 3)

while game:
    window.fill((55, 55, 100))
    for e in event.get():
        if e.type == QUIT:
            game = False
        keys = key.get_pressed()
        if keys[K_SPACE]:
            ball = Ball('tenis_ball.png', 545, 245, 2, 1)
            player.speed = 1
            player2.speed = 1
   
    player.reset()
    player.update()
    player2.reset()
    player2.update()
    if ball.rect.y >= 445:
        ball.speed_y *= -1
    if sprite.collide_rect(ball, player2):
        x = uniform(0, 1) 
        print(x)
        ball.speed_x *= x*(-1)
    if sprite.collide_rect(ball, player):
        ball.speed_x *= (-1)
    if ball.rect.y <= 0:
        ball.speed_y *= -1
    if ball.rect.x <=-25 or ball.rect.x >= 1175:
        ball.speed_x = 0
        ball.speed_y = 0
        
        player.speed = 0
        player2.speed = 0
        
        text_lost = font2.render('Вы проиграли! Чтобы продолжить нажмите Space',1,(255,255,255))
        window.blit(text_lost, (210, 250))
    ball.update()
    ball.reset()
    display.update()
    clock.tick(FPS)
