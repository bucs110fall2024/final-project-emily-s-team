
import pygame
class Player(pygame.sprite.Sprite):
  
  def __init__(self,x,y,img_file):
    #setup pygame data
    super().__init__()
    # Load the image for the player
    self.image = pygame.image.load("assets/Player.png")
        
        # Get the rectangle of the image for positioning
    self.rect = self.image.get_rect()
        
        # Set the initial position of the player
    self.rect.topleft = (x, y)

        # Movement attributes
    self.speed = 5

  def move(self, keys):
    if keys[pygame.K_UP]:
        self.rect.y -= self.speed
    if keys[pygame.K_DOWN]:
        self.rect.y += self.speed
    if keys[pygame.K_LEFT]:
        self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]:
        self.rect.x += self.speed

    def update(self, keys):
       
        self.move(keys)
  

   