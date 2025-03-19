import pygame

YELLOW = (255, 255, 0)
GRAVITY = 0.5  # Gravity constant
MAX_DOWN_VELOCITY = 12  # Maximum falling speed
MAX_UP_VELOCITY = 8  # Maximum rising speed
FLAP_COOLDOWN = 150  # Cooldown in milliseconds

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 40
        self.height = 30  # Made height smaller for oval shape
        self.velocity = 0  # Add vertical velocity
        self.flap_strength = 25  # Negative because up is negative y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.last_flap_time = 0  # Track when we last flapped

    def flap(self):
        # self.y += self.flap_strength
        current_time = pygame.time.get_ticks()
        if current_time - self.last_flap_time >= FLAP_COOLDOWN:
            self.velocity -= self.flap_strength
            self.last_flap_time = current_time
            print("flapping")
        
    def update(self):
        # Apply gravity to velocity
        self.velocity += GRAVITY
        
        # Limit falling speed
        if self.velocity > MAX_DOWN_VELOCITY:
            self.velocity = MAX_DOWN_VELOCITY
        if self.velocity < -MAX_UP_VELOCITY:
            self.velocity = -MAX_UP_VELOCITY

        print(self.velocity)
       #self.velocity = max(self.velocity, MAX_VELOCITY)
    
        # Update position based on velocity
        self.y += self.velocity
        #self.y += GRAVITY
        
        # Update rectangle position
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.ellipse(screen, YELLOW, self.rect)
