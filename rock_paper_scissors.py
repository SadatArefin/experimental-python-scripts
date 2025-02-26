import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480
# set mode of the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# set the title of the screen
pygame.display.set_caption("Rock Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
rock_img = pygame.image.load('rock.png')
paper_img = pygame.image.load('paper.png')
scissors_img = pygame.image.load('scissors.png')

# Resize images
rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissors_img = pygame.transform.scale(scissors_img, (150, 150))

# Font
font = pygame.font.Font(None, 36)

# Game variables
choices = ['rock', 'paper', 'scissors']
user_choice = None
computer_choice = None
result = ""

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 50 < x < 150 and 200 < y < 300:
                user_choice = 'rock'
            elif 250 < x < 350 and 200 < y < 300:
                user_choice = 'paper'
            elif 450 < x < 550 and 200 < y < 300:
                user_choice = 'scissors'
            
            if user_choice:
                computer_choice = random.choice(choices)
                result = get_winner(user_choice, computer_choice)

    # Draw images
    screen.blit(rock_img, (50, 200))
    screen.blit(paper_img, (250, 200))
    screen.blit(scissors_img, (450, 200))

    # Display result
    if user_choice and computer_choice:
        user_text = font.render(f'You chose: {user_choice}', True, BLACK)
        computer_text = font.render(f'Computer chose: {computer_choice}', True, BLACK)
        result_text = font.render(result, True, BLACK)
        screen.blit(user_text, (50, 50))
        screen.blit(computer_text, (50, 100))
        screen.blit(result_text, (50, 150))

    pygame.display.flip()

pygame.quit()