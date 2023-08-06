import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, screen_width, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class Player(Block):
    def __init__(self, path, x_pos, y_pos, max_speed, screen_height, screen_width, acceleration, brake):
        super().__init__(path, x_pos, y_pos, screen_height, screen_width)
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.brake = brake
        self.velocity = 0

    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 1  # это дрыгание не видно, зато оно позволяет починить ошибку
            # print("self.velocity", self.velocity) 
            self.velocity = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height  # здесь это делать не приходиться
            self.velocity = 0

    def move(self, keys_pressed, player_num, **kw_gsp):
        if player_num == 1:
            up_key = pygame.K_UP
            down_key = pygame.K_DOWN
        else:
            up_key = pygame.K_w
            down_key = pygame.K_s

        if keys_pressed[up_key]:
            # Gradual acceleration
            self.velocity -= self.acceleration
            # Max speed limiter
            if self.velocity < -self.max_speed:
                self.velocity = -self.max_speed
        elif keys_pressed[down_key]:
            # Gradual acceleration
            self.velocity += self.acceleration
            # Max speed limiter
            if self.velocity > self.max_speed:
                self.velocity = self.max_speed
        else:
            # Braking
            if self.velocity > 0:
                self.velocity -= self.brake
                if self.velocity < 0:
                    self.velocity = 0
            elif self.velocity < 0:
                self.velocity += self.brake
                if self.velocity > 0:
                    self.velocity = 0

    def update(self):
        self.rect.y += self.velocity
        self.screen_constrain()
