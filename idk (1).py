import pygame
import random

# Colors
# Main colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
# Grays
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
DARK_GRAY = (64, 64, 64)

# Reds
DARK_RED = (128, 0, 0)
LIGHT_RED = (255, 128, 128)
PINK = (255, 192, 203)

# Greens
DARK_GREEN = (0, 128, 0)
LIGHT_GREEN = (128, 255, 128)
LIME = (0, 255, 0)

# Blues
DARK_BLUE = (0, 0, 128)
LIGHT_BLUE = (173, 216, 230)
NAVY = (0, 0, 128)

# Yellows/Oranges
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
DARK_YELLOW = (128, 128, 0)

# Purples
PURPLE = (128, 0, 128)
VIOLET = (238, 130, 238)
INDIGO = (75, 0, 130)

# Browns
BROWN = (165, 42, 42)
TAN = (210, 180, 140)
BEIGE = (245, 245, 220)

# All colors in a list
color = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, LIGHT_GRAY, DARK_GRAY, DARK_RED, LIGHT_RED, PINK, DARK_GREEN, LIGHT_GREEN, LIME, DARK_BLUE, LIGHT_BLUE, NAVY, ORANGE, GOLD, DARK_YELLOW, PURPLE, VIOLET, INDIGO, BROWN, TAN]

x = 500
y = 500

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("THIS WILL GIVW U A SEACURE")
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Randomly select a color from the list
    selected_color = random.choice(color)

    # Fill the screen with the randomly selected color
    screen.fill(selected_color)

    # Draw a blue circle
   # pygame.draw.circle(screen, BLUE, (x, y), 50)

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
