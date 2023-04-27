import os
import pygame
import random
import screen 

# Load target image
target_image = pygame.image.load(os.path.join("target.jpg"))
target_image = pygame.transform.scale(target_image, (2 * target_radius, 2 * target_radius))
target_rect = target_image.get_rect()

# Scale the image to a specific size (50x50 pixels)
target_width, target_height = 50, 50
target_image = pygame.transform.scale(target_image, (target_width, target_height))
target_rect = target_image.get_rect()

# Update the target position
def update_target_pos():
    target_rect.x = random.randint(target_radius, WIDTH - target_radius - target_rect.width)
    target_rect.y = random.randint(target_radius, HEIGHT - target_radius - target_rect.height)

update_target_pos()

# Load "do not hit" target image
dont_hit_image = pygame.image.load(os.path.join("dont_hit.jpg"))

# Scale the "do not hit" image to a specific size (50x50 pixels)
dont_hit_width, dont_hit_height = 50, 50
dont_hit_image = pygame.transform.scale(dont_hit_image, (dont_hit_width, dont_hit_height))
dont_hit_rect = dont_hit_image.get_rect()

# Update the "do not hit" target position
def update_dont_hit_pos():
    dont_hit_rect.x = random.randint(0, WIDTH - dont_hit_rect.width)
    dont_hit_rect.y = random.randint(0, HEIGHT - dont_hit_rect.height)

update_dont_hit_pos()

# Modify the main game loop
while running:
    screen.fill(WHITE)

    # Draw targets
    screen.blit(target_image, target_rect)
    screen.blit(dont_hit_image, dont_hit_rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_pos = pygame.mouse.get_pos()
            if target_rect.collidepoint(mouse_pos):
                score += 1
                update_target_pos()
            elif dont_hit_rect.collidepoint(mouse_pos):
                score -= 1  # Decrease the score if you hit the "do not hit" target
                update_dont_hit_pos()

    # Update the screen
    pygame.display.flip()
    clock.tick(60)