import pygame

pygame.init()
# Phone dimensions (for a more realistic phone screen)
screen = pygame.display.set_mode([375, 667])
pygame.display.set_caption('Idle Restaurant')

background_img = pygame.image.load("c:/Users/lisaa/workspace/idleclicker/Leonardo_Phoenix_10_A_cozy_cartoonstyle_restaurant_interior_wa_1.jpg").convert()
background_img = pygame.transform.scale(background_img, (375, 667))

# Colors
red = (255, 80, 80)
green = (100, 255, 100)
orange = (255, 180, 100)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (200, 150, 255)
gray = (180, 180, 180)
dark_gray = (70, 70, 70)

screen = pygame.display.set_mode([375, 667])
pygame.display.set_caption('Idle Restaurant')
background = background_img
framerate = 60
font = pygame.font.Font(None, 20)
timer = pygame.time.Clock()

# Game values
score = 0

# Station data
stations = [
    {"name": "Salad 🥗", "color": green, "value": 1, "speed": 5, "length": 0, "draw": False, "auto": False, "upgrade_cost": 10, "manager_cost": 50},
    {"name": "Pasta 🍝", "color": red, "value": 2, "speed": 4, "length": 0, "draw": False, "auto": False, "upgrade_cost": 15, "manager_cost": 100},
    {"name": "Juice 🍊", "color": orange, "value": 3, "speed": 3, "length": 0, "draw": False, "auto": False, "upgrade_cost": 20, "manager_cost": 150},
    {"name": "Bread 🍞", "color": white, "value": 4, "speed": 2, "length": 0, "draw": False, "auto": False, "upgrade_cost": 30, "manager_cost": 200},
    {"name": "Cake 🍰", "color": purple, "value": 5, "speed": 1, "length": 0, "draw": False, "auto": False, "upgrade_cost": 40, "manager_cost": 300},
]

def draw_station(station, y):
    global score
    # Auto-run if manager purchased
    if station["auto"]:
        station["draw"] = True

    # Progress bar logic
    if station["draw"] and station["length"] < 200:
        station["length"] += station["speed"]
    elif station["draw"] and station["length"] >= 200:
        station["draw"] = False
        station["length"] = 0
        score += station["value"]

    # Draw icon
    pygame.draw.circle(screen, station["color"], (30, y), 20)
    pygame.draw.rect(screen, station["color"], [70, y - 15, 230, 30])  # Widened progress bar
    pygame.draw.rect(screen, black, [75, y - 10, 225, 20])  # Black border for the bar
    pygame.draw.rect(screen, station["color"], [70, y - 15, station["length"], 30])  # Progress fill

    # Draw the name inside the progress bar
    label = font.render(station["name"], True, white)
    screen.blit(label, (70 + (230 - station["length"]) // 2, y - 8))  # Centered text

    value_text = font.render(f"${station['value']}", True, black)
    screen.blit(value_text, (18, y - 8))

    # Buttons: upgrade and manager
    upg_btn = pygame.Rect(280, y - 15, 100, 20)
    mgr_btn = pygame.Rect(390, y - 15, 100, 20)

    pygame.draw.rect(screen, gray, upg_btn)
    pygame.draw.rect(screen, gray, mgr_btn)

    upg_label = font.render(f"Upgrade (${station['upgrade_cost']})", True, black)
    mgr_label = font.render(f"Manager (${station['manager_cost']})", True, black)
    screen.blit(upg_label, (upg_btn.x + 4, upg_btn.y + 2))
    screen.blit(mgr_label, (mgr_btn.x + 4, mgr_btn.y + 2))

    return pygame.Rect(10, y - 20, 40, 40), upg_btn, mgr_btn

running = True
while running:
    timer.tick(framerate)
    screen.blit(background, (0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, station in enumerate(stations):
                task_y = 50 + i * 65  # Adjusted spacing
                task_rect, upg_rect, mgr_rect = draw_station(station, task_y)

                # Manual click for non-automated stations
                if task_rect.collidepoint(event.pos) and not station["auto"]:
                    station["draw"] = True

                # Upgrade button clicked
                if upg_rect.collidepoint(event.pos) and score >= station["upgrade_cost"]:
                    score -= station["upgrade_cost"]
                    station["speed"] += 1
                    station["upgrade_cost"] += 10

                # Manager button clicked
                if mgr_rect.collidepoint(event.pos) and not station["auto"] and score >= station["manager_cost"]:
                    score -= station["manager_cost"]
                    station["auto"] = True  # Enable automation

    # Auto-progress for stations with managers
    for station in stations:
        if station["auto"]:
            if station["length"] < 200:  # The station will progress automatically
                station["length"] += station["speed"]
            elif station["length"] >= 200:
                station["length"] = 0  # Reset progress after reaching max
                score += station["value"]  # Earn money for fully processed items

    # Draw stations
    for i, station in enumerate(stations):
        draw_station(station, 50 + i * 65)

    # Score display
    money_text = font.render(f"Money: ${round(score, 2)}", True, white)
    screen.blit(money_text, (10, 10))

    pygame.display.update()

pygame.quit()
