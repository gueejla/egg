import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
window = pygame.Window('egg', size=(WINDOW_WIDTH, WINDOW_HEIGHT))
display_surface = window.get_surface()
running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    # I see a window and I want to paint it red
    display_surface.fill('red')

    window.flip()

pygame.quit()
