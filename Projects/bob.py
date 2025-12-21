import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

DARK_RED = (139, 0, 0)
DARK_GREEN = (0, 100, 0)
DARK_BLUE = (0, 0, 139)
DARK_YELLOW = (184, 134, 11)
DARK_CYAN = (0, 139, 139)
DARK_MAGENTA = (139, 0, 139)
DARK_GRAY = (64, 64, 64)
DARK_GREY = (64, 64, 64)

LIGHT_RED = (255, 182, 193)
LIGHT_GREEN = (144, 238, 144)
LIGHT_BLUE = (173, 216, 230)
LIGHT_YELLOW = (255, 255, 224)
LIGHT_CYAN = (224, 255, 255)
LIGHT_PINK = (255, 182, 193)
LIGHT_GRAY = (211, 211, 211)
LIGHT_GREY = (211, 211, 211)

ALICEBLUE = (240, 248, 255)
ANTIQUEWHITE = (250, 235, 215)
AQUA = (0, 255, 255)
AQUAMARINE = (127, 255, 212)
AZURE = (240, 255, 255)
BEIGE = (245, 245, 220)
BISQUE = (255, 228, 196)
BLANCHEDALMOND = (255, 235, 205)
BLUEVIOLET = (138, 43, 226)
BROWN = (165, 42, 42)
BURLYWOOD = (222, 184, 135)
CADETBLUE = (95, 158, 160)
CHARTREUSE = (127, 255, 0)
CHOCOLATE = (210, 105, 30)
CORAL = (255, 127, 80)
CORNFLOWERBLUE = (100, 149, 237)
CORNSILK = (255, 248, 220)
CRIMSON = (220, 20, 60)
DARKBLUE = (0, 0, 139)
DARKCYAN = (0, 139, 139)
DARKGOLDENROD = (184, 134, 11)
DARKGREEN = (0, 100, 0)
DARKKHAKI = (189, 183, 107)
DARKMAGENTA = (139, 0, 139)
DARKOLIVEGREEN = (85, 107, 47)
DARKORANGE = (255, 140, 0)
DARKORCHID = (153, 50, 204)
DARKRED = (139, 0, 0)
DARKSALMON = (233, 150, 122)
DARKSEAGREEN = (143, 188, 143)
DARKSLATEBLUE = (72, 61, 139)
DARKSLATEGRAY = (47, 79, 79)
DARKTURQUOISE = (0, 206, 209)
DARKVIOLET = (148, 0, 211)
DEEPPINK = (255, 20, 147)
DEEPSKYBLUE = (0, 191, 255)
DIMGRAY = (105, 105, 105)
DODGERBLUE = (30, 144, 255)
FIREBRICK = (178, 34, 34)
FLORALWHITE = (255, 250, 240)
FORESTGREEN = (34, 139, 34)
FUCHSIA = (255, 0, 255)
GAINSBORO = (220, 220, 220)
GHOSTWHITE = (248, 248, 255)
GOLD = (255, 215, 0)
GOLDENROD = (218, 165, 32)
GRAY = (128, 128, 128)
GREY = (128, 128, 128)
GREENYELLOW = (173, 255, 47)
HONEYDEW = (240, 255, 240)
HOTPINK = (255, 105, 180)
INDIANRED = (205, 92, 92)
INDIGO = (75, 0, 130)
IVORY = (255, 255, 240)
KHAKI = (240, 230, 140)
LAVENDER = (230, 230, 250)
LAVENDERBLUSH = (255, 240, 245)
LAWNGREEN = (124, 252, 0)
LEMONCHIFFON = (255, 250, 205)
LIGHTBLUE = (173, 216, 230)
LIGHTCORAL = (240, 128, 128)
LIGHTCYAN = (224, 255, 255)
LIGHTGOLDENRODYELLOW = (250, 250, 210)
LIGHTGREEN = (144, 238, 144)
LIGHTPINK = (255, 182, 193)
LIGHTSALMON = (255, 160, 122)
LIGHTSEAGREEN = (32, 178, 170)
LIGHTSKYBLUE = (135, 206, 250)
LIGHTSLATEGRAY = (119, 136, 153)
LIGHTSTEELBLUE = (176, 196, 222)
LIGHTYELLOW = (255, 255, 224)
LIME = (0, 255, 0)
LIMEGREEN = (50, 205, 50)
LINEN = (250, 240, 230)
MAROON = (128, 0, 0)
MEDIUMAQUAMARINE = (102, 205, 170)
MEDIUMBLUE = (0, 0, 205)
MEDIUMORCHID = (186, 85, 211)
MEDIUMPURPLE = (147, 112, 219)
MEDIUMSEAGREEN = (60, 179, 113)
MEDIUMSLATEBLUE = (123, 104, 238)
MEDIUMSPRINGGREEN = (0, 250, 154)
MEDIUMTURQUOISE = (72, 209, 204)
MEDIUMVIOLETRED = (199, 21, 133)
MIDNIGHTBLUE = (25, 25, 112)
MINTCREAM = (245, 255, 250)
MISTYROSE = (255, 228, 225)
MOCCASIN = (255, 228, 181)
NAVAJOWHITE = (255, 222, 173)
NAVY = (0, 0, 128)
OLDLACE = (253, 245, 230)
OLIVE = (128, 128, 0)
OLIVEDRAB = (107, 142, 35)
ORANGE = (255, 165, 0)
ORANGERED = (255, 69, 0)
ORCHID = (218, 112, 214)
PALEGOLDENROD = (238, 232, 170)
PALEGREEN = (152, 251, 152)
PALETURQUOISE = (175, 238, 238)
PALEVIOLETRED = (219, 112, 147)
PAPAYAWHIP = (255, 239, 213)
PEACHPUFF = (255, 218, 185)
PERU = (205, 133, 63)
PINK = (255, 192, 203)
PLUM = (221, 160, 221)
POWDERBLUE = (176, 224, 230)
PURPLE = (128, 0, 128)
ROSYBROWN = (188, 143, 143)
ROYALBLUE = (65, 105, 225)
SADDLEBROWN = (139, 69, 19)
SALMON = (250, 128, 114)
SANDYBROWN = (244, 164, 96)
SEAGREEN = (46, 139, 87)
SEASHELL = (255, 245, 238)
SIENNA = (160, 82, 45)
SILVER = (192, 192, 192)
SKYBLUE = (135, 206, 235)
SLATEBLUE = (106, 90, 205)
SLATEGRAY = (112, 128, 144)
SNOW = (255, 250, 250)
SPRINGGREEN = (0, 255, 127)
STEELBLUE = (70, 130, 180)
TAN = (210, 180, 140)
TEAL = (0, 128, 128)
THISTLE = (216, 191, 216)
TOMATO = (255, 99, 71)
TURQUOISE = (64, 224, 208)
VIOLET = (238, 130, 238)
WHEAT = (245, 222, 179)
WHITESMOKE = (245, 245, 245)
YELLOWGREEN = (154, 205, 50)

