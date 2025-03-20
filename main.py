import pygame
import sys
from sprites.bird import Bird
from sprites.pipe import Pipe
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100" # Just moves game window to laptop screen instead of monitor


# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (135, 206, 235)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

# Game loop
def main():
    running = True
    bird = Bird()
    pipes = [Pipe(800), Pipe(1100), Pipe(1400)]  # Create two pipes with different starting positions

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    bird.flap()

        # Update bird physics
        bird.update()

        # Update pipes
        for pipe in pipes:
            pipe.update()
            # Check for collisions
            if bird.check_collision(pipe):
                # Handle collision (game over, etc.)
                running = False


        # Clear the screen
        screen.fill(LIGHT_BLUE)

        # Draw the pipes first (so they appear behind the bird)
        for pipe in pipes:
            pipe.draw(screen)

        # Draw the bird last (so it appears on top)
        bird.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the game's frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main() 