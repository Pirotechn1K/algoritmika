#создай игру "Лабиринт"!
from pygame import *

window = display.set_mode((1200, 500))
display.set_caption('Project')

window.fill((55, 55, 100))

font.init()
font2 = font.Font(None, 36)
font3 = font.Font(None, 36)

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
    def __init__(self, image1, cord_x, cord_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image1), (55, 55))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprite2):
    def update(self):
        if self.rect.y < 445:
            self.rect.y += self.speed
            self.rect.x += self.speed
        

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
player2 = Player2('racket.png', 1150, 300, 1)
game = True
finish = False

ball = Ball('tenis_ball.png', 545, 245, 3)

player = Player('racket.png', -10, 300, 1)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((55, 55, 100))
    player.reset()
    player.update()
    player2.reset()
    player2.update()
    ball.update()
    ball.reset()
    display.update()
    clock.tick(FPS)