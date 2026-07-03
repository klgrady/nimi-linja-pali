import sys, pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

black = (0, 0, 0)
white = (255, 255, 255)
violet = (153, 153, 255)
aqua = (0, 204, 255)
orange = (255, 153, 0)
vermillion = (255, 102, 0)
teal = (0, 128, 128)

color = vermillion

while running:
    # poll for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game render
    font = pygame.font.Font(None, 74)
    text = font.render("utala", True, black)

    # fill screen
    screen.fill(color)
    screen.blit(text, (250, 250))

    # flip the display onto user screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


