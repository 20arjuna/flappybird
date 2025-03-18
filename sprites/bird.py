import pygame

YELLOW = (255, 255, 0)
GRAVITY = 0.5  # Gravity constant
MAX_VELOCITY = 8  # Maximum falling speed

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 40
        self.height = 30  # Made height smaller for oval shape
        self.velocity = 0  # Add vertical velocity
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        # Apply gravity to velocity
        self.velocity += GRAVITY
        
        # Limit falling speed
        self.velocity = max(self.velocity, MAX_VELOCITY)
    
        # Update position based on velocity
        self.y += self.velocity
        
        # Update rectangle position
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.ellipse(screen, YELLOW, self.rect)
