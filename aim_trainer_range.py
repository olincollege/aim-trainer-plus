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
        Clock
        """
        self._clock = pygame.time.Clock()

    def populateConfig(self, difficulty):
        """
        Resizes image based on difficulty selected. A harder difficulty generates a smaller image.

        Args:
            a string with the value of the difficulty

        Returns:
            a pixel array of the resized target
        """
        global targetImage
        targetImage = pygame.image.load("target.png")
        config = {}
        if difficulty == "easy":
            difficultyFile = open("easy.txt", "r")
        elif difficulty == "medium":
            difficultyFile = open("medium.txt", "r")
        elif difficulty == "hard":
            difficultyFile = open("hard.txt", "r")
        for line in difficultyFile:
            splitLine = line.split(":")
            splitLine[1] = splitLine[1].strip("\n")
            config[splitLine[0]] = int(splitLine[1])
        targetImage = pygame.transform.scale(
            targetImage, (config["enemySize"], config["enemySize"])
        )
        difficultyFile.close()
        return config
