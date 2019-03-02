import pygame
from os import access, F_OK


def check_img(img, size):

    if access(img, F_OK):
        image = pygame.image.load(img).convert_alpha()

    else:
        image = pygame.image.load("./images/no_signal.png")

    if image.get_rect().size != (40, 40):
        image = pygame.transform.scale(image, (size, size))

    return image
