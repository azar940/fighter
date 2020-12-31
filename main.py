###########################modules
import pygame
import random
###########################vars
wid = 1000
heg = 700
isPlayed = True
clock = pygame.time.Clock()
#imgs
backGround = pygame.image.load(r"BG.png")

p1IdleList = [pygame.image.load(r"male\Idle (1).png"), pygame.image.load(r"male\Idle (2).png"), pygame.image.load(r"male\Idle (3).png"), pygame.image.load(r"male\Idle (4).png"), pygame.image.load(r"male\Idle (5).png"), pygame.image.load(r"male\Idle (6).png"), pygame.image.load(r"male\Idle (7).png"), pygame.image.load(r"male\Idle (8).png"), pygame.image.load(r"male\Idle (9).png"), pygame.image.load(r"male\Idle (10).png"), pygame.image.load(r"male\Idle (11).png"), pygame.image.load(r"male\Idle (12).png"), pygame.image.load(r"male\Idle (13).png"), pygame.image.load(r"male\Idle (14).png"), pygame.image.load(r"male\Idle (15).png")]
p1WalkListLift = [pygame.image.load(r"male\Walk (1).png"), pygame.image.load(r"male\Walk (2).png"), pygame.image.load(r"male\Walk (3).png"), pygame.image.load(r"male\Walk (4).png"), pygame.image.load(r"male\Walk (5).png"), pygame.image.load(r"male\Walk (6).png"), pygame.image.load(r"male\Walk (7).png"), pygame.image.load(r"male\Walk (8).png"), pygame.image.load(r"male\Walk (9).png"), pygame.image.load(r"male\Walk (10).png")]
p1AttackList = [pygame.image.load(r"male\Attack (1).png"), pygame.image.load(r"male\Attack (2).png"), pygame.image.load(r"male\Attack (3).png"), pygame.image.load(r"male\Attack (4).png"), pygame.image.load(r"male\Attack (5).png"), pygame.image.load(r"male\Attack (6).png"), pygame.image.load(r"male\Attack (7).png"), pygame.image.load(r"male\Attack (8).png")]
p1DeadList = [pygame.image.load(r"male\Dead (1).png"), pygame.image.load(r"male\Dead (2).png"), pygame.image.load(r"male\Dead (3).png"), pygame.image.load(r"male\Dead (4).png"), pygame.image.load(r"male\Dead (5).png"), pygame.image.load(r"male\Dead (6).png"), pygame.image.load(r"male\Dead (7).png"), pygame.image.load(r"male\Dead (8).png"), pygame.image.load(r"male\Dead (9).png"), pygame.image.load(r"male\Dead (10).png"), pygame.image.load(r"male\Dead (11).png"), pygame.image.load(r"male\Dead (12).png")]

p2IdleList = [pygame.image.load(r"female\Idle (1).png"), pygame.image.load(r"female\Idle (2).png"), pygame.image.load(r"female\Idle (3).png"), pygame.image.load(r"female\Idle (4).png"), pygame.image.load(r"female\Idle (5).png"), pygame.image.load(r"female\Idle (6).png"), pygame.image.load(r"female\Idle (7).png"), pygame.image.load(r"female\Idle (8).png"), pygame.image.load(r"female\Idle (9).png"), pygame.image.load(r"female\Idle (10).png"), pygame.image.load(r"female\Idle (11).png"), pygame.image.load(r"female\Idle (12).png"), pygame.image.load(r"female\Idle (13).png"), pygame.image.load(r"female\Idle (14).png"), pygame.image.load(r"female\Idle (15).png")]
p2WalkListLift = [pygame.image.load(r"female\Walk (1).png"), pygame.image.load(r"female\Walk (2).png"), pygame.image.load(r"female\Walk (3).png"), pygame.image.load(r"female\Walk (4).png"), pygame.image.load(r"female\Walk (5).png"), pygame.image.load(r"female\Walk (6).png"), pygame.image.load(r"female\Walk (7).png"), pygame.image.load(r"female\Walk (8).png"), pygame.image.load(r"female\Walk (9).png")]
p2AttackList = [pygame.image.load(r"female\Attack (1).png"), pygame.image.load(r"female\Attack (2).png"), pygame.image.load(r"female\Attack (3).png"), pygame.image.load(r"female\Attack (4).png"), pygame.image.load(r"female\Attack (5).png"), pygame.image.load(r"female\Attack (6).png"), pygame.image.load(r"female\Attack (7).png"), pygame.image.load(r"female\Attack (8).png")]
p2DeadList = [pygame.image.load(r"female\Dead (1).png"), pygame.image.load(r"female\Dead (2).png"), pygame.image.load(r"female\Dead (3).png"), pygame.image.load(r"female\Dead (4).png"), pygame.image.load(r"female\Dead (5).png"), pygame.image.load(r"female\Dead (6).png"), pygame.image.load(r"female\Dead (7).png"), pygame.image.load(r"female\Dead (8).png"), pygame.image.load(r"female\Dead (9).png"), pygame.image.load(r"female\Dead (10).png"), pygame.image.load(r"female\Dead (11).png"), pygame.image.load(r"female\Dead (12).png")]
def settingDisplay(wid, heg):
    return pygame.display.set_mode((wid, heg))
