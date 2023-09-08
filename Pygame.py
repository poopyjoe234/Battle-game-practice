import time
import pygame
from sys import exit
import random

pygame.init()


class GameWordDesign:
    def __init__(self):
        self.font = pygame.font.Font('Font/advanced_pixel-7.ttf', 50)
        pygame.display.set_caption('Battle Game')


class ScoreSurface:
    def __init__(self):
        self.font = pygame.font.Font('Font/advanced_pixel-7.ttf', 50)
        self.score_surf = self.font.render('Battle Game', False, (0, 0, 0))
        self.score_rect = self.score_surf.get_rect(center=(400, 100))
        self.game_over_surf = self.font.render('GAME OVER', False, (0, 0, 0))
        self.game_over_rect = self.game_over_surf.get_rect(center=(400,100))


class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((800, 400))


class GroundSurface:
    def __init__(self):
        self.ground_surface = pygame.image.load('Graphics/castleground.png').convert_alpha()


class SkySurface:
    def __init__(self):
        self.sky_surface = pygame.image.load('Graphics/castlecastle.png').convert_alpha()


class EnemySurface:
    def __init__(self):
        self.enemy_surface = pygame.image.load('Graphics/goblinsingle.png').convert_alpha()
        self.enemy_rect = self.enemy_surface.get_rect(midbottom=(10, 331))

    def enemy_rect_x_movement(self):
        self.enemy_rect.x += 3

        if self.enemy_rect.left >= 800:
            self.enemy_rect.x = -30


class PlayerSurface:
    def __init__(self):
        self.player_surface = pygame.image.load('Graphics/Image6.png').convert_alpha()
        self.player_rect = self.player_surface.get_rect(midbottom=(500, 330))
        self.gravity = 0


class Mouse:

    @staticmethod
    def get_mouse_pos():
        mouse_pos = pygame.mouse.get_pos()
        if player_surf.player_rect.collidepoint(mouse_pos):
            print('collision\n')

    @staticmethod
    def mouse_button_pressed():
        print(pygame.mouse.get_pressed())

    @staticmethod
    def mouse_cords():
        for event in pygame.event.get(pygame.MOUSEMOTION):  # Only get MOUSEMOTION events
            print(event.pos)

    @staticmethod
    def mouse_down():
        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('Mouse button down')

    @staticmethod
    def mouse_up():
        if pygame.event.get(pygame.MOUSEBUTTONUP):
            print('Mouse button up')

    @staticmethod
    def mouse_up_down():
        mouse.mouse_down()
        mouse.mouse_up()


class Keyboard:
    def __init__(self):
        self.get_key_pressed()

    @staticmethod
    def get_key_pressed():
        print(pygame.key.get_pressed())

    @staticmethod
    def is_key_down():
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.type == pygame.KEYDOWN:
                print('key down')

    @staticmethod
    def is_key_up():
        for event in pygame.event.get(pygame.KEYUP):
            if event.type == pygame.KEYUP:
                print('key up')

    def is_key_up_or_down(self):
        self.is_key_up()
        self.is_key_down()


class CharacterActions:

    @staticmethod
    def jump(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_surf.gravity = -20
                print('jump')

    @staticmethod
    def jump_mouse():
        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_surf.gravity = -20
                print('jump')


class CharacterPhysics:
    @staticmethod
    def gravity_on():
        player_surf.gravity += 1
        player_surf.player_rect.y += player_surf.gravity

        if player_surf.player_rect.bottom >= 330:
            player_surf.player_rect.bottom = 330


def exit_pygame(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()


def for_event_list():
    for event in pygame.event.get():
        exit_pygame(event)
        character_actions.jump(event)


score_surface = ScoreSurface()
game_title = GameWordDesign()
game_clock = Clock()
game_screen = Screen()
ground = GroundSurface()
sky = SkySurface()
enemy = EnemySurface()
player_surf = PlayerSurface()
mouse = Mouse()
keyboard = Keyboard()
character_physics = CharacterPhysics()
character_actions = CharacterActions()

game_active = True

while True:

    for_event_list()

    character_physics.gravity_on()

    if game_active:
        game_screen.display.blit(sky.sky_surface, (0, 0))
        game_screen.display.blit(ground.ground_surface, (0, 315))
        game_screen.display.blit(score_surface.score_surf, score_surface.score_rect)
        game_screen.display.blit(player_surf.player_surface, player_surf.player_rect)

        game_screen.display.blit(enemy.enemy_surface, enemy.enemy_rect)
        enemy.enemy_rect_x_movement()

        if enemy.enemy_rect.colliderect(player_surf.player_rect):
            game_active = False

    else:
        game_screen.display.fill('Yellow')

    pygame.display.update()
    game_clock.clock.tick(60)

