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


screen = pygame.display.set_mode([300, 450])
pygame.display.set_caption('Idle Restaurant')
background = black
framerate = 60
font = pygame.font.Font(None, 16)
timer = pygame.time.Clock()

running = True
while running:
    timer.tick(framerate)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    pygame.display.update()

pygame.quit()
