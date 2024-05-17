import pygame

# Initialize Pygame
pygame.init()

# Set window size and title
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure Game")

# Load font
font = pygame.font.Font(None, 32)

# Introduction
intro_text = font.render("Welcome to the Adventure Game!", 1, (255, 255, 255))
window.blit(intro_text, (100, 100))
intro_text = font.render("You are a brave adventurer on a quest to defeat the evil dragon and save the kingdom.", 1, (255, 255, 255))
window.blit(intro_text, (100, 150))

# First choice
choice_text = font.render("You come to a fork in the road. Do you go left or right?", 1, (255, 255, 255))
window.blit(choice_text, (100, 200))

# Create left and right buttons
left_button = pygame.Rect(100, 250, 150, 50)
right_button = pygame.Rect(550, 250, 150, 50)
pygame.draw.rect(window, (255, 255, 255), left_button)
pygame.draw.rect(window, (255, 255, 255), right_button)
left_text = font.render("Left", 1, (0, 0, 0))
window.blit(left_text, (150, 270))
right_text = font.render("Right", 1, (0, 0, 0))
window.blit(right_text, (600, 270))

# Update display
pygame.display.update()

# Wait for user input
choice = None
while choice is None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if user clicked on left or right button
            if left_button.collidepoint(event.pos):
                choice = "left"
            elif right_button.collidepoint(event.pos):
                choice = "right"

# Clear window
window.fill((0, 0, 0))

# First choice outcomes
#if choice == "left":
