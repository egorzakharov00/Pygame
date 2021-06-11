# The code provided by HyperionDev from task15/game/example.py was used and edited in the making of this python program
# All images used in the program were sourced from the web
# player.jpeg - https://lh3.googleusercontent.com/proxy/B2Q62py2IHaahD2dQETeHkP6d_jTZmwqvcQ6xykHrFYIOuroo1jK9mpLXt-VfQxY0NC_rza4BDMeDaaT_me5atZkb-UPSVfrgy9buRM
# enemy1.jpeg - http://www.tah.co.za/blog/wp-content/uploads/2019/09/snake-without-dog.jpg
# enemy2.jpg - https://dsx.weather.com/util/image/w/en-ca-lizardfossil.jpg?v=at&w=200&h=200&api=7db9fe61-7414-47b5-9871-e17d87b8b6a0
# enemy3.jpg - https://i.pinimg.com/236x/68/7e/c6/687ec650419101036f2d3f9541440c94--birdwatching-animal-pictures.jpg
# prize.jpg - https://saveourbones.com/storage/bananas.jpg

import pygame  # Imports a game library that lets you use specific functions in your program.
import random  # Import to generate random numbers.

# Initialize the pygame modules to get everything started.

pygame.init()

# The screen that will be created needs a width and a height.

screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width,
                                  screen_height))  # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy and prize images).

player = pygame.image.load("player.jpeg")
enemy1 = pygame.image.load("enemy1.jpeg")
enemy2 = pygame.image.load("enemy2.jpeg")
enemy3 = pygame.image.load("enemy3.jpeg")
prize = pygame.image.load("prize.jpeg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later.

playerXPosition = 100
playerYPosition = 50

# Make the enemies and prize start off screen and at a random y position.

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1_height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)

enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up, down, left or right key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False.
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to
# represent real time game play.

while 1:  # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later.

    screen.fill(0)  # Clears the screen.
    screen.blit(player, (playerXPosition,
                         playerYPosition))  # This draws the player image to the screen at the position specified. I.e. (100, 50).
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.

    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.

        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.

            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        # This event checks if the key is up(i.e. not pressed by the user).

        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if keyUp:
        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown:
        if playerYPosition < screen_height - image_height:  # This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft:
        if playerXPosition > 0:  # This makes sure that the user does not move the player left of the window
            playerXPosition -= 1
    if keyRight:
        if playerXPosition < screen_width - image_width:  # This makes sure that the user does not move the player right of the window
            playerXPosition += 1

    # Check for collision of the enemies with the player or with the prize and the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:

    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemies:

    enemyBox1 = pygame.Rect(enemy1.get_rect())
    enemyBox1.top = enemy1YPosition
    enemyBox1.left = enemy1XPosition

    enemyBox2 = pygame.Rect(enemy2.get_rect())
    enemyBox2.top = enemy2YPosition
    enemyBox2.left = enemy2XPosition

    enemyBox3 = pygame.Rect(enemy3.get_rect())
    enemyBox3.top = enemy3YPosition
    enemyBox3.left = enemy3XPosition

    # Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the boxes:

    if playerBox.colliderect(enemyBox1) or playerBox.colliderect(enemyBox2) or playerBox.colliderect(enemyBox3):

        # Display losing status to the user:

        print("You lose!")

        # Quit game and exit window:

        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):

        # Display winning status to the user:

        print("You win!")

        # Quit game and exit window

        pygame.quit()
        exit(0)

    # Make enemies and prize approach the player at set speeds.

    enemy1XPosition -= 1
    enemy2XPosition -= 0.75
    enemy3XPosition -= 0.5
    prizeXPosition -= 0.25

    # ================The game loop logic ends here. =============
