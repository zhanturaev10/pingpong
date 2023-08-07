import pygame


class Settings:
    def __init__(self, game):
        self.game = game
        self.max_ball_speed = 8
        self.ball = "ball_1"
        self.player_acceleration = 0.3
        self.player_brake = 0.35
        self.current_res_index = 0
        self.res_options = [(1920, 1080), (1600, 900), (1280, 1024), (800, 600)]

    def draw_settings(self):
        while True:
            self.game.screen.fill((0, 0, 0))

            settings_items = [
                {"text": "Change resolution", "action": self.change_resolution},
                {"text": "Change ball settings", "action": self.change_ball_settings},
                {"text": "Change player settings", "action": self.change_player_settings},
                {"text": "Change sound", "action": self.change_sound},
            ]

            for i, item in enumerate(settings_items):
                text_surface = self.game.font.render(item["text"], True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(self.game.screen.get_width() / 2, 100 + i * 100))
                self.game.screen.blit(text_surface, text_rect)

            back_arrow_surface = self.game.font.render("<", True, (255, 255, 255))
            back_arrow_rect = back_arrow_surface.get_rect(topleft=(20, 20))
            self.game.screen.blit(back_arrow_surface, back_arrow_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, item in enumerate(settings_items):
                        text_surface = self.game.font.render(item["text"], True, (255, 255, 255))
                        text_rect = text_surface.get_rect(center=(self.game.screen.get_width() / 2, 100 + i * 100))
                        if text_rect.collidepoint(event.pos):
                            item["action"]()
                    if back_arrow_rect.collidepoint(event.pos):
                        return

            pygame.display.flip()

    def change_resolution(self):
        while True:
            self.game.screen.fill((0, 0, 0))

            current_res = self.res_options[self.current_res_index]

            back_arrow_surface = self.game.font.render("<", True, (255, 255, 255))
            back_arrow_rect = back_arrow_surface.get_rect(topleft=(20, 20))
            self.game.screen.blit(back_arrow_surface, back_arrow_rect)

            res_text = "{}x{}".format(current_res[0], current_res[1])
            res_text_surface = self.game.font.render(res_text, True, (255, 255, 255))
            res_text_rect = res_text_surface.get_rect(
                center=(self.game.screen.get_width() / 2, self.game.screen.get_height() / 2))
            self.game.screen.blit(res_text_surface, res_text_rect)

            res_increase_rect = None
            res_arrow_rect = None

            if self.current_res_index >= 1:
                res_increase_surface = self.game.font.render(">", True, (255, 255, 255))
                res_increase_rect = res_increase_surface.get_rect(
                    topleft=(res_text_rect.right + 10, res_text_rect.centery))
                self.game.screen.blit(res_increase_surface, res_increase_rect)

            if self.current_res_index < len(self.res_options) - 1:
                res_arrow_surface = self.game.font.render("<", True, (255, 255, 255))
                res_arrow_rect = res_arrow_surface.get_rect(
                    topright=(res_text_rect.left - 10, res_text_rect.centery))
                self.game.screen.blit(res_arrow_surface, res_arrow_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_arrow_rect.collidepoint(event.pos):
                        return
                    elif res_arrow_rect and res_arrow_rect.collidepoint(event.pos):
                        self.current_res_index += 1
                    elif res_increase_rect and res_increase_rect.collidepoint(event.pos):
                        self.current_res_index -= 1

            current_res = self.res_options[self.current_res_index]
            self.game.screen = pygame.display.set_mode(current_res)
            pygame.display.flip()

    # Implement other settings functions (change_ball_settings, change_player_settings, change_sound) here