MATERIAL_RED_50 = (255, 235, 238)
MATERIAL_RED_100 = (255, 205, 210)
MATERIAL_RED_200 = (239, 154, 154)
MATERIAL_RED_300 = (229, 115, 115)
MATERIAL_RED_400 = (239, 83, 80)
MATERIAL_RED_500 = (244, 67, 54)
MATERIAL_RED_600 = (229, 57, 53)
MATERIAL_RED_700 = (211, 47, 47)
MATERIAL_RED_800 = (198, 40, 40)
MATERIAL_RED_900 = (183, 28, 28)

MATERIAL_BLUE_50 = (227, 242, 253)
MATERIAL_BLUE_100 = (187, 222, 251)
MATERIAL_BLUE_200 = (144, 202, 249)
MATERIAL_BLUE_300 = (100, 181, 246)
MATERIAL_BLUE_400 = (66, 165, 245)
MATERIAL_BLUE_500 = (33, 150, 243)
MATERIAL_BLUE_600 = (30, 136, 229)
MATERIAL_BLUE_700 = (25, 118, 210)
MATERIAL_BLUE_800 = (21, 101, 192)
MATERIAL_BLUE_900 = (13, 71, 161)

MATERIAL_GREEN_50 = (232, 245, 233)
MATERIAL_GREEN_100 = (200, 230, 201)
MATERIAL_GREEN_200 = (165, 214, 167)
MATERIAL_GREEN_300 = (129, 199, 132)
MATERIAL_GREEN_400 = (102, 187, 106)
MATERIAL_GREEN_500 = (76, 175, 80)
MATERIAL_GREEN_600 = (67, 160, 71)
MATERIAL_GREEN_700 = (56, 142, 60)
MATERIAL_GREEN_800 = (46, 125, 50)
MATERIAL_GREEN_900 = (27, 94, 32)

