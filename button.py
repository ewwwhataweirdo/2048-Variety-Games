import pygame
class Button():
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height, border_radius=10)
        self.text = text
        self.font = pygame.font.SysFont("arialblack", 50)
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)