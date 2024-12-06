import pygame
from src.player import Player
from src.world import World
from src.enemy import Enemy
from src.item import Item
from src.menu import Menu

class Controller:
    def __init__(self):
        """
        Intializations of game world.
        """
        self.screen = None
        self.clock = None
        self.running = True
        self.state = "menu"  # Initial state is menu
        self.item_counter = 0  # Track collected items
        self.enemy_collision_counter = 0  # Track enemy collisions
        self.items_collected_to_win = 3  # Number of items required to win
        self.enemy_collisions_to_lose = 3  # Number of enemy collisions required to lose

        # Create platforms (x,y,w,h)
        self.platform1 = World(725, 525, 250, 15)
        self.platform2 = World(0, 675, 300, 15)
        self.platform3 = World(250, 600, 300, 15)
        self.platform4 = World(0, 525, 200, 15)
        self.platform5 = World(0, 440, 50, 15)
        self.platform6 = World(0, 360, 50, 15)
        self.platform7 = World(250, 400, 150, 15)
        self.platform8 = World(400, 325, 100, 15)

        # Create ground and world bounds
        self.ground = World(0, 750, 1000, 800)
        self.world_bound_right = World(0, 0, 5, 800)
        self.world_bound_left = World(995, 0, 5, 800)

        # Create enemies/parkour
        self.enemies = pygame.sprite.Group()
        enemy1 = Enemy(700, 700)  # Bottom right enemy
        enemy2 = Enemy(850, 700)  # Bottom right enemy
        enemy3 = Enemy(450, 475)  # Middle enemy
        enemy4 = Enemy(700, 300)
        self.enemies.add(enemy1, enemy2, enemy3, enemy4)

        # Create collectible items
        self.items = pygame.sprite.Group()
        item1 = Item(350, 500)  # Example item positions
        item2 = Item(600, 300)
        item3 = Item(100, 650)
        self.items.add(item1, item2, item3)

        # Create sprite group for worlds (platforms)
        self.worlds = pygame.sprite.Group()
        self.worlds.add(
            self.platform1, self.platform2, self.ground,
            self.world_bound_right, self.world_bound_left,
            self.platform3, self.platform4, self.platform5,
            self.platform6, self.platform7, self.platform8
        )

    def display_text(self, text, size, color):
        """
        
        Utility to display text at the center of the screen
        Uses the text that is to be displayed, the size and the color
        
        
        """
        font = pygame.font.Font(None, size)
        render = font.render(text, True, color)
        text_rect = render.get_rect(center=(500,400 ))
        self.screen.blit(render, text_rect)

    def menu_loop(self):
        """
        Menu screen loop

        """
        while self.state == "menu":
            self.screen.fill((0, 0, 0))  # Black background
            
            self.display_text("Welcome to my simple game! Press any key to start. Your goal is to avoid the red squares, and collect the green circles!", 20, (255, 255, 255))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.state = None
                if event.type == pygame.KEYDOWN:
                    self.state = "game"  # Switch to game state

    def end_loop(self, result):
        """
        Simple end-game screen loop showing win or lose result
        Result is whether the player wins or loses
        """
        while self.state == "end":
            self.screen.fill((0, 0, 0))  # Black background
            if result == "win":
                self.display_text("You Win!", 50, (0, 255, 0))  # Green for win
            elif result == "lose":
                self.display_text("Game Over", 50, (255, 0, 0))  # Red for lose

           

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.state = None
                
    def mainloop(self):
        """Main loop for handling different states."""
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()

        # Create player instance
        self.player = Player(0, 750)  # Starting position

        # Create menu instance
        self.menu = Menu(self.screen)

        # Create sprite group for easy update and draw
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(
            self.player, self.enemies, self.items,
            self.platform1, self.platform2, self.ground,
            self.world_bound_right, self.world_bound_left,
            self.platform3, self.platform4, self.platform5,
            self.platform6, self.platform7, self.platform8
        )

        while self.running:
            if self.state == "menu":
                self.menu_loop()
            elif self.state == "game":
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.state = None

                keys = pygame.key.get_pressed()

                # Update player and platforms
                self.player.update(keys, self.worlds)
                self.worlds.update()
                self.enemies.update()
                self.items.update()

                # Item collisions
                collected_count = Item.handle_collisions(self.player, self.items)
                self.item_counter += collected_count

                # Handle enemy collisions
                if pygame.sprite.spritecollideany(self.player, self.enemies):
                    self.enemy_collision_counter += 1
                    self.player.rect.topleft = (50, 600)  # Reset player position

                # Check win/lose conditions
                if self.item_counter >= self.items_collected_to_win:
                    self.state = "end"  # Win condition
                    self.end_loop("win")
                elif self.enemy_collision_counter >= self.enemy_collisions_to_lose:
                    self.state = "end"  # Lose condition
                    self.end_loop("lose")

                # Clear screen
                self.screen.fill((135, 206, 250))

                # Draw all sprites and menu
                self.all_sprites.draw(self.screen)
                self.menu.draw(self.item_counter, self.enemy_collision_counter)

                # Update display
                pygame.display.flip()

                # Control frame rate
                self.clock.tick(60)

        pygame.quit()