MATERIAL_ORANGE_50 = (255, 243, 224)
MATERIAL_ORANGE_100 = (255, 224, 178)
MATERIAL_ORANGE_200 = (255, 204, 128)
MATERIAL_ORANGE_300 = (255, 183, 77)
MATERIAL_ORANGE_400 = (255, 167, 38)
MATERIAL_ORANGE_500 = (255, 152, 0)
MATERIAL_ORANGE_600 = (251, 140, 0)
MATERIAL_ORANGE_700 = (245, 124, 0)
MATERIAL_ORANGE_800 = (239, 108, 0)
MATERIAL_ORANGE_900 = (230, 81, 0)

MATERIAL_PURPLE_50 = (243, 229, 245)
MATERIAL_PURPLE_100 = (225, 190, 231)
MATERIAL_PURPLE_200 = (206, 147, 216)
MATERIAL_PURPLE_300 = (186, 104, 200)
MATERIAL_PURPLE_400 = (171, 71, 188)
MATERIAL_PURPLE_500 = (156, 39, 176)
MATERIAL_PURPLE_600 = (142, 36, 170)
MATERIAL_PURPLE_700 = (123, 31, 162)
MATERIAL_PURPLE_800 = (106, 27, 154)
MATERIAL_PURPLE_900 = (74, 20, 140)

RAINBOW_RED = (255, 0, 0)
RAINBOW_ORANGE = (255, 127, 0)
RAINBOW_YELLOW = (255, 255, 0)
RAINBOW_GREEN = (0, 255, 0)
RAINBOW_BLUE = (0, 0, 255)
RAINBOW_INDIGO = (75, 0, 130)
RAINBOW_VIOLET = (148, 0, 211)

PASTEL_PINK = (255, 209, 220)
PASTEL_BLUE = (174, 198, 207)
PASTEL_GREEN = (119, 221, 119)
PASTEL_YELLOW = (253, 253, 150)
PASTEL_ORANGE = (255, 179, 71)
PASTEL_PURPLE = (179, 158, 181)
PASTEL_RED = (255, 105, 97)
PASTEL_CYAN = (119, 221, 231)

NEON_PINK = (255, 16, 240)
NEON_GREEN = (57, 255, 20)
NEON_BLUE = (31, 81, 255)
NEON_YELLOW = (255, 255, 49)
NEON_ORANGE = (255, 95, 31)
NEON_PURPLE = (191, 64, 191)
NEON_CYAN = (0, 255, 255)

GOLD_METALLIC = (212, 175, 55)
SILVER_METALLIC = (192, 192, 192)
BRONZE_METALLIC = (205, 127, 50)
COPPER_METALLIC = (184, 115, 51)
PLATINUM_METALLIC = (229, 228, 226)

EARTH_BROWN = (101, 67, 33)
EARTH_GREEN = (102, 51, 0)
EARTH_RED = (123, 63, 0)
EARTH_YELLOW = (153, 102, 51)
EARTH_ORANGE = (204, 119, 34)

TWILIGHT_PURPLE = (72, 61, 139)
TWILIGHT_BLUE = (25, 25, 112)
TWILIGHT_PINK = (255, 20, 147)
TWILIGHT_ORANGE = (255, 99, 71)

OCEAN_BLUE = (0, 119, 190)
OCEAN_GREEN = (0, 150, 136)
OCEAN_TEAL = (0, 131, 143)
OCEAN_NAVY = (0, 77, 64)

FOREST_GREEN = (34, 139, 34)
FOREST_BROWN = (101, 67, 33)
FOREST_MOSS = (173, 223, 173)
FOREST_PINE = (1, 68, 33)

