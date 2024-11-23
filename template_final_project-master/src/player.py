
import pygame
class Cloud(pygame.sprite.Sprite):
  
  def __init__(self,name):
    #setup pygame data
    super().__init__()
    self.name
    self.size = "small"
    self.image = pygame.image.load(f"assets/{name}.png")
    self.rect = self.image.get_rect()
    self.rect.x = 0
    self.rect.y = 0
    is_jumping = None

  def jump(self)
    if is_jumping:
      pass
  def update(self):
    self.rect.x -= 2

   