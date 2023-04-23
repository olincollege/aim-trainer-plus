"""
Window, colors, and targets and timer
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerRange:
    """
    Window for game and active elements.
    """

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # Window Size
    WINDOWHEIGHT = 750
    WINDOWWIDTH = 750

    FONT = pygame.font.SysFont(cs_regular.ttf, 48)

    def __init__(self):
        """
        Clock and Window
        """
        self._clock = pygame.time.Clock()
        self._window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
