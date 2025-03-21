import pygame
import random

GREEN = (0, 255, 0)
LIGHT_BLUE = (135, 206, 235)
PIPE_WIDTH = 80
PIPE_HEIGHT = 600
GAP_HEIGHT = 150  # Height of the gap

class Pipe:
    def __init__(self, x):
        self.x = x
        self.speed = 4
        
        # Create surfaces for pipe and gap
        self.pipe_surface = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.pipe_surface.fill(GREEN)
        self.gap_surface = pygame.Surface((PIPE_WIDTH, GAP_HEIGHT))
        self.gap_surface.fill(LIGHT_BLUE)
        
        # Create masks for collision detection
        self.pipe_mask = pygame.mask.from_surface(self.pipe_surface)
        self.gap_mask = pygame.mask.from_surface(self.gap_surface)
        
        # Randomly position the gap
        self.gap_y = random.randint(100, 400)
        
        # Create rectangles for pipe and gap
        self.pipe_rect = pygame.Rect(x, 0, PIPE_WIDTH, PIPE_HEIGHT)
        self.gap_rect = pygame.Rect(x, self.gap_y, PIPE_WIDTH, GAP_HEIGHT)
    
    def update(self):
        # Move pipe and gap left
        self.x -= self.speed
        self.pipe_rect.x = self.x
        self.gap_rect.x = self.x
        
        # Reset pipe when it moves off screen
        if self.x < -PIPE_WIDTH:
            self.reset()
    
    def reset(self):
        self.x = 800  # Move to right side of screen
        self.gap_y = random.randint(100, 400)  # New random gap position
        self.pipe_rect.x = self.x
        self.gap_rect.x = self.x
        self.gap_rect.y = self.gap_y
    
    def draw(self, screen):
        # Draw the green pipe
        pygame.draw.rect(screen, GREEN, self.pipe_rect)
        # Draw the blue gap on top
        pygame.draw.rect(screen, LIGHT_BLUE, self.gap_rect) 