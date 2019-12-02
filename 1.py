import pygame


pygame.init()
size = int(input())
cage = int(input())
s = size, size
screen = pygame.display.set_mode(s)
color = (0, 0, 0)
for i in range(cage):
    x = (0, size - ((size // cage) * (i + 1)))
    y = (size // cage, size - ((size // cage) * i))
    print(x)
    print(y)
    print()
    for j in range(cage):
        pygame.draw.rect(screen, color, (x[0], x[1], y[0], y[1]), 0)
        new_x = (x[0] + size // cage, x[1])
        x = new_x
        new_y = (y[0] + size // cage, y[1])
        y = new_y
        if color == (0, 0, 0):
            color = (255, 255, 255)
        elif color == (255, 255, 255):
            color = (0, 0, 0)
    if cage % 2 == 0:
        if color == (0, 0, 0):
            color = (255, 255, 255)
        elif color == (255, 255, 255):
            color = (0, 0, 0)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()

print()
