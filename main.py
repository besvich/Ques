# -*- coding: utf8 -*- 
import pygame
import random

pygame.init()
pygame.font.init()
win = pygame.display.set_mode((1440, 810))
pygame.display.set_caption("Simple Questions")

walkRight = [pygame.image.load('wizard/Run/0.1.png'), pygame.image.load('wizard/Run/1.1.png'),
             pygame.image.load('wizard/Run/2.1.png'), pygame.image.load('wizard/Run/3.1.png'),
             pygame.image.load('wizard/Run/4.1.png'), pygame.image.load('wizard/Run/5.1.png'),
             pygame.image.load('wizard/Run/6.1.png'), pygame.image.load('wizard/Run/7.1.png'),
             pygame.image.load('wizard/Run/8.1.png'), pygame.image.load('wizard/Run/9.1.png')]

walkLeft = [pygame.image.load('wizard/Run/0.2.png'), pygame.image.load('wizard/Run/1.2.png'),
            pygame.image.load('wizard/Run/2.2.png'), pygame.image.load('wizard/Run/3.2.png'),
            pygame.image.load('wizard/Run/4.2.png'), pygame.image.load('wizard/Run/5.2.png'),
            pygame.image.load('wizard/Run/6.2.png'), pygame.image.load('wizard/Run/7.2.png'),
            pygame.image.load('wizard/Run/8.2.png'), pygame.image.load('wizard/Run/9.2.png')]
playerStandRight = [pygame.image.load('wizard/Stand/0.png'), pygame.image.load('wizard/Stand/1.png'),
                    pygame.image.load('wizard/Stand/2.png'), pygame.image.load('wizard/Stand/3.png'),
                    pygame.image.load('wizard/Stand/4.png'), pygame.image.load('wizard/Stand/5.png'),
                    pygame.image.load('wizard/Stand/6.png'), pygame.image.load('wizard/Stand/7.png'),
                    pygame.image.load('wizard/Stand/8.png'), pygame.image.load('wizard/Stand/9.png'), ]
playerStandLeft = [pygame.image.load('wizard/Stand/0.1.png'), pygame.image.load('wizard/Stand/1.1.png'),
                   pygame.image.load('wizard/Stand/2.1.png'), pygame.image.load('wizard/Stand/3.1.png'),
                   pygame.image.load('wizard/Stand/4.1.png'), pygame.image.load('wizard/Stand/5.1.png'),
                   pygame.image.load('wizard/Stand/6.1.png'), pygame.image.load('wizard/Stand/7.1.png'),
                   pygame.image.load('wizard/Stand/8.1.png'), pygame.image.load('wizard/Stand/9.1.png'), ]
playerJumpLeft = [pygame.image.load('wizard/Jump/01.png'), pygame.image.load('wizard/Jump/11.png'),
                  pygame.image.load('wizard/Jump/21.png'), pygame.image.load('wizard/Jump/31.png'),
                  pygame.image.load('wizard/Jump/41.png'), pygame.image.load('wizard/Jump/51.png'),
                  pygame.image.load('wizard/Jump/61.png'), pygame.image.load('wizard/Jump/71.png'),
                  pygame.image.load('wizard/Jump/81.png'), pygame.image.load('wizard/Jump/91.png'), ]
playerJumpRight = [pygame.image.load('wizard/Jump/0.png'), pygame.image.load('wizard/Jump/1.png'),
                   pygame.image.load('wizard/Jump/3.png'), pygame.image.load('wizard/Jump/3.png'),
                   pygame.image.load('wizard/Jump/4.png'), pygame.image.load('wizard/Jump/5.png'),
                   pygame.image.load('wizard/Jump/6.png'), pygame.image.load('wizard/Jump/7.png'),
                   pygame.image.load('wizard/Jump/8.png'), pygame.image.load('wizard/Jump/9.png'), ]
bg = pygame.image.load('bg/game_background_42.png')

endp = pygame.image.load('bg/end.png')

