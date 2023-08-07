import pygame
import sys
from gl_classes import Block


class MapEditor:
    def __init__(self, game):
        self.game = game
        self.grid_size = 50
        self.tools = ["add", "delete"]
        self.current_tool = "add"

    def draw_interface(self):
        world = []
        world_width, world_height = pygame.display.get_window_size()[0] // self.grid_size, \
                                    pygame.display.get_window_size()[1] // self.grid_size
        for row in range(world_height):
            line = []
            for col in range(world_width):
                line.append(0)
            world.append(line)

        while True:
            self.game.screen.fill((0, 0, 0))

            back_arrow_surface = self.game.font.render("<", True, (255, 255, 255))
            back_arrow_rect = back_arrow_surface.get_rect(topleft=(20, 20))
            self.game.screen.blit(back_arrow_surface, back_arrow_rect)

            add_button_texture = pygame.image.load('icons/drawing.png').convert_alpha()
            add_button_texture = pygame.transform.scale(add_button_texture, (32, 32))
            add_button_rect = add_button_texture.get_rect()
            add_button_rect.center = self.game.screen.get_width() / 2 - 92, 40
            self.game.screen.blit(add_button_texture, add_button_rect)

            delete_button_texture = pygame.image.load('icons/delete.png').convert_alpha()
            delete_button_texture = pygame.transform.scale(delete_button_texture, (32, 32))
            delete_button_rect = delete_button_texture.get_rect()
            delete_button_rect.center = self.game.screen.get_width() / 2 - 46, 40
            self.game.screen.blit(delete_button_texture, delete_button_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_arrow_rect.collidepoint(event.pos):
                        return
                    elif add_button_rect.collidepoint(event.pos):
                        self.current_tool = "add"
                    elif delete_button_rect.collidepoint(event.pos):
                        self.current_tool = "delete"
                    elif event.button == 4:  # Mouse wheel up
                        self.cycle_block(-1)
                    elif event.button == 5:  # Mouse wheel down
                        self.cycle_block(1)

                elif event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pressed()[0]:  # Left mouse button pressed
                        if self.current_tool == "add":
                            mouse_px, mouse_py = pygame.mouse.get_pos()
                            mouse_row, mouse_col = mouse_py // self.grid_size, mouse_px // self.grid_size
                            if 0 <= mouse_row < world_height and 0 <= mouse_col < world_width:
                                world[mouse_row][mouse_col] = self.game.settings.block
                        elif self.current_tool == "delete":
                            mouse_px, mouse_py = pygame.mouse.get_pos()
                            mouse_row, mouse_col = mouse_py // self.grid_size, mouse_px // self.grid_size
                            if 0 <= mouse_row < world_height and 0 <= mouse_col < world_width:
                                world[mouse_row][mouse_col] = 0

            # Draw the world
            for row in range(world_height):
                for col in range(world_width):
                    if world[row][col] != 0:
                        x_pos, y_pos = col * self.grid_size, row * self.grid_size
                        self.game.screen.blit(self.game.settings.block_sprites[world[row][col]], (x_pos, y_pos))

            pygame.display.flip()

    def cycle_block(self, direction):
        current_block = self.game.settings.block
        max_block = len(self.game.settings.block_sprites) - 1
        new_block = current_block + direction
        if new_block > max_block:
            new_block = 1
        elif new_block < 1:
            new_block = max_block
        self.game.settings.block = new_block


    def add(self):
        pass

    def delete(self):
        pass
