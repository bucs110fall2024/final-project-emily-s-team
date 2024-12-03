
import pygame
class Player(pygame.sprite.Sprite):
  
  def __init__(self,x,y):
    #setup pygame data
    super().__init__()
    # Load the image for the player
    self.rect1 = pygame.Rect(50, 50, 100, 100)
    
        
        # Get the rectangle of the image for positioning
   
        
        # Set the initial position of the player
    self.rect1.topleft = (x, y)

        # Movement attributes
    self.speed = 5

  def move(self, keys):
    if keys[pygame.K_UP]:
        self.rect1.y -= self.speed
    if keys[pygame.K_DOWN]:
        self.rect1.y += self.speed
    if keys[pygame.K_LEFT]:
        self.rect1.x -= self.speed
    if keys[pygame.K_RIGHT]:
        self.rect1.x += self.speed

    def update(self, keys):
       
        self.move(keys)
  

   