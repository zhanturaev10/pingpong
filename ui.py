import pygame as pg


class Slider:
    import pygame as pg

    class Slider:
        def __init__(self, x, y, w, h):
            self.circle_x = x
            self.volume = 0
            self.sliderRect = pg.Rect(x, y, w, h)
            self.dragging = False

        def draw(self, screen):
            pg.draw.rect(screen, (255, 255, 255), self.sliderRect)
            pg.draw.circle(screen, (255, 240, 255), (self.circle_x, (self.sliderRect.h // 2 + self.sliderRect.y)),
                           self.sliderRect.h * 3 // 2)

        def on_slider(self, x, y):
            return self.sliderRect.collidepoint(x, y)

        def on_slider_hold(self, x, y):
            return ((x - self.circle_x) ** 2 + (y - (self.sliderRect.y + self.sliderRect.h // 2)) ** 2) <= (
                        self.sliderRect.h * 3 // 2) ** 2

        def handle_event(self, screen, x, min_val, max_val):
            if self.dragging:
                self.circle_x = x
                self.update_volume(x, min_val, max_val)
                self.draw(screen)

        def update_volume(self, x, min_val, max_val):
            self.volume = min_val + int((x - self.sliderRect.x) / float(self.sliderRect.w) * (max_val - min_val))

        def start_dragging(self):
            self.dragging = True

        def stop_dragging(self):
            self.dragging = False
