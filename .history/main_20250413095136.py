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
gray = (100, 100, 100)

screen = pygame.display.set_mode([300, 450])
pygame.display.set_caption('Idle Restaurant')
background = black
framerate = 60
font = pygame.font.Font(None, 16)
timer = pygame.time.Clock()

# Game variables
green_value, red_value, orange_value, white_value, purple_value = 1, 2, 3, 4, 5
green_speed, red_speed, orange_speed, white_speed, purple_speed = 5, 4, 3, 2, 1
green_length = red_length = orange_length = white_length = purple_length = 0
draw_green = draw_red = draw_orange = draw_white = draw_purple = False
auto_green = auto_red = auto_orange = auto_white = auto_purple = False
green_upgrade_cost = red_upgrade_cost = orange_upgrade_cost = white_upgrade_cost = purple_upgrade_cost = 10
green_manager_cost = red_manager_cost = orange_manager_cost = white_manager_cost = purple_manager_cost = 50

score = 0

def draw_task(color, y_coord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif draw and length >= 200:
        draw = False
        length = 0
        score += value
    pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])
    value_text = font.render(str(value), True, white)
    screen.blit(value_text, (16, y_coord - 10))
    return pygame.Rect(10, y_coord - 20, 40, 40), draw, length

def draw_button(text, x, y, width, height, cost, enabled):
    color = gray if not enabled else white
    pygame.draw.rect(screen, color, [x, y, width, height])
    label = font.render(text + f" (${cost})", True, black)
    screen.blit(label, (x + 5, y + 5))
    return pygame.Rect(x, y, width, height)

running = True
while running:
    timer.tick(framerate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Task triggers
            if task1.collidepoint(event.pos) and not auto_green:
                draw_green = True
            if task2.collidepoint(event.pos) and not auto_red:
                draw_red = True
            if task3.collidepoint(event.pos) and not auto_orange:
                draw_orange = True
            if task4.collidepoint(event.pos) and not auto_white:
                draw_white = True
            if task5.collidepoint(event.pos) and not auto_purple:
                draw_purple = True

            # Upgrades
            if green_upgrade_btn.collidepoint(event.pos) and score >= green_upgrade_cost and green_speed < 200:
                score -= green_upgrade_cost
                green_speed += 1
                green_upgrade_cost += 5

            if red_upgrade_btn.collidepoint(event.pos) and score >= red_upgrade_cost and red_speed < 200:
                score -= red_upgrade_cost
                red_speed += 1
                red_upgrade_cost += 5

            if orange_upgrade_btn.collidepoint(event.pos) and score >= orange_upgrade_cost and orange_speed < 200:
                score -= orange_upgrade_cost
                orange_speed += 1
                orange_upgrade_cost += 5

            if white_upgrade_btn.collidepoint(event.pos) and score >= white_upgrade_cost and white_speed < 200:
                score -= white_upgrade_cost
                white_speed += 1
                white_upgrade_cost += 5

            if purple_upgrade_btn.collidepoint(event.pos) and score >= purple_upgrade_cost and purple_speed < 200:
                score -= purple_upgrade_cost
                purple_speed += 1
                purple_upgrade_cost += 5

            # Managers
            if green_manager_btn.collidepoint(event.pos) and score >= green_manager_cost:
                score -= green_manager_cost
                auto_green = True

            if red_manager_btn.collidepoint(event.pos) and score >= red_manager_cost:
                score -= red_manager_cost
                auto_red = True

            if orange_manager_btn.collidepoint(event.pos) and score >= orange_manager_cost:
                score -= orange_manager_cost
                auto_orange = True

            if white_manager_btn.collidepoint(event.pos) and score >= white_manager_cost:
                score -= white_manager_cost
                auto_white = True

            if purple_manager_btn.collidepoint(event.pos) and score >= purple_manager_cost:
                score -= purple_manager_cost
                auto_purple = True

    # Auto-clicker logic
    if auto_green: draw_green = True
    if auto_red: draw_red = True
    if auto_orange: draw_orange = True
    if auto_white: draw_white = True
    if auto_purple: draw_purple = True

    screen.fill(background)
    task1, draw_green, green_length = draw_task(green, 50, green_value, draw_green, green_length, green_speed)
    task2, draw_red, red_length = draw_task(red, 110, red_value, draw_red, red_length, red_speed)
    task3, draw_orange, orange_length = draw_task(orange, 170, orange_value, draw_orange, orange_length, orange_speed)
    task4, draw_white, white_length = draw_task(white, 230, white_value, draw_white, white_length, white_speed)
    task5, draw_purple, purple_length = draw_task(purple, 290, purple_value, draw_purple, purple_length, purple_speed)

    # Buttons (Upgrade and Manager)
    green_upgrade_btn = draw_button("Upgrade", 10, 320, 100, 20, green_upgrade_cost, score >= green_upgrade_cost)
    green_manager_btn = draw_button("Manager", 120, 320, 100, 20, green_manager_cost, score >= green_manager_cost)

    red_upgrade_btn = draw_button("Upgrade", 10, 340, 100, 20, red_upgrade_cost, score >= red_upgrade_cost)
    red_manager_btn = draw_button("Manager", 120, 340, 100, 20, red_manager_cost, score >= red_manager_cost)

    orange_upgrade_btn = draw_button("Upgrade", 10, 360, 100, 20, orange_upgrade_cost, score >= orange_upgrade_cost)
    orange_manager_btn = draw_button("Manager", 120, 360, 100, 20, orange_manager_cost, score >= orange_manager_cost)

    white_upgrade_btn = draw_button("Upgrade", 10, 380, 100, 20, white_upgrade_cost, score >= white_upgrade_cost)
    white_manager_btn = draw_button("Manager", 120, 380, 100, 20, white_manager_cost, score >= white_manager_cost)

    purple_upgrade_btn = draw_button("Upgrade", 10, 400, 100, 20, purple_upgrade_cost, score >= purple_upgrade_cost)
    purple_manager_btn = draw_button("Manager", 120, 400, 100, 20, purple_manager_cost, score >= purple_manager_cost)

    display_score = font.render('Money: $' + str(round(score, 2)), True, white, black)
    screen.blit(display_score, (10, 5))
    pygame.display.update()

pygame.quit()
