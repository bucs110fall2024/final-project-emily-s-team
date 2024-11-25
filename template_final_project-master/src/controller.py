
import pygame
from src import player
class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
  def mainloop(self):
        self.screen = pygame.display.set_mode((800, 600))


        # Clock for controlling frame rate
        self.clock = pygame.time.Clock()

        # Initialize player and sprite groups
        self.player = Player(100, 100, "Player.png")
        self.all_sprites = pygame.sprite.Group(self.player)

        # State variable
        self.running = True
        self.state = "menu"
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
