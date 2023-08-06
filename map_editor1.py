import pygame
import sys
from gl_classes import Block


# class Brick(Block):
#     def __init__(self,path,x_pos,y_pos,part_of_name,type_of_brick):
#         super().__init__(path,x_pos,y_pos,part_of_name)


class MapEditor:
    def __init__(self, game):
        self.game = game
        self.grid_size = 50

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

            add_button_texture = pygame.image.load('icons/drawing.png').convert()
            add_button_texture = pygame.transform.scale(add_button_texture, (32, 32))
            add_button_rect = add_button_texture.get_rect()
            add_button_rect.center = self.game.screen.get_width() / 2 - 92, 40
            self.game.screen.blit(add_button_texture, add_button_rect)

            # delete_button_texture = pygame.image.load('icons/drawing.png').convert()
            # delete_button_texture = pygame.transform.scale(delete_button_texture, (32, 32))
            # delete_button_rect = delete_button_texture.get_rect()
            # delete_button_rect.center = self.game.screen.get_width() / 2 - 46, 40
            # self.game.screen.blit(delete_button_texture, delete_button_rect)

            # edit_button_texture = pygame.image.load('icons/drawing.png').convert()
            # edit_button_texture = pygame.transform.scale(edit_button_texture, (32, 32))
            # edit_button_rect = edit_button_texture.get_rect()
            # edit_button_rect.center = self.game.screen.get_width() / 2, 40
            # self.game.screen.blit(edit_button_texture, edit_button_rect)

            # save_button_texture = pygame.image.load('icons/drawing.png').convert()
            # save_button_texture = pygame.transform.scale(save_button_texture, (32, 32))
            # save_button_rect = save_button_texture.get_rect()
            # save_button_rect.center = self.game.screen.get_width() / 2 + 46, 40
            # self.game.screen.blit(save_button_texture, save_button_rect)

            # open_button_texture = pygame.image.load('icons/drawing.png').convert()
            # open_button_texture = pygame.transform.scale(open_button_texture, (32, 32))
            # open_button_rect = open_button_texture.get_rect()
            # open_button_rect.center = self.game.screen.get_width() / 2 + 92, 40
            # self.game.screen.blit(open_button_texture, open_button_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if add_button_rect.collidepoint(event.pos):
                        self.add()
                    # if delete_button_rect.collidepoint(event.pos):
                    #     self.delete()
                    # if edit_button_rect.collidepoint(event.pos):
                    #     print("Edit time")
                    # if save_button_rect.collidepoint(event.pos):
                    #     # self.save_map(world, world_width, world_height)
                    #     pass
                    # if open_button_rect.collidepoint(event.pos):
                    #     pass
                    #     #print("Open map")
                    #     #world = self.open_map()
                    if back_arrow_rect.collidepoint(event.pos):
                        return
                # elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                #     print("Save map")
                #     self.save_map(world, world_width, world_height)
                # elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                #     print("Open map")
                #     world = self.open_map(world_width)

            mouse_px, mouse_py = pygame.mouse.get_pos()
            b1, b2, b3 = pygame.mouse.get_pressed()

            mouse_row, mouse_col = mouse_py // self.grid_size, mouse_px // self.grid_size

            # if b1:
            #     world[mouse_row][mouse_col] = 1
            # elif b3:
            #     world[mouse_row][mouse_col] = 0

            # for row in range(world_height): for col in range(world_width): x, y = col * self.grid_size,
            # row * self.grid_size if world[row][col] == 1: pygame.draw.rect(self.game.screen, pygame.Color('gray'),
            # (x, y, self.grid_size, self.grid_size)) else: pygame.draw.rect(self.game.screen, pygame.Color('gray'),
            # (x, y, self.grid_size, self.grid_size), 1)

            # pygame.display.flip()

    def add(self):
        pass

    def delete(self):
        pass

    # def save_map(self, world, width, height):
    #     file = open('map.txt', 'w')
    #     for row in range(height):
    #         for col in range(width):
    #             file.write(str(world[row][col]))

    #     file.close()

    # def open_map(self, width):
    #     world = []
    #     try:
    #         file = open('map.txt', 'r')
    #         row, col = 0, 0
    #         for line in file:
    #             for s in line:
    #                 world[row][col] = int(s)
    #                 col += 1
    #                 if col >= width-1:
    #                     row += 1
    #                     col = 0
    #         file.close()
    #     except:
    #         print('File map not found')
    #     return world
