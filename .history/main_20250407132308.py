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

def draw_task(color, y_coord):
  pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
  pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
  pygame.draw.rect(screen, black, [75, y_coord - 10, 190, 20])

running = True
while running:
    timer.tick(framerate)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    draw_task(green, 50)
    pygame.display.update()

pygame.quit()
