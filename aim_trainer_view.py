"""
Aim Trainer Text Prompts
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerView:
    """
    Opens window for game and prompts user text.

    Attributes:

    """

    def __init__(self, FONT, COLORS['RED']):
        """
        Makes instance of font and red
        """
        self.FONT = FONT
        self.RED = COLORS['RED']

    def drawText(text, surface, x, y, font=self.FONT, color=self.RED):
        """
        Prints intractable text for user
        """
        textObject = font.render(text, 1, color)
        textRect = textObject.get_rect()
        textRect.topleft = (x, y)
        surface.blit(textObject, textRect)

    def gameOver(totalShots, hitShots, difficulty, score):
        """
        Presents player with end of games stats and prompts for new game
        """
        pygame.mouse.set_visible(True)
        if totalShots != 0 and hitShots != 0:
            accuracy = round(hitShots / totalShots * 100)
        else:
            accuracy = 0
        range.windowSurface.fill(COLORS['BLACK'])
        drawText(
            "GAME OVER",
            range.windowSurface,
            200,
            325,
            pygame.font.SysFont(None, 72, True),
        )
        drawText(
            "Click anywhere to restart", range.windowSurface, 170, 380
        )
        drawText(
            "Accuracy: " + str(accuracy) + "%", range.windowSurface, 269, 414
        )
        drawText("Score: " + str(score), range.windowSurface, 308, 450)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == MOUSEBUTTONDOWN:
                    range.windowSurface.fill(range.WHITE)
                    Menu()
                if event.type == KEYDOWN:
                    terminate()
