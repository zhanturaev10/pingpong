import tkinter
import tkinter.filedialog

import pygame
import pygame_widgets
import sys
from pygame_widgets.button import Button

import gl_functions
import ui


class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, part_of_name):
        super().__init__()
        self.sprites = gl_functions.load_image(path, part_of_name)
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class Settings:
    def __init__(self, game):
        self.game = game
        self.max_ball_speed = 8
        self.ball = "ball_1"
        self.player_acceleration = 0.3
        self.player_brake = 0.35

    def draw_settings(self):

        settings_items = [
            {"text": "Change resolution", "action": self.change_resolution},
            {"text": "Change ball settings", "action": self.change_ball_settings},
            {"text": "Change player settings", "action": self.change_player_settings},
            {"text": "Change sound", "action": self.change_sound},
        ]

        while True:
            self.game.screen.fill((0, 0, 0))

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
                    sys.exit()
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
            self.screen.fill((0, 0, 0))

            res_options = [(1920, 1080), (1600, 900), (1280, 1024), (800, 600)]

            current_res = res_options[self.current_res_index]

            back_arrow_surface = self.font.render("<", True, (255, 255, 255))
            back_arrow_rect = back_arrow_surface.get_rect(topleft=(20, 20))
            self.screen.blit(back_arrow_surface, back_arrow_rect)

            res_text = "{}x{}".format(current_res[0], current_res[1])
            res_text_surface = self.font.render(res_text, True, (255, 255, 255))
            res_text_rect = res_text_surface.get_rect(
                center=(self.screen.get_width() / 2, self.screen.get_height() / 2))
            self.screen.blit(res_text_surface, res_text_rect)

            res_increase_rect = None
            res_arrow_rect = None

            if self.current_res_index >= 1:
                # Draw resolution increase arrow
                res_increase_surface = self.font.render(">", True, (255, 255, 255))
                res_increase_rect = res_increase_surface.get_rect(
                    topleft=(res_text_rect.right + 10, res_text_rect.centery))
                self.screen.blit(res_increase_surface, res_increase_rect)

            if self.current_res_index < len(res_options) - 1:
                res_arrow_surface = self.font.render("<", True, (255, 255, 255))
                res_arrow_rect = res_arrow_surface.get_rect(
                    topright=(res_text_rect.left - 10, res_text_rect.centery))
                self.screen.blit(res_arrow_surface, res_arrow_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_arrow_rect.collidepoint(event.pos):
                        return
                    elif res_arrow_rect and res_arrow_rect.collidepoint(event.pos):
                        self.current_res_index += 1
                    elif res_increase_rect and res_increase_rect.collidepoint(event.pos):
                        self.current_res_index -= 1

            current_res = res_options[self.current_res_index]
            self.screen = pygame.display.set_mode(current_res)

            # Update the display
            pygame.display.flip()

    def change_ball_settings(self):

        slider = ui.Slider((self.game.screen.get_width() / 2) - 100, 250, 200, 10)

        while True:
            self.game.screen.fill((0, 0, 0))

            back_arrow_surface = self.game.font.render("<", True, (255, 255, 255))
            back_arrow_rect = back_arrow_surface.get_rect(topleft=(20, 20))
            self.game.screen.blit(back_arrow_surface, back_arrow_rect)

            text_surface = self.game.font.render("Max ball speed: {}".format(self.max_ball_speed), True,
                                                 (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.game.screen.get_width() / 2, 200))
            self.game.screen.blit(text_surface, text_rect)

            slider.draw(self.game.screen)

            text_surface = self.game.font.render("Ball's texture:", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.game.screen.get_width() / 2, 400))
            self.game.screen.blit(text_surface, text_rect)

            black_texure = gl_functions.load_image('ball\small_balls', "ball_1")[0]
            black_texure = pygame.transform.scale(black_texure,
                                                  (black_texure.get_width() * 3, black_texure.get_height() * 3))
            black_texure_rect = black_texure.get_rect()
            black_texure_rect.center = self.game.screen.get_width() / 2 - 50, 475
            self.game.screen.blit(black_texure, black_texure_rect)

            white_texture = gl_functions.load_image('ball\small_balls', "ball_2")[0]
            white_texture = pygame.transform.scale(white_texture,
                                                   (white_texture.get_width() * 3, white_texture.get_height() * 3))
            white_texture_rect = white_texture.get_rect()
            white_texture_rect.center = self.game.screen.get_width() / 2 + 50, 475
            self.game.screen.blit(white_texture, white_texture_rect)

            # blue_ball_texture = gl_functions.load_image('ball\small_balls', "blue_ball")[0]
            # blue_ball_texture = pygame.transform.scale(blue_ball_texture, (blue_ball_texture.get_width()*3, blue_ball_texture.get_height()*3))
            # blue_ball_rect = blue_ball_texture.get_rect()
            # blue_ball_rect.center = self.game.screen.get_width() / 2 - 50, 475
            # self.game.screen.blit(blue_ball_texture, blue_ball_rect)
            # red_ball_texture = gl_functions.load_image('ball\small_balls', "red_ball")[0]
            # red_ball_texture = pygame.transform.scale(red_ball_texture, (red_ball_texture.get_width() * 3, red_ball_texture.get_height() * 3))
            # red_ball_rect = red_ball_texture.get_rect()
            # red_ball_rect.center = self.game.screen.get_width() / 2 + 50, 475
            # self.game.screen.blit(red_ball_texture, red_ball_rect)

            if self.ball == "ball_1":
                pygame.draw.rect(self.game.screen, (255, 255, 255), black_texure_rect, 1)
            if self.ball == "ball_2":
                pygame.draw.rect(self.game.screen, (255, 255, 255), white_texture_rect, 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if slider.on_slider(event.pos[0], event.pos[1]):
                        slider.handle_event(self.game.screen, event.pos[0], 4, 9)
                        self.max_ball_speed = slider.volume
                    # Check if the back arrow was clicked
                    if black_texure_rect.collidepoint(event.pos):
                        self.ball = "ball_1"
                    if white_texture_rect.collidepoint(event.pos):
                        self.ball = "ball_2"
                    if back_arrow_rect.collidepoint(event.pos):
                        return

            pygame.display.flip()

    def change_player_settings(self):

        slider_acceleration = ui.Slider((self.game.screen.get_width() / 2) - 100, 270, 200, 10)
        slider_brake = ui.Slider((self.game.screen.get_width() / 2) - 100, 470, 200, 10)

        while True:
            self.game.screen.fill((0, 0, 0))

            back_arrow_surface = self.game.font.render("<", True, (255, 255, 255))
            back_arrow_rect = back_arrow_surface.get_rect(topleft=(20, 20))
            self.game.screen.blit(back_arrow_surface, back_arrow_rect)

            text_surface = self.game.font.render("Change player's acceleration: {}".format(self.player_acceleration),
                                                 True,
                                                 (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.game.screen.get_width() / 2, 200))
            self.game.screen.blit(text_surface, text_rect)

            slider_acceleration.draw(self.game.screen)

            text_surface = self.game.font.render("Change player's brake: {}".format(self.player_brake), True,
                                                 (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.game.screen.get_width() / 2, 400))
            self.game.screen.blit(text_surface, text_rect)

            slider_brake.draw(self.game.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if slider_acceleration.on_slider(event.pos[0], event.pos[1]):
                        slider_acceleration.handle_event(self.game.screen, event.pos[0], 10, 100)
                        self.player_acceleration = float(slider_acceleration.volume / 100)
                    if slider_brake.on_slider(event.pos[0], event.pos[1]):
                        slider_brake.handle_event(self.game.screen, event.pos[0], 10, 100)
                        self.player_brake = float(slider_brake.volume / 100)
                    if back_arrow_rect.collidepoint(event.pos):
                        return

            pygame.display.flip()

    def change_sound(self):
        def open_dialog():
            top = tkinter.Tk()
            top.withdraw()
            file_name = tkinter.filedialog.askopenfilename(parent=top)
            top.destroy()
            if file_name[-3::] == 'mp3':
                pygame.mixer.music.unload()
                pygame.mixer.music.load(file_name)
                pygame.mixer.music.play(10000)
            else:
                print("Can't open music file")

        button = Button(
            self.game.screen, self.game.screen.get_width() / 2 - 100, 250, 200, 50, text='Choose music',
            fontSize=18, margin=20,
            inactiveColour=(255, 225, 255),
            pressedColour=(0, 255, 0), radius=20,
            onClick=open_dialog
        )
        while True:
            self.game.screen.fill((0, 0, 0))

            back_arrow_surface = self.game.font.render("<", True, (255, 255, 255))
            back_arrow_rect = back_arrow_surface.get_rect(topleft=(20, 20))
            self.game.screen.blit(back_arrow_surface, back_arrow_rect)

            text_surface = self.game.font.render("Change music:", True,
                                                 (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.game.screen.get_width() / 2, 200))
            self.game.screen.blit(text_surface, text_rect)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.game.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_arrow_rect.collidepoint(event.pos):
                        return

            button.listen(events)
            button.draw()
            pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
            pygame.display.flip()