BURNT_ORANGE = (204, 85, 0)
FOREST_RANGER = (95, 39, 205)
MIDNIGHT_EXPRESS = (36, 10, 64)
GOLDEN_POPPY = (252, 194, 0)
ELECTRIC_LIME = (204, 255, 0)
HOT_MAGENTA = (255, 29, 206)
VIVID_VIOLET = (159, 0, 255)
SPRING_BUD = (167, 252, 0)
ELECTRIC_BLUE = (125, 249, 255)
BRIGHT_TURQUOISE = (8, 232, 222)
CYBER_YELLOW = (255, 211, 0)
RADICAL_RED = (255, 53, 94)
SHOCKING_PINK = (252, 15, 192)
LASER_LEMON = (254, 254, 34)
SCREAMIN_GREEN = (118, 255, 122)
ELECTRIC_PURPLE = (191, 0, 255)
BLIZZARD_BLUE = (172, 229, 238)
ATOMIC_TANGERINE = (255, 153, 102)
WILD_STRAWBERRY = (255, 67, 164)
OUTRAGEOUS_ORANGE = (255, 110, 74)

colorz = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, DARK_RED, DARK_GREEN, DARK_BLUE, DARK_YELLOW, DARK_CYAN, DARK_MAGENTA, DARK_GRAY, DARK_GREY, LIGHT_RED, LIGHT_GREEN, LIGHT_BLUE, LIGHT_YELLOW, LIGHT_CYAN, LIGHT_PINK, LIGHT_GRAY, LIGHT_GREY, ALICEBLUE, ANTIQUEWHITE, AQUA, AQUAMARINE, AZURE, BEIGE, BISQUE, BLANCHEDALMOND, BLUEVIOLET, BROWN, BURLYWOOD, CADETBLUE, CHARTREUSE, CHOCOLATE, CORAL, CORNFLOWERBLUE, CORNSILK, CRIMSON, DARKBLUE, DARKCYAN, DARKGOLDENROD, DARKGREEN, DARKKHAKI, DARKMAGENTA, DARKOLIVEGREEN, DARKORANGE, DARKORCHID, DARKRED, DARKSALMON, DARKSEAGREEN, DARKSLATEBLUE, DARKSLATEGRAY, DARKTURQUOISE, DARKVIOLET, DEEPPINK, DEEPSKYBLUE, DIMGRAY, DODGERBLUE, FIREBRICK, FLORALWHITE, FORESTGREEN, FUCHSIA, GAINSBORO, GHOSTWHITE, GOLD, GOLDENROD, GRAY, GREY, GREENYELLOW, HONEYDEW, HOTPINK, INDIANRED, INDIGO, IVORY, KHAKI, LAVENDER, LAVENDERBLUSH, LAWNGREEN, LEMONCHIFFON, LIGHTBLUE, LIGHTCORAL, LIGHTCYAN, LIGHTGOLDENRODYELLOW, LIGHTGREEN, LIGHTPINK, LIGHTSALMON, LIGHTSEAGREEN, LIGHTSKYBLUE, LIGHTSLATEGRAY, LIGHTSTEELBLUE, LIGHTYELLOW, LIME, LIMEGREEN, LINEN, MAROON, MEDIUMAQUAMARINE, MEDIUMBLUE, MEDIUMORCHID, MEDIUMPURPLE, MEDIUMSEAGREEN, MEDIUMSLATEBLUE, MEDIUMSPRINGGREEN, MEDIUMTURQUOISE, MEDIUMVIOLETRED, MIDNIGHTBLUE, MINTCREAM, MISTYROSE, MOCCASIN, NAVAJOWHITE, NAVY, OLDLACE, OLIVE, OLIVEDRAB, ORANGE, ORANGERED, ORCHID, PALEGOLDENROD, PALEGREEN, PALETURQUOISE, PALEVIOLETRED, PAPAYAWHIP, PEACHPUFF, PERU, PINK, PLUM, POWDERBLUE, PURPLE, ROSYBROWN, ROYALBLUE, SADDLEBROWN, SALMON, SANDYBROWN, SEAGREEN, SEASHELL, SIENNA, SILVER, SKYBLUE, SLATEBLUE, SLATEGRAY, SNOW, SPRINGGREEN, STEELBLUE, TAN, TEAL, THISTLE, TOMATO, TURQUOISE, VIOLET, WHEAT, WHITESMOKE, YELLOWGREEN, MATERIAL_RED_50, MATERIAL_RED_100, MATERIAL_RED_200, MATERIAL_RED_300, MATERIAL_RED_400, MATERIAL_RED_500, MATERIAL_RED_600, MATERIAL_RED_700, MATERIAL_RED_800, MATERIAL_RED_900, MATERIAL_BLUE_50, MATERIAL_BLUE_100, MATERIAL_BLUE_200, MATERIAL_BLUE_300, MATERIAL_BLUE_400, MATERIAL_BLUE_500, MATERIAL_BLUE_600, MATERIAL_BLUE_700, MATERIAL_BLUE_800, MATERIAL_BLUE_900, MATERIAL_GREEN_50, MATERIAL_GREEN_100, MATERIAL_GREEN_200, MATERIAL_GREEN_300, MATERIAL_GREEN_400, MATERIAL_GREEN_500, MATERIAL_GREEN_600, MATERIAL_GREEN_700, MATERIAL_GREEN_800, MATERIAL_GREEN_900, MATERIAL_ORANGE_50, MATERIAL_ORANGE_100, MATERIAL_ORANGE_200, MATERIAL_ORANGE_300, MATERIAL_ORANGE_400, MATERIAL_ORANGE_500, MATERIAL_ORANGE_600, MATERIAL_ORANGE_700, MATERIAL_ORANGE_800, MATERIAL_ORANGE_900, MATERIAL_PURPLE_50, MATERIAL_PURPLE_100, MATERIAL_PURPLE_200, MATERIAL_PURPLE_300, MATERIAL_PURPLE_400, MATERIAL_PURPLE_500, MATERIAL_PURPLE_600, MATERIAL_PURPLE_700, MATERIAL_PURPLE_800, MATERIAL_PURPLE_900, RAINBOW_RED, RAINBOW_ORANGE, RAINBOW_YELLOW, RAINBOW_GREEN, RAINBOW_BLUE, RAINBOW_INDIGO, RAINBOW_VIOLET, PASTEL_PINK, PASTEL_BLUE, PASTEL_GREEN, PASTEL_YELLOW, PASTEL_ORANGE, PASTEL_PURPLE, PASTEL_RED, PASTEL_CYAN, NEON_PINK, NEON_GREEN, NEON_BLUE, NEON_YELLOW, NEON_ORANGE, NEON_PURPLE, NEON_CYAN, GOLD_METALLIC, SILVER_METALLIC, BRONZE_METALLIC, COPPER_METALLIC, PLATINUM_METALLIC, EARTH_BROWN, EARTH_GREEN, EARTH_RED, EARTH_YELLOW, EARTH_ORANGE, TWILIGHT_PURPLE, TWILIGHT_BLUE, TWILIGHT_PINK, TWILIGHT_ORANGE, OCEAN_BLUE, OCEAN_GREEN, OCEAN_TEAL, OCEAN_NAVY, FOREST_GREEN, FOREST_BROWN, FOREST_MOSS, FOREST_PINE, BURNT_ORANGE, FOREST_RANGER, MIDNIGHT_EXPRESS, GOLDEN_POPPY, ELECTRIC_LIME, HOT_MAGENTA, VIVID_VIOLET, SPRING_BUD, ELECTRIC_BLUE, BRIGHT_TURQUOISE, CYBER_YELLOW, RADICAL_RED, SHOCKING_PINK, LASER_LEMON, SCREAMIN_GREEN, ELECTRIC_PURPLE, BLIZZARD_BLUE, ATOMIC_TANGERINE, WILD_STRAWBERRY, OUTRAGEOUS_ORANGE]

