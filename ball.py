import math
import random

import pygame

import gl_functions

pygame.mixer.init(44100, -16, 2, 512)

plob_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")


class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, part_of_name):
        super().__init__()
        self.sprites = gl_functions.load_image(path, part_of_name)
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class Ball(Block):
    def __init__(self, path, x_pos, y_pos, speed_x, speed_y, paddles, screen_width, screen_height, max_speed, elas_coef,
                 screen, part_of_name):
        super().__init__(path, x_pos, y_pos, part_of_name)
        self.screen = screen
        self.basic_font = pygame.font.SysFont('comicsansms', 32)
        self.accent_color = (27, 35, 43)
        self.bg_color = pygame.Color('#2F373F')
        self.current_sprite = 0
        self.first_speed_x = speed_x * random.choice((-1, 1))
        self.first_speed_y = speed_y * random.choice((-1, 1))
        self.speed_x = speed_x * random.choice((-1, 1))
        self.speed_y = speed_y * random.choice((-1, 1))
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.paddles = paddles
        self.max_speed = max_speed
        self.elas_coef = elas_coef
        self.active = False
        self.active_animation = False
        self.spr_list_anim = len(self.sprites) - 1
        self.score_time = 0

    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart_counter()

    def f(self, x, y, target, coef):
        return (target - x) * math.exp(-coef * y)

    def collisions(self):


        if pygame.sprite.spritecollide(self, self.paddles, False):
            pygame.mixer.Sound.play(plob_sound)
            collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)
            for spr2 in collision_paddle:
                if self.rect.colliderect(spr2.rect):
                    spr = spr2
                    break

            if abs(self.rect.right - spr.rect.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
                if spr.velocity > 0:
                    self.speed_y += self.f(self.speed_y, spr.velocity, self.max_speed, 0.25)
                    print('self.speed_y =', self.speed_y, 'spr.velocity > 0', 'spr.velociyt =', spr.velocity,
                          'self.f(self.speed_y,spr.velocity,self.max_speed,-0.25) =',
                          self.f(self.speed_y, spr.velocity, self.max_speed, -0.25))
                elif spr.velocity < 0:
                    self.speed_y = -(-self.speed_y + self.f(-self.speed_y, -spr.velocity, self.max_speed, 0.25))
                    print('self.speed_y =', self.speed_y, 'spr.velocity < 0', 'spr.velociyt =', spr.velocity,
                          'self.f(-self.speed_y,-spr.velocity,self.max_speed,-0.25) =',
                          self.f(-self.speed_y, -spr.velocity, self.max_speed, -0.25))

            if abs(self.rect.left - spr.rect.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
                if spr.velocity > 0:
                    self.speed_y += self.f(self.speed_y, spr.velocity, self.max_speed, 0.25)
                    print('self.speed_y =', self.speed_y, 'spr.velocity > 0', 'spr.velociyt =', spr.velocity,
                          'self.f(self.speed_y,spr.velocity,self.max_speed,-0.25) -',
                          self.f(self.speed_y, spr.velocity, self.max_speed, -0.25))
                elif spr.velocity < 0:
                    self.speed_y = -(-self.speed_y + self.f(-self.speed_y, -spr.velocity, self.max_speed, 0.25))
                    print('self.speed_y =', self.speed_y, 'spr.velocity < 0', 'spr.velociyt =', spr.velocity,
                          'self.f(-self.speed_y,-spr.velocity,self.max_speed,-0.25) =',
                          self.f(-self.speed_y, -spr.velocity, self.max_speed, -0.25))

            if abs(self.rect.top - spr.rect.bottom) < 10 and self.speed_y < 0:
                self.rect.top = spr.rect.bottom
                self.speed_y *= -1 * (self.elas_coef * random.uniform(0, 1))

            if abs(self.rect.bottom - spr.rect.top) < 10 and self.speed_y > 0:
                self.rect.bottom = spr.rect.top
                self.speed_y *= -1 * (self.elas_coef * random.uniform(0, 1))

    def reset_ball(self):
        self.active = False
        self.speed_x = self.first_speed_x * random.choice((-1, 1))
        self.speed_y = self.first_speed_y * random.choice((-1, 1))
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (self.screen_width / 2, self.screen_height / 2)
        pygame.mixer.Sound.play(score_sound)

    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown_number = 3

        if current_time - self.score_time <= 700:
            countdown_number = 3
        if 700 < current_time - self.score_time <= 1400:
            countdown_number = 2
        if 1400 < current_time - self.score_time <= 2100:
            countdown_number = 1
        if current_time - self.score_time >= 2100:
            self.active = True

        time_counter = self.basic_font.render(str(countdown_number), True, self.accent_color)
        time_counter_rect = time_counter.get_rect(center=(self.screen_width / 2, self.screen_height / 2 + 50))
        pygame.draw.rect(self.screen, self.bg_color, time_counter_rect)
        self.screen.blit(time_counter, time_counter_rect)
