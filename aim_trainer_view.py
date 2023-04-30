"""
Aim Trainer Text Prompts
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerView:
    """
    Prompts text
    """

    FONT = pygame.font.SysFont(None, 48)

    def __init__(self, status):
        """ """
        self._status = status

    def draw_text(
        self, text, surface, x, y, font=FONT, color=self._status.COLORS["RED"]
    ):
        """
        Prints intractable text for user
        """
        # Load text
        text_object = font.render(text, 1, color)
        # get area of text
        text_rect = text_object.get_rect()
        # align text
        text_rect.topleft = (x, y)
        # display on surface
        surface.blit(text_object, text_rect)

    def endgame_screen(self):
        # End of game prompt
        window_surface.fill(self._status.COLORS["BLACK"])
        self.draw_text(
            "GAME OVER",
            window_surface,
            200,
            325,
            pygame.font.SysFont(None, 72, True),
        )
        # Restart game prompt
        self.draw_text(
            "Click anywhere to restart", window_surface, 170, 380
        )
        # Game stats prompt
        self.draw_text(
            "Accuracy: " + str(self._status.accuracy) + "%",
            window_surface,
            269,
            414,
        )
        self.draw_text(
            "Score: " + str(self._status.score), window_surface, 308, 450
        )
        pygame.display.update()

    def game_status(self):
        """ """
        # dsiplay game status to player
        self.draw_text(
            "Time: " + str(self._status.config[0]), window_surface, 8, 8
        )
        self.draw_text(
            "Score: " + str(self._status.score), window_surface, 8, 38
        )

    def display_targets(self):
        """ """
        for target in self._status.resize_target:
            window_surface.blit(self._status.resize_target, target)

    def start_screen(self):
        """
        """
        # Display difficulties
        for rect in difficultyRects:
            pygame.draw.rect(windowSurface, RED, rect)
            draw_text("Pick a difficulty",window_surface,90,150,pygame.font.SysFont(None, 112),color,)
            draw_text("Easy",window_surface,83,485,FONT,COLORS["BLACK"],)
            draw_text("Medium",window_surface,312,485,FONT,COLORS["BLACK"],)
            draw_text("Hard",window_surface,580,485,FONT,COLORS["BLACK"],)
