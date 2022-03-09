import pygame
from pygame import draw
import Colors

pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode([screen_width, screen_height])

x = screen_width/2
y = screen_height/2

player_color = Colors.RED
player_width = 10
player_height = 10
player = (player_width, player_height)



run = True
# pętla główna
while run:
    # obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw.rect(screen, player_color, (x, y, player))
    pygame.display.update()

