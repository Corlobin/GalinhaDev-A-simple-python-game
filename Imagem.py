__author__ = 'Ricardo'

import os

import pygame

main_dir = os.path.split(os.path.abspath(__file__))[0]


class Imagem(object):
    def __init__(self):
        return

    @staticmethod
    def load_image(name, transparent):
        path = os.path.join(main_dir, 'dados/imagens/', name)
        try:
            print(path)
            surface = pygame.image.load(path)

        except pygame.error:
            print(path)
            raise SystemExit('Nao foi possivel carregar a imagem %s %s ' % (path, pygame.get_error()))
        print(path)
        if transparent:
            corner = surface.get_at((0, 0))
            surface.set_colorkey(corner, pygame.RLEACCEL)

        print(surface)
        return surface.convert()