Paddle_Width = 100
Paddle_Height = 15
Paddle_Speed = 10
Ball_size = 10
Ball_speed = 5
Brick_Width = 75
Brick_Height = 25
Brick_rows = 8
Brick_Cols = 10
Brick_padding = 5

def color_brightness(color):
    return (color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114)

def are_colors_different(color1, color2, threshold=100):
    r_diff = abs(color1[0] - color2[0])
    g_diff = abs(color1[1] - color2[1])
    b_diff = abs(color1[2] - color2[2])
    total_diff = r_diff + g_diff + b_diff
    return total_diff > threshold

def get_contrasting_colors(num_colors):
    selected = []
    attempts = 0
    max_attempts = 1000
    
    while len(selected) < num_colors and attempts < max_attempts:
        color = random.choice(colorz)
        
        if len(selected) == 0:
            selected.append(color)
        else:
            is_good = True
            for existing in selected:
                if not are_colors_different(color, existing, threshold=150):
                    is_good = False
                    break
            
            if is_good:
                selected.append(color)
        
        attempts += 1
    
    while len(selected) < num_colors:
        selected.append(random.choice(colorz))
    
    return selected

class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.size = Ball_size
        self.dx = Ball_speed * random.choice((1, -1))
        self.dy = -Ball_speed
        self.color = color

    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.x <= self.size or self.x >= SCREEN_WIDTH - self.size:
            self.dx *= -1
        
        if self.y <= self.size:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))
    
    def get_rect(self):
        return pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)

