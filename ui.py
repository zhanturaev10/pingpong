import pygame as pg


class Slider:
    def __init__(self, x, y, w, h):
        self.circle_x = x
        self.volume = 0
        self.sliderRect = pg.Rect(x, y, w, h)

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), self.sliderRect)
        pg.draw.circle(screen, (255, 240, 255), (self.circle_x, (self.sliderRect.h / 2 + self.sliderRect.y)), self.sliderRect.h * 1.5)

    def on_slider(self, x, y):
        if self.on_slider_hold(x, y) or self.sliderRect.x <= x <= self.sliderRect.x + self.sliderRect.w and self.sliderRect.y <= y <= self.sliderRect.y + self.sliderRect.h:
            return True
        else:
            return False

    def on_slider_hold(self, x, y):
        if ((x - self.circle_x) * (x - self.circle_x) + (y - (self.sliderRect.y + self.sliderRect.h / 2)) * (y - (self.sliderRect.y + self.sliderRect.h / 2)))\
               <= (self.sliderRect.h * 1.5) * (self.sliderRect.h * 1.5):
            return True
        else:
            return False

    def handle_event(self, screen, x, min, max):
        if x < self.sliderRect.x:
            self.circle_x = self.sliderRect.x
        elif x > self.sliderRect.x + self.sliderRect.w:
            self.circle_x = self.sliderRect.x + self.sliderRect.w
        else:
            self.circle_x = x
        self.update_volume(x, min, max)
        self.draw(screen)

    def update_volume(self, x, min, max):
        if x < self.sliderRect.x:
            self.volume = min
        elif x > self.sliderRect.x + self.sliderRect.w:
            self.volume = max
        else:
            self.volume = int((x - self.sliderRect.x) / float(self.sliderRect.w) * max) + 1
