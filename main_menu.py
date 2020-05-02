#sets up pygame
import pygame, sys

#pygame/window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Video Game')
screen = pygame.display.set_mode ((500,500),0,32)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

#click variable
click = False



#main menu loop
def main_menu():
    while True:
        
        screen.fill((0,0,0)) #change later to background picture
        draw_text('Main Menu', font, (255,255,255), screen, 20, 20)


        mx, my = pygame.mouse.get.get_pos()
        
        #butons
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
            
        #mouse collides with button
        if button_1.collidepoint ((mx,my)):
            if click:
                 game()
            if button_2.collidepoint ((mx,my)):
                if click:
                 options()
            #renders buttons
            pygame.draw.rect(screen, (0, 0, 255), button_1)
            pygame.draw.rect(screen, (255, 0, 0), button_2)

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                #mouse click left
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True


    pygame.display.update()
    mainClock.tick(60)

#Main game loop

    def game():
        running = True
        while running:
            screen.fill((0,0,0))
            draw_text('Main Game', font, (0,0,255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        runnning = False

        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('Options', font, (0,0,255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    runnning = False