class Paddle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = Paddle_Width
        self.height = Paddle_Height
        self.speed = Paddle_Speed
        self.color = color

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Brick:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = Brick_Width
        self.height = Brick_Height
        self.color = color
        self.destroyed = False
    
    def draw(self, screen):
        if not self.destroyed:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Brick Breaker - Colorful Edition")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.won = False
        
        game_colors = get_contrasting_colors(3)
        self.ball_color = game_colors[0]
        self.paddle_color = game_colors[1]
        self.bg_color = game_colors[2]
        
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, self.ball_color)
        self.paddle = Paddle(SCREEN_WIDTH // 2 - Paddle_Width // 2, SCREEN_HEIGHT - 50, self.paddle_color)
        
        self.bricks = []
        self.all_colors = colorz.copy()
        random.shuffle(self.all_colors)
        self.color_index = 0
        self.wave = 1
        self.create_bricks()
        
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def create_bricks(self):
        offset_x = (SCREEN_WIDTH - (Brick_Cols * (Brick_Width + Brick_padding))) // 2
        offset_y = 50
        
        for row in range(Brick_rows):
            for col in range(Brick_Cols):
                x = offset_x + col * (Brick_Width + Brick_padding)
                y = offset_y + row * (Brick_Height + Brick_padding)
                brick_color = self.all_colors[self.color_index % len(self.all_colors)]
                self.bricks.append(Brick(x, y, brick_color))
                self.color_index += 1

    def check_collision(self):
        ball_rect = self.ball.get_rect()
        paddle_rect = self.paddle.get_rect()
        
        if ball_rect.colliderect(paddle_rect) and self.ball.dy > 0:
            self.ball.dy *= -1
            hit_pos = (self.ball.x - self.paddle.x) / self.paddle.width
            self.ball.dx = float((hit_pos - 0.5) * Ball_speed * 2)
        
        for brick in self.bricks:
            if not brick.destroyed and ball_rect.colliderect(brick.get_rect()):
                brick.destroyed = True
                self.ball.dy *= -1
                self.score += 10
                break

    def update(self):
        if self.game_over or self.won:
            return
        
        keys = pygame.key.get_pressed()
        self.paddle.update(keys)
        self.ball.update()
        self.check_collision()
        
        if self.ball.y > SCREEN_HEIGHT:
            self.game_over = True
        
        if all(brick.destroyed for brick in self.bricks):
            if self.color_index < len(self.all_colors):
                self.wave += 1
                self.ball.x = SCREEN_WIDTH // 2
                self.ball.y = SCREEN_HEIGHT - 100
                self.ball.dx = Ball_speed * random.choice((1, -1))
                self.ball.dy = -Ball_speed
                self.create_bricks()
            else:
                self.won = True

    def draw(self):
        self.screen.fill(self.bg_color)
        
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        
        for brick in self.bricks:
            brick.draw(self.screen)
        
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        wave_text = self.font.render(f"Wave: {self.wave}", True, WHITE)
        self.screen.blit(wave_text, (10, 50))
        
        colors_used = min(self.color_index, len(self.all_colors))
        color_progress = self.font.render(f"Colors: {colors_used}/{len(self.all_colors)}", True, WHITE)
        self.screen.blit(color_progress, (SCREEN_WIDTH - 200, 10))
        
        if self.game_over:
            game_over_text = self.font.render("GAME OVER! Press R to Restart", True, RED)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
        
        if self.won:
            win_text = self.font.render("YOU WIN! Press R to Restart", True, GREEN)
            text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(win_text, text_rect)
        
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and (self.game_over or self.won):
                    self.__init__()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
