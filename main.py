from pygame import *
init()


W = 700
H = 700


window = display.set_mode((W, H))
display.set_caption("Labyrinth")
display.set_icon(image.load('treasure.png'))

back = transform.scale(image.load('background.jpg'), (W, H))
clock = time.Clock()

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.set_volume(0.5)
mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H - 65:
            self.rect.y += self.speed
        
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < W - 65:
            self.rect.x += self.speed
        

class Enemy(GameSprite):
    direction = "right"

    def update(self, start, end):
        if self.rect.x >= end:
            self.direction = "left"
            self.image = transform.scale(image.load('grib_left.png'), (65, 65))
        if self.rect.x <= start:
            self.direction = "right"
            self.image = transform.scale(image.load('grib_right.png'), (65, 65))

        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_w, wall_h, wall_x, wall_y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



hero = Player("dino_test.png", 40, 150, 3.5)
enemy1 = Enemy('grib_right.png', 300, 300, 3)
enemy2 = Enemy('grib_right.png', 40, 20, 4)
enemy3 = Enemy('grib_right.png', 350, 450, 6.5)
gold = GameSprite('coin.png', 550, 600, 0)
game = True

wall1 = Wall(126, 200, 10, 150, 20, 0, 90)
wall2 = Wall(126, 200, 10, 150, 20, 0, 250)
wall3 = Wall(126, 200, 10, 150, 20, 150, 400)
wall4 = Wall(126, 200, 10, 20, 150, 300, 400)
wall5 = Wall(126, 200, 10, 150, 20, 0, 545)
wall6 = Wall(126, 200, 10, 20, 175, 300, 90)
wall7 = Wall(126, 200, 10, 150, 20, 300, 550)
wall8 = Wall(126, 200, 10, 20, 150, 450, 550)
wall9 = Wall(126, 200, 10, 275, 20, 300, 90)
wall10 = Wall(126, 200, 10, 280, 20, 420, 245)
wall11 = Wall(126, 200, 10, 300, 20, 300, 400)
wall12 = Wall(126, 200, 10, 150, 20, 450, 550)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(back, (0, 0))
    gold.reset()

    hero.reset()
    hero.update()

    enemy1.reset()
    enemy1.update(200, 350)
    enemy2.reset()
    enemy2.update(40, 640)
    enemy3.reset()
    enemy3.update(350, 625)
    
    
    wall1.reset()
    wall2.reset()
    wall3.reset()
    wall4.reset()
    wall5.reset()
    wall6.reset()
    wall7.reset()
    wall8.reset()
    wall9.reset()
    wall10.reset()
    wall11.reset()
    wall12.reset()

    if sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2)  or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7) or sprite.collide_rect(hero, wall8) or sprite.collide_rect(hero, wall9) or sprite.collide_rect(hero, wall10) or sprite.collide_rect(hero, wall11) or sprite.collide_rect(hero, wall12):
        hero.rect.x = 40
        hero.rect.y = 150

    if sprite.collide_rect(hero, gold):
        game = False

    if sprite.collide_rect(hero, enemy1) or sprite.collide_rect(hero, enemy2) or sprite.collide_rect(hero, enemy3):
        hero.rect.x = 40
        hero.rect.y = 150
    
    if hero.rect.x == 40 and hero.rect.y == 600:
        game = False

    display.update()
    clock.tick(60)