root = settingDisplay(wid, heg)
pygame.display.set_caption("figth by AZIZ")
pygame.display.set_icon(p1IdleList[0])
class Player():
    def __init__(self, posX):
        self.objectsHeg = 522
        self.objectsWid = 430
        self.posX = posX
        self.posY = 150
        self.isWalkLisft = False
        self.isWalkRight = False
        self.isIdle = True
        self.isAttack = False
        self.isDead = False
        self.HealthLevel = 100
        self.moves = 0
        self.step = 5
        self.HealthLevelwid = 300
        self.HealthLevelheg = 20
        self.HealthLevelPosX = 50
        self.HealthLevelPosY = 10
    def drawHeat(self):
        pygame.draw.rect(root, (255, 255, 255),[self.HealthLevelPosX, self.HealthLevelPosY, self.HealthLevelwid, self.HealthLevelheg])
        pygame.draw.rect(root, (0, 255, 0), [self.HealthLevelPosX, self.HealthLevelPosY, 3 * self.HealthLevel, self.HealthLevelheg])
        pygame.draw.rect(root, (255, 0, 0), [self.HealthLevelPosX, self.HealthLevelPosY, self.HealthLevelwid, self.HealthLevelheg],2)
    def drawPlayer(self):
        global isPlayed
        if self.HealthLevel > 0:
            if self.isIdle:
                for i in range(len(p1IdleList)):
                    for j in 1, 2:
                        root.blit(backGround, (0, 0))
                        root.blit(p1IdleList[i], (self.posX, self.posY))
                        # time.sleep(0.02)
                        self.drawHeat()
                        pygame.display.update()
                        i += 1
                        if i == 15:
                            i = 0
            elif self.isWalkLisft or self.isWalkRight:
                root.blit(p1WalkListLift[self.moves // 2], (self.posX, self.posY))
                self.moves += 1
                if self.moves == 20:
                    self.moves = 0
            elif self.isAttack:
                root.blit(p1AttackList[self.moves // 2], (self.posX, self.posY))
                self.moves += 1
                if self.moves == 14:
                    self.moves = 0
        else:
            for i in range(len(p1DeadList)):
                for j in 1, 2:
                    root.blit(backGround, (0, 0))
                    root.blit(p1DeadList[i], (self.posX, self.posY))
                    # time.sleep(0.02)
                    pygame.display.update()
                    i += 1
                    if i == len(p1DeadList):
                        self.isDead = True
                        break
                if self.isDead:
                    break
            root.blit(backGround, (0, 0))
            root.blit(p1DeadList[11], (self.posX, self.posY))
            isPlayed = False
        self.drawHeat()
p1 = Player(100)
def tasadom():
    if p1.isAttack:
        p1.HealthLevel -= 0.2


#update the game
def reDrawGmae():
    global P2play
    global moves
    global p1isDead
    root.blit(backGround, (0, 0))
    p1.drawPlayer()
    tasadom()
    pygame.display.update()
while isPlayed:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and p1.posX > -70:
        p1.posX -= p1.step
        p1.isWalkLisft = True
        p1.isWalkRight = False
        p1.isIdle = False
        p1.isAttack = False
    elif keys[pygame.K_RIGHT] and p1.posX < wid-p1.objectsWid+70:
        p1.posX += p1.step
        p1.isWalkRight = True
        p1.isWalkLisft = False
        p1.isAttack = False
        p1.isIdle = False
    elif keys[pygame.K_SPACE]:
        p1.isWalkLisft = False
        p1.isWalkRight = False
        p1.isIdle = False
        p1.isAttack = True
    else:
        p1.isIdle = True
        p1.isAttack = False
        p1.isWalkRight = False
        p1.isWalkLisft = False
        p1.moves = 0
    reDrawGmae()
