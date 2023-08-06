import pygame
import sys
import playervsplayer
from block import Player
from ball import Ball
import gl_classes
import map_editor


class MainLoop:
    def __init__(self):
        pygame.init()
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.accent_color = (27, 35, 43)
        self.font = pygame.font.SysFont('comicsansms', 32)
        self.menu_items = [
            {"text": "Player vs. Player", "action": self.game_vs_player},
            {"text": "Player vs. Bot", "action": self.game_vs_bot},
            {"text": "Settings", "action": self.settings},
            {"text": "Map editor", "action": self.map_editor},
            {"text": "Enable Neural Network Training", "action": self.enable_nn_training},
        ]
        self.menu_item_height = 50
        self.menu_item_spacing = 20
        self.running = True
        self.current_screen = "menu"
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        pygame.mixer.music.load('15_Kamski.mp3')
        pygame.mixer.music.play(10000)
        self.exit_button_rect = pygame.Rect((self.screen.get_width() / 2 - 100, 700, 200, 50))
        self.exit_button_text = "Exit"

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.current_screen == "menu":
                        self.handle_menu_click(event.pos)
                    elif self.current_screen == "nn_training":
                        self.handle_nn_training_click(event.pos)

            self.screen.fill((0, 0, 0))
            if self.current_screen == "menu":
                self.draw_menu()
            elif self.current_screen == "nn_training":
                self.draw_nn_training()

            pygame.display.flip()
            self.clock.tick(60)

    @staticmethod
    def exit_game():
        pygame.quit()
        sys.exit()

    def handle_menu_click(self, pos):
        for item in self.menu_items:
            text_surface = self.font.render(item["text"], True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.screen.get_width() / 2, 100 + self.menu_items.index(item) * 100))
            if text_rect.collidepoint(pos):
                item["action"]()
            if self.exit_button_rect.collidepoint(pos):
                self.exit_game()

    def draw_menu(self):
        total_menu_items_height = len(self.menu_items) * (self.menu_item_height + self.menu_item_spacing)
        y_offset = (self.screen.get_height() - total_menu_items_height) // 2

        for i, item in enumerate(self.menu_items):
            text_surface = self.font.render(item["text"], True, (255, 255, 255))
            text_rect = text_surface.get_rect(
                center=(self.screen.get_width() / 2, y_offset + i * (self.menu_item_height + self.menu_item_spacing)))
            self.screen.blit(text_surface, text_rect)

        # Draw Exit Button
        exit_button_surface = self.font.render(self.exit_button_text, True, (255, 255, 255))
        exit_button_rect = exit_button_surface.get_rect(center=(self.screen.get_width() / 2,
                                                                y_offset + len(self.menu_items) * (
                                                                            self.menu_item_height + self.menu_item_spacing)))
        pygame.draw.rect(self.screen, (200, 0, 0), exit_button_rect)
        self.screen.blit(exit_button_surface, exit_button_rect)

    def game_vs_player(self):
        # ... Implement the Player vs. Player game mode here ...
        pass

    def game_vs_bot(self):
        # ... Implement the Player vs. Bot game mode here ...
        pass

    def settings(self):
        # ... Implement the settings screen here ...
        pass

    def enable_nn_training(self):
        print("Opening neural network training")
        self.current_screen = "nn_training"

    def handle_nn_training_click(self, pos):
        arrow_surface = self.font.render("<", True, (255, 255, 255))
        arrow_rect = arrow_surface.get_rect(topleft=(20, 20))
        if arrow_rect.collidepoint(pos):
            self.current_screen = "menu"

    def draw_nn_training(self):
        self.screen.fill((0, 0, 0))
        arrow_surface = self.font.render("<", True, (255, 255, 255))
        arrow_rect = arrow_surface.get_rect(topleft=(20, 20))
        self.screen.blit(arrow_surface, arrow_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 200, 400, 200))

    def map_editor(self):
        # ... Implement the map editor here ...
        pass


if __name__ == '__main__':
    game = MainLoop()
    game.main_loop()
