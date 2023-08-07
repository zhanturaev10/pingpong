import pygame
import os

def load_image(folder_path, part_of_name):
    file_list = os.listdir(folder_path)
    filtered_list = list(filter(lambda x: x.startswith(part_of_name), file_list))
    sprites = [pygame.image.load(os.path.join(folder_path, file)).convert_alpha() for file in filtered_list]
    return sprites

def load_music(file_path):
    if file_path[-3:] == 'mp3':
        pygame.mixer.music.unload()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(10000)
    else:
        print("Can't open music file")
