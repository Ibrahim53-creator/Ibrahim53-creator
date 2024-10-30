import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load images
player_image = pygame.Surface((50, 50))
player_image.fill(RED)

obstacle_image = pygame.Surface((50, 50))
obstacle_image.fill(BLACK)

# Game classes
class Player:
    def __init__(self):
        self.rect = player_image.get_rect(center=(100, SCREEN_HEIGHT - 100))
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(player_image, self.rect)

class Obstacle:
    def __init__(self):
        self.rect = obstacle_image.get_rect(center=(SCREEN_WIDTH, random.randint(50, SCREEN_HEIGHT - 50)))
        self.speed = 5

    def move(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(obstacle_image, self.rect)

# Main game loop
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Subway Surfers-like Game")
    clock = pygame.time.Clock()

    player = Player()
    obstacles = []
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.move()

        # Create new obstacles
        if random.randint(1, 20) == 1:
            obstacles.append(Obstacle())

        # Move obstacles
        for obstacle in obstacles:
            obstacle.move()
            if obstacle.rect.right < 0:
                obstacles.remove(obstacle)
                score += 1

        # Check for collisions
        for obstacle in obstacles:
            if player.rect.colliderect(obstacle.rect):
                print("Game Over! Score:", score)
                running = False

        # Drawing
        screen.fill(WHITE)
        player.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()

