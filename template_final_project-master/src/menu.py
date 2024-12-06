import pygame

class Menu:
    def __init__(self, screen):
        """Initialize the menu with a reference to the screen."""
        self.screen = screen
        self.font = pygame.font.Font(None, 36)  # Default font with size 36

    def draw(self, item_counter, enemy_collision_counter):
        """Draw the menu displaying item count and enemy collision count."""
        # Render texts
        item_text = self.font.render(f"Items Collected: {item_counter}", True, (255, 255, 255))
        enemy_text = self.font.render(f"Enemy Collisions: {enemy_collision_counter}", True, (255, 255, 255))
        
        # Draw texts on the screen
        self.screen.blit(item_text, (10, 10))  # Top-left corner
        self.screen.blit(enemy_text, (10, 50))  # Below item text
