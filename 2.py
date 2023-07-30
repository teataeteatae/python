import pygame

WHITE = (255, 255, 255)
pad_width = 740
pad_height = 370

def runGame():
    global gamepad, clock 

    x = pad_width * 0.005
    y = pad_height * 0.8
    y_change = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.K_up:
                y_change = -5
                