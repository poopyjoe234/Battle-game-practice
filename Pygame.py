import pygame
from sys import exit
import Testing_rewrite

pygame.init()

class GameWords:
    def __init__(self):
        self.font = pygame.font.Font('Font/advanced_pixel-7.ttf', 50)
        self.text_surface = self.font.render('Battle Game', False, (0, 0, 0))
        pygame.display.set_caption('Battle Game')

class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()
class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((800, 400))

class GroundSurface:
    def __init__(self):
        self.ground_surface = pygame.image.load('Graphics/castleground_scaled.png').convert_alpha()

class SkySurface:
    def __init__(self):
        self.sky_surface = pygame.image.load('Graphics/castlecastle_scaled.png').convert_alpha()

class EnemySurface:
    def __init__(self):
        self.enemy_surface = pygame.image.load('Graphics/goblinsingle.png').convert_alpha()
        self.enemy_x_pos = 0
        self.enemy_y_pos = 270

class PlayerSurface:
    def __init__(self):
        self.player_surface = pygame.image.load('Graphics/Image6.png').convert_alpha()


game_title = GameWords()
game_clock = Clock()
game_screen = Screen()
ground = GroundSurface()
sky = SkySurface()
enemy = EnemySurface()
player = PlayerSurface()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    game_screen.display.blit(sky.sky_surface, (0,0))
    game_screen.display.blit(ground.ground_surface, (0, 315))
    game_screen.display.blit(game_title.text_surface, (300, 100))
    game_screen.display.blit(player.player_surface, (500, 270))
    game_screen.display.blit(enemy.enemy_surface, (enemy.enemy_x_pos, enemy.enemy_y_pos))
    enemy.enemy_x_pos += 5
    if enemy.enemy_x_pos == 800:
        enemy.enemy_x_pos = 0

    pygame.display.update()
    game_clock.clock.tick(60)