# ques= [[pygame.image.load('ques/0.png'), True],[pygame.image.load('ques/1.png'), False ]]
ques = [[pygame.image.load('ques/0.png'), True], [pygame.image.load('ques/1.png'), True],
        [pygame.image.load('ques/2.png'), False], [pygame.image.load('ques/3.png'), False],
        [pygame.image.load('ques/4.png'), False], [pygame.image.load('ques/5.png'), False],
        [pygame.image.load('ques/6.png'), True], [pygame.image.load('ques/7.png'), False],
        [pygame.image.load('ques/8.png'), False], [pygame.image.load('ques/9.png'), False],
        [pygame.image.load('ques/10.png'), True], [pygame.image.load('ques/11.png'), False],
        [pygame.image.load('ques/12.png'), True], [pygame.image.load('ques/13.png'), False],
        [pygame.image.load('ques/14.png'), False], [pygame.image.load('ques/15.png'), True],
        [pygame.image.load('ques/16.png'), False], [pygame.image.load('ques/17.png'), False],
        [pygame.image.load('ques/18.png'), False], [pygame.image.load('ques/19.png'), True]]  # Вопросы с ответами

from random import shuffle

shuffle(ques)

x = 465
y = 385
widht = 512
height = 512
speed = 12

end = False
clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
animStand = 0
leftStand = False
rightStand = True

ich = 0
icha = list(range(len(ques)))
ansWrong, ansCor = 0, 0
Barr = pygame.image.load('ques/Bar.png')


def drawWin():
    global animCount, animStand, animJump
    win.blit(bg, (0, 0))
    win.blit(ansyes, ansRect)
    win.blit(ansno, rect)
    win.blit(ques[icha[ich]][0], (535, 120))
    win.blit(Bar, (0, 0))
    win.blit(Barr, (0, 0))

    win.blit(Bar_font.render(str(ansCor), 3, (0, 255, 0)), (150, 0))
    win.blit(Bar_font.render(str(ansWrong), 3, (255, 0, 0)), (187, 114))
    if animCount + 1 >= 36:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 4], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 4], (x, y))
        animCount += 1
    else:
        if animStand + 1 >= 36:
            animStand = 0
        if rightStand:
            win.blit(playerStandRight[animStand // 4], (x, y))
        elif leftStand:
            win.blit(playerStandLeft[animStand // 4], (x, y))
        animStand += 1

    pygame.display.update()


def answer():
    global ansWrong, ansCor, x, ich, end
    if x < 100 and y < 385:
        if ques[icha[ich]][1]:
            ansCor += 1
            if ich + 1 < len(icha):
                ich += 1
            else:
                ich = 0
                end = True
        else:
            ansWrong += 1
        x = 465
    elif x > 840 and y < 385:
        if not (ques[icha[ich]][1]):
            ansCor += 1
            if ich + 1 < len(icha):
                ich += 1
            else:
                ich = 0
                end = True
        else:
            ansWrong += 1
        x = 465


run = True
ansno = pygame.Surface((300, 400))
ansno.set_alpha(100)
ansno.fill((255, 0, 10))
rect = pygame.Rect((1120, 390, 300, 400))

ansyes = pygame.Surface((300, 400))
ansyes.set_alpha(100)
ansyes.fill((10, 255, 10))
ansRect = pygame.Rect((20, 390, 300, 500))

Bar = pygame.Surface((260, 160))
Bar.set_alpha(220)
Bar.fill((191, 253, 246))
Bar_font = pygame.font.SysFont('Impact', 40)

end_font = pygame.font.SysFont('Comic Sans', 160)

while run:  # Главный цикл
    clock.tick(44)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > -160:
        x -= speed
        left = True
        right = False
        leftStand = True
        rightStand = False
    elif keys[pygame.K_RIGHT] and x < 1440 - widht + 160:
        x += speed
        left = False
        right = True
        leftStand = False
        rightStand = True
    else:
        left = False
        right = False
        animCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    drawWin()
    answer()
    if end:
        win.blit(endp, (0, 0))
        x = 465
        win.blit(end_font.render(str(ansWrong), 3, (255, 0, 0)), (685, 350))
        pygame.display.update()
        ansCor = 0
        ansWrong = 0
        pygame.time.delay(5555)
        end = False
        random.shuffle(icha)
pygame.quit()
