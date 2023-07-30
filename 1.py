import pygame

WHITE = (255, 255, 255) #RGB
pad_width = 740
pad_height = 370

def runGame():
    global gamepad, clock
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gamepad.fill(WHITE)
        pygame.display.update()#화면을 계속 업데이트
        clock.tick(60) #프레임 제한

    pygame.quit()#게임을 끝낸다.

def initGame():
    global gamepad, clock 

    pygame.init()
    gamepad = pygame.display.set_model((pad_width, pad_height))
    pygame.display.set_caption('pyFlaying')#화면 타이틀 설정

    clock = pygame.timeClock()
    runGame()

initGame()#초기화