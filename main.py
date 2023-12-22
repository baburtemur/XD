import pygame
import random



if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('QUADRATO')
    running = True
    size = height, width = 200, 200
    clock = pygame.time.Clock()
    color = pygame.Color('white')
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    pygame.display.flip()
    screen2 = pygame.Surface(screen.get_size())
    a = 0
    font1 = pygame.font.SysFont(str(a), 42)
    img1 = font1.render(str(a), True, (255, 0, 0))
    screen.blit(img1, (20, 20))
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.WINDOWEVENT_HIDDEN:
                a += 1
            if event.type == pygame.WINDOWEVENT_SHOWN:
                font1 = pygame.font.SysFont(str(a), 42)
                img1 = font1.render(str(a), True, (255, 0, 0))
                screen.blit(img1, (20, 20))

    pygame.quit()