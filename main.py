import pygame

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

background_color = (255, 255, 255)

running = True

while running:
    screen.fill(background_color)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
