import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('RingForge')
clock = pygame.time.Clock()
gesture = 'None'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                gesture = 'Menu Activated'
            elif event.button == 3:
                gesture = 'Scroll Up'
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render(f'Gesture: {gesture} - AR Screen Updated!', True, (255, 255, 255))
    screen.blit(text, (50, 50))
    pygame.display.flip()
    clock.tick(60)