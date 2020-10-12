import sys
import pygame

def run_test():

    pygame.init()
    screen=pygame.display.set_mode((1024,500))
    pygame.display.set_caption('show event type')

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                print(event.key)

        screen.fill((0,0,230))
        pygame.display.flip()
run_test()