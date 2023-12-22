import pygame
import os
import sys


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('QUADRATO')
    running = True
    size = height, width = 200, 200
    screen = pygame.display.set_mode(size)

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            sys.exit()
        qq = pygame.image.load(fullname)
        return qq

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image('arrow.png')
    sprite.rect = sprite.image.get_rect()


    pygame.mouse.set_visible(False)
    while running:
        screen.fill(pygame.Color("black"))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.topleft = event.pos
            if pygame.mouse.get_focused():
               all_sprites.draw(screen)
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()

