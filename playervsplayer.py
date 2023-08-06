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

        if self.ball_group.sprite.rect.top <= 10 or self.ball_group.sprite.rect.bottom >= self.screen_height + 10:
            pygame.mixer.Sound.play(self.plob_sound)
            self.ball_group.sprite.speed_y *= -1
            self.ball_group.sprite.active_animation = True

        if self.ball_group.sprite.active_animation and (
                self.ball_group.sprite.speed_x ** 2 + self.ball_group.sprite.speed_y ** 2) ** 0.5 >= 3:
            self.ball_group.sprite.current_sprite += 1
            self.ball_group.sprite.image = self.ball_group.sprite.sprites[self.ball_group.sprite.current_sprite]
            self.ball_group.sprite.spr_list_anim -= 1

            if not self.ball_group.sprite.spr_list_anim:
                self.ball_group.sprite.spr_list_anim = len(self.ball_group.sprite.sprites) - 1
                self.ball_group.sprite.current_sprite = 0
                self.ball_group.sprite.active_animation = False

            self.ball_group.sprite.image = self.ball_group.sprite.sprites[self.ball_group.sprite.current_sprite]

            # for i in range(len(self.ball_group.sprite.sprites)): print(1) self.ball_group.sprite.current_sprite = (
            # self.ball_group.sprite.current_sprite + 1) % (len(self.ball_group.sprite.sprites))
            # self.ball_group.sprite.image = self.ball_group.sprite.sprites[self.ball_group.sprite.current_sprite]
            # self.ball_group.draw(self.screen) self.ball_group.update()

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
