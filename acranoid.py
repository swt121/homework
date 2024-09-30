import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 400, 600
BALL_RAD = 10
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 20
START_PLATFORM_WIDTH = PLATFORM_WIDTH
BRICK_WIDTH, BRICK_HEIGHT = 40, 20
LIVES = 3
FONT = pygame.font.SysFont("Arial", 20)
SPEED = 9
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

platform_x = WIDTH // 2 - PLATFORM_WIDTH // 2
platform_y = HEIGHT - PLATFORM_HEIGHT - 10
platform_speed = SPEED

ball_x = random.randint(275, WIDTH - BALL_RAD)
ball_y = random.randint(175, HEIGHT // 2)
ball_speed_x = random.choice([-SPEED, SPEED])
ball_speed_y = random.choice([-SPEED, SPEED])
start_ball_speed_x = ball_speed_x
start_ball_speed_y = ball_speed_y

bricks = []
rows = 7
for row in range(rows):
    for i in range(0, WIDTH, BRICK_WIDTH + 10):
        bricks.append(pygame.Rect(i, 30 + row * (BRICK_HEIGHT + 5), BRICK_WIDTH + 3, BRICK_HEIGHT - 3))

bonus_types = ['plat', 'plus_life', 'ball','minus_life']
bonus = None
bonus_type = None
bonus_speed = 10

bonus_end_time_plat = 0
bonus_end_time_ball = 0
plat_increased = False
ball_speed_decreased = False

running = True
game_over = False
game_win = False

while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over:
        screen.fill(WHITE)
        game_over_text = FONT.render("GAME OVER", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        time.sleep(2.5)
        break

    if game_win:
        screen.fill(WHITE)
        game_over_text = FONT.render("YOU WIN", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        time.sleep(2.5)
        break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        platform_x -= platform_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        platform_x += platform_speed

    if platform_x < 0:
        platform_x = 0
    if platform_x + PLATFORM_WIDTH > WIDTH:
        platform_x = WIDTH - PLATFORM_WIDTH

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - BALL_RAD <= 0 or ball_x + BALL_RAD >= WIDTH:
        ball_speed_x *= -1
    if ball_y - BALL_RAD <= 0:
        ball_speed_y *= -1

    if platform_y <= ball_y + BALL_RAD <= platform_y + PLATFORM_HEIGHT:
        if platform_x <= ball_x <= platform_x + PLATFORM_WIDTH:
            ball_speed_y *= -1

    if ball_y + BALL_RAD >= HEIGHT:
        LIVES -= 1
        ball_speed_y *= 1.5
        ball_speed_x *= 1.5
        if LIVES == 0:
            game_over = True
        else:
            ball_x = random.randint(275, WIDTH - BALL_RAD)
            ball_y = random.randint(175, HEIGHT // 2)
            ball_speed_x = random.choice([-SPEED, SPEED])
            ball_speed_y = random.choice([-SPEED, SPEED])

    for brick in bricks[:]:
        if brick.colliderect(pygame.Rect(ball_x - BALL_RAD, ball_y - BALL_RAD, BALL_RAD * 2, BALL_RAD * 2)):
            ball_speed_y *= -1
            bricks.remove(brick)

            if random.random() < 0.1:
                bonus_type = random.choice(bonus_types)
                bonus = pygame.Rect(brick.x, brick.y, 20, 20)

    if not bricks:
        game_win = True

    if bonus:
        bonus.y += bonus_speed
        if bonus.colliderect(pygame.Rect(platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)):
            if bonus_type == 'plat' and not plat_increased:
                print("Бонус пойман! Платформа увеличена на 10 секунд.")
                PLATFORM_WIDTH *= 2
                bonus_end_time_plat = time.time() + 10
                plat_increased = True

            elif bonus_type == 'plus_life':
                print("Бонус пойман! Добавлена одна жизнь.")
                LIVES += 1

            elif bonus_type == 'ball' and not ball_speed_decreased:
                print('Бонус пойман! Скорость шарика уменьшилась на 10 секунд.')
                ball_speed_x /= 2
                ball_speed_y /= 2
                bonus_end_time_ball = time.time() + 10
                ball_speed_decreased = True

            elif bonus_type == 'minus_life':
                print('Бонус пойман! Удалена одна жизнь.')
                LIVES -= 1
                if LIVES < 1:
                    game_over = True

            bonus = None

        elif bonus.y > HEIGHT:
            bonus = None

    if plat_increased and time.time() > bonus_end_time_plat:
        print('Бонус увеличения платформы закончился! Платформа вернулась к норме.')
        PLATFORM_WIDTH = START_PLATFORM_WIDTH
        plat_increased = False

    if ball_speed_decreased and time.time() > bonus_end_time_ball:
        print('Бонус замедления шарика закончился! Скорость шарика вернулась к норме.')
        ball_speed_x = start_ball_speed_x
        ball_speed_y = start_ball_speed_y
        ball_speed_decreased = False

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, (int(ball_x), int(ball_y)), BALL_RAD)

    pygame.draw.rect(screen, BLACK, (platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT))

    for brick in bricks:
        pygame.draw.rect(screen, (165, 42, 42), brick)

    if bonus:
        pygame.draw.circle(screen, (216, 235, 52), (bonus.x + 10, bonus.y + 10), 5)

    lives_text = FONT.render(f"Жизни: {LIVES}", True, BLACK)
    screen.blit(lives_text, (10, 5))

    pygame.display.update()

pygame.quit()