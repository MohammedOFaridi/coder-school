import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (219, 212, 61)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Bissmillah")
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  screen.fill(GOLD)
  # Draw house body (filled rectangle)
  pygame.draw.rect(screen, RED, [100, 200, 100, 100])
  
  # Create triangle roof points
  import math
  center_x, center_y = 150, 200  # Position triangle at top of square
  size = 120  # Make roof wider than house
  height = size * math.sqrt(3) / 2
  
  triangle_points = [
    (center_x, center_y - height * 2/3),           # Top point
    (center_x - size/2, center_y + height/3),     # Bottom left
    (center_x + size/2, center_y + height/3)      # Bottom right
  ]
  
  # Draw filled triangle roof
  pygame.draw.polygon(screen, BLUE, triangle_points)
  
  # Or draw outline only (uncomment this line instead):
  # pygame.draw.polygon(screen, BLUE, triangle_points, 3)
  
  pygame.display.update()
  #   polygon(surface, color, points, width)





pygame.quit()

