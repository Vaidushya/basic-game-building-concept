import pygame

# initialize pygame
pygame.init()

# game setup
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("My First Game Screen🪟")
screen.fill((255, 255, 255))
brown = (150, 75, 0)
blue = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)

# title
font = pygame.font.Font(None, 74)
text = font.render("My Window", 1, black)
screen.blit(text, (100, 10))

# window
window = pygame.draw.rect(screen, brown, (150, 100, 200, 200), 5)
scene =  pygame.draw.rect(screen, blue, (155, 105, 190, 190))
line = pygame.draw.line(screen, brown, (250, 100), (250, 300), 5)
line2 = pygame.draw.line(screen, brown, (150, 200), (350, 200), 5)
window_shine = pygame.draw.rect(screen, white, (300, 120, 30, 30))

pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()