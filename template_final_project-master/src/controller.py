
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
        

        # State variable
        self.running = True
        self.state = "menu"
        pygame.quit()
  ### below are some sample loop states ###


