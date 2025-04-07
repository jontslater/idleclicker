import pygame
pygame.init()
print("Game is starting...")

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (127, 0, 255)
orange = (255, 165, 0)

# Screen setup
screen = pygame.display.set_mode([300, 450])
pygame.display.set_caption('Idle Restaurant')
background = white  # Changed to white to check if the screen is rendering properly
framerate = 60
font = pygame.font.Font(None, 16)  # Changed to default font
timer = pygame.time.Clock()

running = True
while running:
    print("Game Loop Running...")  # Check if the game loop is running
    timer.tick(framerate)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    pygame.display.update()  # Ensure the display updates after filling the screen

pygame.quit()
