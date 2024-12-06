
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

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
