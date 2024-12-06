import pygame

class Menu:
    def __init__(self, screen):
       
        self.screen = screen
        self.font = pygame.font.Font(None, 36)  # Default font with size 36

    def draw(self, item_counter, enemy_collision_counter):
        """
       This creates the top of the screen during the game that contains information such as how many times you've touched an enemy, and how many items you've collected
       Item counter counts how many items have been collected
       Enemy collision counter counts how many times the player has touched an enemy
       """

        # Render texts
        item_text = self.font.render(f"Items Collected: {item_counter}", True, (255, 255, 255))
        enemy_text = self.font.render(f"Enemy Collisions: {enemy_collision_counter}", True, (255, 255, 255))
        
        # Draw texts on the screen
        self.screen.blit(item_text, (10, 10))  # Top-left corner
        self.screen.blit(enemy_text, (10, 50))  # Below item text
