import pygame

pygame.init()
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode(size=(HEIGHT, WIDTH))
clock = pygame.time.Clock()
pygame.display.set_caption('circle in box')


# why without events pygame hangs
x, y = 255, 255
step = 20
running = True
while running:
    screen.fill((255, 255, 255))  # RGB - red, green, blue; 0 - black; 255 - white
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 500, 500), 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= step
    if pressed[pygame.K_DOWN]:
        y += step
    if pressed[pygame.K_LEFT]:
        x -= step
    if pressed[pygame.K_RIGHT]:
        x += step
    if x <= 0 or x >= WIDTH - 25:
        x = -x
    if y <= 0 or y >= HEIGHT - 25:
        y = -y
    print(pygame.K_UP)
    circle = pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.flip()

    clock.tick(140)