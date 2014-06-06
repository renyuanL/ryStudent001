import pygame, sys, time, random
from pygame.locals import *

# set up pygame
pygame.init()
主點擊 = pygame.time.Clock()

# set up the window
視窗寬度 = 400
視窗高度 = 400
視窗畫面 = pygame.display.set_mode((視窗寬度, 視窗高度), 0, 32)
pygame.display.set_caption('Sprites and Sound')

# set up the colors
黑 = (0, 0, 0)

# set up the block data structure
玩家 = pygame.Rect(300, 100, 40, 40)
玩家圖 = pygame.image.load('player.png')
玩家圖變大 = pygame.transform.scale(玩家圖, (40, 40))
餵食的圖 = pygame.image.load('cherry.png')
食物們 = []
for i in range(20):
    食物們.append(pygame.Rect(random.randint(0, 視窗寬度 - 20), random.randint(0, 視窗高度 - 20), 20, 20))

食物計數器 = 0
新食物 = 40

# set up keyboard variables
往左 = False
往右 = False
往上 = False
往下 = False

移動速度 = 6

# set up music
吃食物的聲音 = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1, 0.0)
開啟聲音 = True

# run the game loop
while True:
    # check for the QUIT event
    for 事件 in pygame.event.get():
        if 事件.type == QUIT:
            pygame.quit()
            sys.exit()
        if 事件.type == KEYDOWN:
            # change the keyboard variables
            if 事件.key == K_LEFT or 事件.key == ord('a'):
                往右 = False
                往左 = True
            if 事件.key == K_RIGHT or 事件.key == ord('d'):
                往左 = False
                往右 = True
            if 事件.key == K_UP or 事件.key == ord('w'):
                往下 = False
                往上 = True
            if 事件.key == K_DOWN or 事件.key == ord('s'):
                往上 = False
                往下 = True
        if 事件.type == KEYUP:
            if 事件.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if 事件.key == K_LEFT or 事件.key == ord('a'):
                往左 = False
            if 事件.key == K_RIGHT or 事件.key == ord('d'):
                往右 = False
            if 事件.key == K_UP or 事件.key == ord('w'):
                往上 = False
            if 事件.key == K_DOWN or 事件.key == ord('s'):
                往下 = False
            if 事件.key == ord('x'):
                玩家.top = random.randint(0, 視窗高度 - 玩家.height)
                玩家.left = random.randint(0, 視窗寬度 - 玩家.width)
            if 事件.key == ord('m'):
                if 開啟聲音:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                開啟聲音 = not 開啟聲音

        if 事件.type == MOUSEBUTTONUP:
            食物們.append(pygame.Rect(事件.pos[0] - 10, 事件.pos[1] - 10, 20, 20))

    食物計數器 += 1
    if 食物計數器 >= 新食物:
        # add new 食物
        食物計數器 = 0
        食物們.append(pygame.Rect(random.randint(0, 視窗寬度 - 20), random.randint(0, 視窗高度 - 20), 20, 20))

    # draw the 黑 background onto the surface
    視窗畫面.fill(黑)

    # move the 玩家
    if 往下 and 玩家.bottom < 視窗高度:
        玩家.top += 移動速度
    if 往上 and 玩家.top > 0:
        玩家.top -= 移動速度
    if 往左 and 玩家.left > 0:
        玩家.left -= 移動速度
    if 往右 and 玩家.right < 視窗寬度:
        玩家.right += 移動速度


    # draw the block onto the surface
    視窗畫面.blit(玩家圖變大, 玩家)

    # check if the block has intersected with any 食物 squares.
    for 食物 in 食物們[:]:
        if 玩家.colliderect(食物):
            食物們.remove(食物)
            玩家 = pygame.Rect(玩家.left, 玩家.top, 玩家.width + 2, 玩家.height + 2)
            玩家圖變大 = pygame.transform.scale(玩家圖, (玩家.width, 玩家.height))
            if 開啟聲音:
                吃食物的聲音.play()

    # draw the 食物
    for 食物 in 食物們:
        視窗畫面.blit(餵食的圖, 食物)

    # draw the window onto the screen
    pygame.display.update()
    主點擊.tick(40)