import pygame
import os

pygame.init()

# Screen setup for phone dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Idle Restaurant")

# Load background image (replace with your actual path)
# background = pygame.image.load("restaurant_bg.jpg")  # Make sure this is 400x800
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonts and colors
font_small = pygame.font.Font(None, 24)
font_large = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
GREEN = (100, 255, 100)

# Station data
stations = [
    {"name": "Salad", "value": 10, "progress": 0, "max": 300, "color": (180, 255, 180)},
    {"name": "Soup", "value": 25, "progress": 0, "max": 250, "color": (255, 210, 150)},
    {"name": "Pasta", "value": 50, "progress": 0, "max": 200, "color": (255, 150, 150)},
    {"name": "Pizza", "value": 100, "progress": 0, "max": 180, "color": (255, 255, 180)},
]

def draw_ui():
    screen.blit(background, (0, 0))
    y_offset = 120

    # Draw header
    header = font_large.render("$134.993 M", True, WHITE)
    screen.blit(header, (20, 40))

    # Draw stations
    for i, station in enumerate(stations):
        pygame.draw.rect(screen, station["color"], (20, y_offset, 280, 40))
        pygame.draw.rect(screen, GRAY, (20, y_offset, 280, 40), 2)

        # Progress fill
        progress_width = (station["progress"] / station["max"]) * 280
        pygame.draw.rect(screen, GREEN, (20, y_offset, progress_width, 40))

        # Text
        name = font_small.render(station["name"], True, BLACK)
        screen.blit(name, (30, y_offset + 10))

        income = font_small.render(f"${station['value']}/sec", True, BLACK)
        screen.blit(income, (220, y_offset + 10))

        y_offset += 70

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update logic (example: increase progress)
    for station in stations:
        station["progress"] += 1
        if station["progress"] >= station["max"]:
            station["progress"] = 0
            # Here you could increase money by station['value']

    draw_ui()
    pygame.display.flip()

pygame.quit()
