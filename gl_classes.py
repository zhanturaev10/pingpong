import pygame
import os


class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, part_of_name):
        super().__init__()
        self.sprites = load_image(path, part_of_name)
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update_image(self, index):
        if index < len(self.sprites):
            self.image = self.sprites[index]


def load_image(folder_path, part_of_name):
    file_list = os.listdir(folder_path)
    filtered_list = list(filter(lambda x: x.startswith(part_of_name), file_list))
    sprites = [pygame.image.load(os.path.join(folder_path, file)) for file in filtered_list]
    return sprites
