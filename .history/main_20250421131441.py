import pygame

pygame.init()

# Screen setup (phone dimensions)
screen = pygame.display.set_mode([375, 667])
pygame.display.set_caption('Idle Restaurant')

# Load and scale background
background_img = pygame.image.load("c:/Users/lisaa/workspace/idleclicker/Leonardo_Phoenix_10_A_cozy_cartoonstyle_restaurant_interior_wa_1.jpg").convert()
background_img = pygame.transform.scale(background_img, (375, 667))
background = background_img

# Load chef icon image
Icon_img = pygame.image.load("C:/Users/lisaa/workspace/idleclicker/ChefCircle.png").convert_alpha()

# Colors
red = (255, 80, 80)
green = (100, 255, 100)
orange = (255, 180, 100)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (200, 150, 255)
gray = (180, 180, 180)

# Font and clock
font = pygame.font.Font(None, 20)
framerate = 60
timer = pygame.time.Clock()

# Game values
score = 0

# Station data
stations = [
    {"name": "Salad 🥗", "color": green, "value": 1, "speed": 5, "length": 0, "draw": False, "auto": False, "upgrade_cost": 10, "manager_cost": 50, "manager_level": 0},
    {"name": "Pasta 🍝", "color": red, "value": 2, "speed": 4, "length": 0, "draw": False, "auto": False, "upgrade_cost": 15, "manager_cost": 100, "manager_level": 0},
    {"name": "Juice 🍊", "color": orange, "value": 3, "speed": 3, "length": 0, "draw": False, "auto": False, "upgrade_cost": 20, "manager_cost": 150, "manager_level": 0},
    {"name": "Bread 🍞", "color": white, "value": 4, "speed": 2, "length": 0, "draw": False, "auto": False, "upgrade_cost": 30, "manager_cost": 200, "manager_level": 0},
    {"name": "Cake 🍰", "color": purple, "value": 5, "speed": 1, "length": 0, "draw": False, "auto": False, "upgrade_cost": 40, "manager_cost": 300, "manager_level": 0},
]

def draw_circular_icon(image, position, size):
    # Resize the image
    icon_scaled = pygame.transform.smoothscale(image, (size, size)).convert_alpha()

    # Create a surface for the mask
    mask_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.circle(mask_surface, (255, 255, 255, 255), (size // 2, size // 2), size // 2)

    # Apply mask using BLEND_RGBA_MIN
    icon_scaled.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    # Blit the icon to the screen
    screen.blit(icon_scaled, position)

    return pygame.Rect(position[0], position[1], size, size)

def draw_station(station, y):
    global score

    if station["auto"]:
        station["draw"] = True

    # Progress logic
    if station["draw"] and station["length"] < 200:
        station["length"] += station["speed"]
    elif station["draw"] and station["length"] >= 200:
        station["draw"] = False
        station["length"] = 0
        score += station["value"]

    # Draw circular icon
    icon_rect = draw_circular_icon(Icon_img, (10, y - 20), 40,)
    pygame.draw.rect(screen, black, icon_rect, 2)

    # Progress bar background
    pygame.draw.rect(screen, station["color"], [70, y - 15, 230, 30])
    pygame.draw.rect(screen, black, [75, y - 10, 225, 20])
    pygame.draw.rect(screen, station["color"], [70, y - 15, station["length"], 30])

    # Text
    label = font.render(station["name"], True, white)
    screen.blit(label, (70 + (230 - station["length"]) // 2, y - 8))

    value_text = font.render(f"${station['value']}", True, black)
    screen.blit(value_text, (18, y - 8))

    # Buttons
    upg_btn = pygame.Rect(240, y - 15, 60, 20)
    mgr_btn = pygame.Rect(305, y - 15, 60, 20)

    pygame.draw.rect(screen, gray, upg_btn)
    pygame.draw.rect(screen, gray, mgr_btn)

    upg_label = font.render(f"Upg ${station['upgrade_cost']}", True, black)
    mgr_label = font.render(f"Mgr ${station['manager_cost']}", True, black)
    screen.blit(upg_label, (upg_btn.x + 2, upg_btn.y + 2))
    screen.blit(mgr_label, (mgr_btn.x + 2, mgr_btn.y + 2))

    return icon_rect, upg_btn, mgr_btn

# Game loop
running = True
while running:
    timer.tick(framerate)
    screen.blit(background, (0, 0))

    station_rects = []
    for i, station in enumerate(stations):
        task_y = 50 + i * 65
        rects = draw_station(station, task_y)
        station_rects.append(rects)

    # Score display
    money_text = font.render(f"Money: ${round(score, 2)}", True, white)
    screen.blit(money_text, (10, 10))

    pygame.display.update()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, station in enumerate(stations):
                task_rect, upg_rect, mgr_rect = station_rects[i]

                if task_rect.collidepoint(event.pos) and not station["auto"]:
                    station["draw"] = True

                if upg_rect.collidepoint(event.pos) and score >= station["upgrade_cost"]:
                    score -= station["upgrade_cost"]
                    station["speed"] += 1
                    station["upgrade_cost"] += 10

                if mgr_rect.collidepoint(event.pos) and score >= station["manager_cost"]:
                    score -= station["manager_cost"]
                    station["auto"] = True
                    station["manager_level"] += 1
                    station["manager_cost"] = int(station["manager_cost"] * 1.5)

pygame.quit()
