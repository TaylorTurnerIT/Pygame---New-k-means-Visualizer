# Import the Pygame library
import pygame
import debug
from dataHandler import DataHandler
# from visualStep import
# from processStep import

# Initialize Pygame
pygame.init()
display = pygame.display.Info()

# Set the dimensions of the game window
screenSize = 0.75 # Amount of screen to fill with game
screen = pygame.display.set_mode((display.current_w*screenSize, display.current_h*screenSize))

# Set the title of the window
pygame.display.set_caption("k-Means Visualizer")

# Game loop control variable
running = True

# Initialize Handlers
data = DataHandler("data.csv")

# Main game loop
while running:
    # Event handling loop
    for event in pygame.event.get():
        # Check for QUIT event to exit the game
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill("WHITE")

    # Update the display with everything drawn
    pygame.display.flip()

# Exit the game and close the window
pygame.quit()
