import pygame
import os
import random

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('egg')
running = True

# import egg
player_path = os.path.join('images', 'egg.png')
player_surf = pygame.image.load(player_path).convert_alpha()

# import grass
grass_path = os.path.join('images', 'grass.png')
grass_surf = pygame.image.load(grass_path).convert_alpha()

# import star
star_path = os.path.join('images', 'star.png')
star_surf = pygame.image.load(star_path).convert_alpha()
star_surf = pygame.transform.scale(star_surf, (20, 20))

# draw background
display_surface.fill('midnight blue')
display_surface.blit(grass_surf, (200, 200))

for i in range(0, 20):
    x_pos = random.randint(200, 1100)
    y_pos = random.randint(0, 150)

    display_surface.blit(star_surf, (x_pos, y_pos))

while running:
  # event loop
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

  # draw the player
  display_surface.blit(player_surf, (650, 175))

  pygame.display.update()

pygame.quit()
