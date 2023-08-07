import pygame
import sys
import random


class GameManager:
    def __init__(self, paddle_group, screen, screen_width, screen_height, ball_group, plob_sound):
        self.basic_font = pygame.font.SysFont('comicsansms', 32)
        self.accent_color = (27, 35, 43)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.screen = screen
        self.paddle_group = paddle_group
        self.plob_sound = plob_sound

    def run_game(self):
        # Drawing the game objects
        self.paddle_group.draw(self.screen)
        self.ball_group.draw(self.screen)

        # Updating the game objects
        self.paddle_group.update()
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    def reset_ball(self):
        if (self.ball_group.sprite.rect.top <= 10 or self.ball_group.sprite.rect.bottom >= self.screen_height + 10):
            pygame.mixer.Sound.play(self.plob_sound)
            self.ball_group.sprite.speed_y *= -1
            self.ball_group.sprite.active_animation = True

        if self.ball_group.sprite.active_animation and (
                self.ball_group.sprite.speed_x ** 2 + self.ball_group.sprite.speed_y ** 2) ** 0.5 >= 3:
            self.ball_group.sprite.current_sprite += 1
            self.ball_group.sprite.image = self.ball_group.sprite.sprites[self.ball_group.sprite.current_sprite]
            self.ball_group.sprite.spr_list_anim -= 1

            if not (self.ball_group.sprite.spr_list_anim):
                self.ball_group.sprite.spr_list_anim = len(self.ball_group.sprite.sprites) - 1
                self.ball_group.sprite.current_sprite = 0
                self.ball_group.sprite.active_animation = False

            self.ball_group.sprite.image = self.ball_group.sprite.sprites[self.ball_group.sprite.current_sprite]

        if self.ball_group.sprite.rect.right >= self.screen_width:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self):
        player_score = self.basic_font.render(str(self.player_score), True, self.accent_color)
        opponent_score = self.basic_font.render(str(self.opponent_score), True, self.accent_color)

        player_score_rect = player_score.get_rect(midleft=(self.screen_width / 2 + 40, self.screen_height / 2))
        opponent_score_rect = opponent_score.get_rect(midright=(self.screen_width / 2 - 40, self.screen_height / 2))

        self.screen.blit(player_score, player_score_rect)
        self.screen.blit(opponent_score, opponent_score_rect)


class Bot(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, max_speed, screen_height, screen_width, ball_group):
        super().__init__()
        self.max_speed = max_speed
        self.ball_group = ball_group
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.screen_height = screen_height
        self.screen_width = screen_width

    def update(self):
        if self.rect.centery < self.ball_group.sprite.rect.centery:
            self.rect.centery += min(abs(self.rect.centery - self.ball_group.sprite.rect.centery), self.max_speed)
        elif self.rect.centery > self.ball_group.sprite.rect.centery:
            self.rect.centery -= min(abs(self.rect.centery - self.ball_group.sprite.rect.centery), self.max_speed)

        # Constrain the bot's paddle within the screen bounds
        if self.rect.top <= 0:
            self.rect.top = 1
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
