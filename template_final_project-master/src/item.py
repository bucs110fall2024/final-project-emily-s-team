import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, width=20, height=20, color=(0, 255, 0)):
        super().__init__()
        # Create a visual representation of the item (a green square by default)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # Position the item
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def handle_collisions(player, items_group):
        collected_items = pygame.sprite.spritecollide(player, items_group, True)  # Remove collided items
        return len(collected_items)  # Return the count of collected items