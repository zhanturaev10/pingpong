import pygame
import os


def load_image(folder_path, part_of_name):
    file_list = os.listdir(folder_path)
    filtered_list = list(filter(lambda x: x.startswith(part_of_name), file_list))
    sprites = [pygame.image.load(os.path.join(folder_path, file)) for file in filtered_list]
    return sprites


print(load_image('ball\small_balls', 'blue_ball'))
