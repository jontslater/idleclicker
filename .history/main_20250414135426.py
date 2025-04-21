import pygame
import os

pygame.init()

# Screen setup for phone dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Idle Restaurant")

background = pygame.image.load("C:/Users/lisaa/workspace/idleclicker/Leonardo_Phoenix_10_A_cozy_cartoonstyle_restaurant_interior_wa_1.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonts and colors
font_small = pygame.font.Font(None, 24)
font_large = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
GREEN = (100, 255, 100)
RED = (255, 0, 0)

# Station data
stations = [
    {"name": "Salad", "value": 10, "progress": 0, "max": 300, "color": (180, 255, 180), "manager": False},
    {"name": "Soup", "value": 25, "progress": 0, "max": 250, "color": (255, 210, 150), "manager": False},
    {"name": "Pasta", "value": 50, "progress": 0, "max": 200, "color": (255, 150, 150), "manager": False},
    {"name": "Pizza", "value": 100, "progress": 0, "max": 180, "color": (255, 255, 180), "manager": False},
]

# Player money
player_money = 0

# Button setup
button_start = pygame.Rect(50, 700, 100, 40)
button_manager = pygame.Rect(250, 700, 100, 40)

def draw_ui():
    screen.blit(background, (0, 0))
    y_offset = 120

    # Draw header
    header = font_large.render(f"${player_money:,.2f}", True, WHITE)
    screen.blit(header, (20, 40))

    # Draw stations
    for i, station in enumerate(stations):
        # Progress fill
        progress_width = (station["progress"] / station["max"]) * 280
        pygame.draw.rect(screen, GREEN, (20, y_offset, progress_width, 40))

        # Base color on top with border
        pygame.draw.rect(screen, station["color"], (20, y_offset, 280, 40))
        pygame.draw.rect(screen, GRAY, (20, y_offset, 280, 40), 2)

        # Text
        name = font_small.render(station["name"], True, BLACK)
        screen.blit(name, (30, y_offset + 10))

        income = font_small.render(f"${station['value']}/sec", True, BLACK)
        screen.blit(income, (220, y_offset + 10))

        # Manager status
        if station["manager"]:
            manager_text = font_small.render("Manager Hired", True, RED)
            screen.blit(manager_text, (220, y_offset + 30))

        y_offset += 70

    # Draw buttons
    pygame.draw.rect(screen, WHITE, button_start)
    start_text = font_small.render("Start Revenue", True, BLACK)
    screen.blit(start_text, (button_start.x + 10, button_start.y + 10))

    pygame.draw.rect(screen, WHITE, button_manager)
    manager_text = font_small.render("Hire Manager", True, BLACK)
    screen.blit(manager_text, (button_manager.x + 10, button_manager.y + 10))


def handle_buttons():
    global player_money

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if button_start.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
        # Start revenue generation for each station
        for station in stations:
            if not station["manager"]:
                station["progress"] += station["value"]
                player_money += station["value"]

    if button_manager.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
        # Hire a manager for the first available station
        for station in stations:
            if not station["manager"] and player_money >= station["value"]:
                station["manager"] = True
                player_money -= station["value"]
                break


# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle button clicks
    handle_buttons()

    # Update logic (example: increase progress automatically if manager is hired)
    for station in stations:
        if station["manager"]:
            station["progress"] += station["value"]
            if station["progress"] >= station["max"]:
                station["progress"] = 0
                player_money += station["value"]

    draw_ui()
    pygame.display.flip()

pygame.quit()
