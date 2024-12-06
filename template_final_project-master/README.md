
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# A Simple Collection Game
## CS110 Final Project  Fall Semester, 2024

## Team Members



Emily Scott
***

## Project Description


I am going to be making a scroller, parkour game where the user can collect objects whilst avoiding enemies.
***    

## GUI Design


### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Moveable player
2. Collectable items
3. Damaging items
4. Menu
5. Lose and win screen

### Classes

-World class- Creates the aspects of the world, like the ground, platforms, and world boundaries.
-Enemy class- Creates the "enemies" or damaging squares that will cause you to lose life and potentially lose the game
-Item class- Creates the "items" that the player can collect in order to win the game
-Player class- in charge of creating the player that has gravity, jumping, and collisions, and movement
-Menu Class- creates the counters that count how many items the player has collected as well as how many times the player has collided with an enemy.

## ATP

Test Case 1: Player Movement
1. Start the Game
2. Press a key to get to game
3. Press arrow key right or left
4. Player moves in said direction
Expected Outcome: Player moves in left or right direction

Test Case 2: Player Colliding with platforms
1. Start the game
2. Press key to get to game
3. Player uses space bar to jump onto platform
Expected outcome: Player doesn't fall through platform and can move on it, but not through it.

Test Case 3: Start Screen
1. Start the game
2. Press a key
Expected outcome: The game starts and player can see platforms

Test Case 4: Player collecting objects
1. Start the game
2. Press a key
3. Player uses arrow keys and spacebar to touch a green circle
Expected outcome: Item disappears, and counter on top of screen increases
Test Case 5: Player touching enemies
1. Start game
2. Press a key
3. Player uses arrow keys and spacebar to touch a red square
Expected outcome: Player will reset position to the beginning, and the counter to see how many times youve collided with enemies increases.