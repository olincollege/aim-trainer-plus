"""
Window, colors, and targets and timer
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerRange:
    """
    Window for game and active elements.

    Attributes:
        BLACK: a tuple of ints that represent a hex code
        WHITE: a tuple of ints that represent a hex code
        RED: a tuple of ints that represent a hex code
        BLUE: a tuple of ints that represent a hex code
        WINDOWHEIGHT: a int being the number of pixels high the window will be
        WINDOWWIDTH: a int being the number of pixels wide the window will be
        FONT:
    """

    # Colors

    COLORS = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "BLUE": (0, 0, 255),
    }

    # Window Size
    WINDOWHEIGHT = 750
    WINDOWWIDTH = 750

    FONT = pygame.font.SysFont(cs_regular.ttf, 48)

    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("sniper")

    shootSound = pygame.mixer.Sound("snipersound.wav")
    hitSound = pygame.mixer.Sound("metalHit.wav")
    shootSound.set_volume(0.25)
    hitSound.set_volume(1)

    def __init__(self):
        """
        Clock and score
        """
        self._clock = pygame.time.Clock()
        # self._hits =

    def populateConfig(difficulty):
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
