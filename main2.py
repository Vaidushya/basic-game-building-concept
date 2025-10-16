import pygame

# Making a hollow and a solid ball

pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill((255, 255, 255))
green = (0, 255, 0)

pygame.draw.circle(screen, green, (100, 100), 50) # solid
pygame.draw.circle(screen, green, (300, 300), 50, 5) # hollow

pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()