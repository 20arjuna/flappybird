import pygame

YELLOW = (255, 255, 0)
GRAVITY = 0.5  # Gravity constant
MAX_DOWN_VELOCITY = 12  # Maximum falling speed
MAX_UP_VELOCITY = 8  # Maximum rising speed
FLAP_COOLDOWN = 100  # Cooldown in milliseconds

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 100

        self.image = pygame.image.load("assets/bird.png")
        self.image = pygame.transform.scale(self.image, (50, 37.5))

        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.velocity = 0  

        self.flap_strength = 35
        self.last_flap_time = 0  
        
        # self.angle = 0  
        # self.max_down_angle = 90
        # self.max_up_angle = -30

        self.mask = pygame.mask.from_surface(self.image)

    def flap(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_flap_time >= FLAP_COOLDOWN:
            self.velocity -= self.flap_strength
            self.last_flap_time = current_time
        
    def update(self):
        # Apply gravity to velocity
        self.velocity += GRAVITY
        
        # Limit falling / flapping speed
        if self.velocity > MAX_DOWN_VELOCITY:
            self.velocity = MAX_DOWN_VELOCITY
        if self.velocity < -MAX_UP_VELOCITY:
            self.velocity = -MAX_UP_VELOCITY

        # Update position based on velocity
        self.y += self.velocity
        self.rect.y = self.y

        # After rotating the image, update the mask
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_edge_points(self):
        # Get the mask's bounding box
        bounds = self.mask.get_bounding_rects()[0]
        
        # Calculate actual positions relative to the screen
        leftmost = self.rect.x + bounds.left
        rightmost = self.rect.x + bounds.right
        
        return leftmost, rightmost

    def check_collision(self, pipe):
        # Check if bird overlaps with pipe but not with gap
        pipe_overlap = self.mask.overlap(pipe.pipe_mask, 
            (pipe.pipe_rect.x - self.rect.x, pipe.pipe_rect.y - self.rect.y))
        gap_overlap = self.mask.overlap(pipe.gap_mask,
            (pipe.gap_rect.x - self.rect.x, pipe.gap_rect.y - self.rect.y))
        
        return pipe_overlap and not gap_overlap
