import pygame
import sys


class MapEditor:
    def __init__(self, game):
        self.game = game
        self.grid_size = 50
        self.grid_width = int(self.game.screen.get_width() * 0.8 / self.grid_size)
        self.grid_height = int(self.grid_width * 9 / 16)
        self.grid_start_x = int(self.game.screen.get_width() * 0.1)
        self.grid_start_y = int((self.game.screen.get_height() - self.grid_height * self.grid_size) / 2)
        self.drawing_mode = False

    def add_image(self, row, col):
        image = pygame.image.load('wallpack\wall_1_1.png').convert_alpha()
        cell_size = self.grid_size
        cell_center_x = col * cell_size + cell_size // 2 + self.grid_start_x
        cell_center_y = row * cell_size + cell_size // 2 + self.grid_start_y
        image_rect = image.get_rect(center=(cell_center_x, cell_center_y))
        self.game.screen.blit(image, image_rect)

    def draw_interface(self):
        drawing_icon = pygame.image.load('icons/drawing.png').convert_alpha()
        drawing_actve_icon = pygame.image.load('icons/drawing1.png').convert_alpha()

        world = []
        for row in range(self.grid_height):
            line = []
            for col in range(self.grid_width):
                line.append(0)
            world.append(line)

        while True:
            self.game.screen.fill((30, 30, 30))

            back_arrow_surface = self.game.font.render("<", True, (255, 255, 255))
            back_arrow_rect = back_arrow_surface.get_rect(topleft=(20, 20))
            self.game.screen.blit(back_arrow_surface, back_arrow_rect)

            add_button_texture = drawing_actve_icon if self.drawing_mode else drawing_icon
            add_button_texture = pygame.transform.scale(add_button_texture, (32, 32))
            add_button_rect = add_button_texture.get_rect()
            add_button_rect.center = self.game.screen.get_width() / 2 - 92, 40
            self.game.screen.blit(add_button_texture, add_button_rect)
            pygame.draw.rect(self.game.screen, (255, 255, 255),
                             pygame.Rect(self.grid_start_x - 2, self.grid_start_y - 2,
                                         self.grid_width * self.grid_size + 4, self.grid_height * self.grid_size + 4),
                             2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if add_button_rect.collidepoint(event.pos):
                        # start adding images on click
                        while True:
                            for event in pygame.event.get():
                                add_button_texture = drawing_actve_icon if self.drawing_mode else drawing_icon
                                add_button_texture = pygame.transform.scale(add_button_texture, (32, 32))
                                self.game.screen.blit(add_button_texture, add_button_rect)

                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if add_button_rect.collidepoint(event.pos):
                                        self.drawing_mode = not self.drawing_mode
                                    if self.drawing_mode:
                                        print(1)
                                        mouse_px, mouse_py = pygame.mouse.get_pos()
                                        if mouse_px < self.grid_start_x or mouse_px > self.grid_start_x + self.grid_width * self.grid_size:
                                            continue
                                        mouse_row, mouse_col = (mouse_py - self.grid_start_y) // self.grid_size, (
                                                mouse_px - self.grid_start_x) // self.grid_size
                                        if mouse_row < 0 or mouse_row >= self.grid_height or mouse_col < 0 or mouse_col >= self.grid_width:
                                            continue
                                        self.add_image(mouse_row, mouse_col)
                                elif event.type == pygame.QUIT:
                                    self.game.running = False
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        # stop adding images on escape
                                        self.drawing_mode = False
                                        break
                            pygame.display.flip()
            pygame.display.flip()

# class MapEditor:
#     def __init__(self, game):
#         self.game = game
#         self.grid_size = 50
#         self.drawing_mode = False
#         self.icon_texture = 'icons/drawing.png'

#     def add_image(self, row, col):
#         if self.drawing_mode:
#             image = pygame.image.load('2.png').convert_alpha()
#         else:
#             image = pygame.image.load('1.png').convert_alpha()

#         cell_size = self.grid_size
#         cell_center_x = col * cell_size + cell_size // 2
#         cell_center_y = row * cell_size + cell_size // 2
#         image_rect = image.get_rect(center=(cell_center_x, cell_center_y))
#         self.game.screen.blit(image, image_rect)

#     def draw_interface(self):

#         world = []
#         world_width, world_height = pygame.display.get_window_size()[0] // self.grid_size, \
#                                     pygame.display.get_window_size()[1] // self.grid_size

#         field_width = world_width // 10 * 9
#         field_height = field_width // 16 * 9

#         x_offset = (world_width - field_width) // 2
#         y_offset = (world_height - field_height) // 2

#         for row in range(world_height):
#             line = []
#             for col in range(world_width):
#                 if col < x_offset or col >= x_offset + field_width or \
#                         row < y_offset or row >= y_offset + field_height:
#                     line.append(1)
#                 else:
#                     line.append(0)
#             world.append(line)

#         while True:
#             self.game.screen.fill((30, 30, 30))

# # Draw the game grid for row in range(world_height): for col in range(world_width): if world[row][col] == 0:
# pygame.draw.rect(self.game.screen, (255, 255, 255), (col * self.grid_size, row * self.grid_size, self.grid_size,
# self.grid_size), 1)

#             # Draw the interface elements
#             back_arrow_surface = self.game.font.render("<", True, (255, 255, 255))
#             back_arrow_rect = back_arrow_surface.get_rect(topleft=(20, 20))
#             self.game.screen.blit(back_arrow_surface, back_arrow_rect)

#             add_button_texture = pygame.image.load(self.icon_texture).convert()
#             add_button_texture = pygame.transform.scale(add_button_texture, (32, 32))
#             add_button_rect = add_button_texture.get_rect()
#             add_button_rect.center = self.game.screen.get_width() / 2 - 92, 40
#             self.game.screen.blit(add_button_texture, add_button_rect)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.game.running = False
#                     pygame.quit()
#                     sys.exit()
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     if add_button_rect.collidepoint(event.pos):
#                         # start adding images on click
#                         drawing_mode = True
#                         current_image = "drawing.png"
#                         while drawing_mode:
#                             for event in pygame.event.get():
#                                 if event.type == pygame.MOUSEBUTTONDOWN:
#                                     mouse_px, mouse_py = pygame.mouse.get_pos()
#                                     mouse_row, mouse_col = mouse_py // self.grid_size, mouse_px // self.grid_size
#                                     if self.grid[mouse_row][mouse_col] == 0 and \
#                                             self.field_rect.collidepoint((mouse_px, mouse_py)):
#                                         self.add_image(mouse_row, mouse_col, current_image)
#                                         self.grid[mouse_row][mouse_col] = 1
#                                 elif event.type == pygame.QUIT:
#                                     self.game.running = False
#                                     pygame.quit()
#                                     sys.exit()
#                                 elif event.type == pygame.KEYDOWN:
#                                     if event.key == pygame.K_ESCAPE:
#                                         # stop adding images on escape
#                                         drawing_mode = False
#                                     elif event.key == pygame.K_b:
#                                         # switch to bebra.png
#                                         current_image = "bebra.png"
#                             pygame.display.flip()
#                         add_button_texture = pygame.image.load('icons/drawing.png').convert()
#                         add_button_texture = pygame.transform.scale(add_button_texture, (32, 32))
#                     elif self.field_rect.collidepoint(event.pos):
#                         # stop drawing mode on click outside the field
#                         drawing_mode = False
#                         add_button_texture = pygame.image.load('icons/drawing.png').convert()
#                         add_button_texture = pygame.transform.scale(add_button_texture, (32, 32))
#                 pygame.display.flip()
#             pygame.display.flip()
