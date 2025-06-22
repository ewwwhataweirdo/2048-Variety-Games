import pygame
class tile():
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def draw(self, surface):
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.value), True, (0, 0, 0))
        rect = text.get_rect(center=(self.x + 50, self.y + 50))
        surface.blit(text, rect)

    def update(self):
        pass  # Placeholder for future updates if needed