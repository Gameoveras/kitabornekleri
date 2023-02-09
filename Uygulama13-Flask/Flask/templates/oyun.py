import pygame, sys

pygame.init()

pencere = pygame.display.set_mode((500,400))

kare = pygame.Surface((100,100))
kare.fill((255,0,0))
kare_rect = pygame.Rect((0,0), kare.get_size())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_UP]:
        kare_rect.y -= 2
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        kare_rect.y += 2
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        kare_rect.x -= 2
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        kare_rect.x += 2

    pencere.fill((0,0,0))

    pencere.blit(kare, kare_rect)
    pygame.display.flip()