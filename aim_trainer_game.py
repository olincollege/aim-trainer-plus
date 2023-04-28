"""
Run and stop trainer
"""
import pygame, random, sys, os
from pygame.locals import *

from aim_trainer_range import AimTrainerRange
from aim_trainer_view import AimTrainerView
from aim_trainer_controller import AimTrainerController


def main():
    range = AimTrainerRange()
    view = AimTrainerView(range)
    controller = AimTrainerController(range)

    def Menu():
        """
        Prompts player for difficulty level
        """
        timer = 0
        color = range.COLORS["BLUE"]
        switch = False
        while True:
            range.windowSurface.fill(range.COLORS["BLACK"])
            difficultyRects = []
            difficultyRects.append(pygame.Rect(5, 450, 240, 100))
            difficultyRects.append(pygame.Rect(255, 450, 240, 100))
            difficultyRects.append(pygame.Rect(505, 450, 240, 100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminate()
                if event.type == MOUSEBUTTONDOWN:
                    if difficultyRects[0].collidepoint(pygame.mouse.get_pos()):
                        game("easy")
                    if difficultyRects[1].collidepoint(pygame.mouse.get_pos()):
                        game("medium")
                    if difficultyRects[2].collidepoint(pygame.mouse.get_pos()):
                        game("hard")
            for rect in difficultyRects:
                pygame.draw.rect(range.windowSurface, range.RED, rect)
            view.drawText(
                "Pick a difficulty",
                range.windowSurface,
                90,
                150,
                pygame.font.SysFont(None, 112),
                color,
            )
            view.drawText(
                "Easy",
                range.windowSurface,
                83,
                485,
                range.FONT,
                range.COLORS["BLACK"],
            )
            view.drawText(
                "Medium",
                range.windowSurface,
                312,
                485,
                range.FONT,
                range.COLORS["BLACK"],
            )
            view.drawText(
                "Hard",
                range.windowSurface,
                580,
                485,
                range.FONT,
                range.COLORS["BLACK"],
            )
            mainClock.tick(50)
            timer += 1
            if timer % 100 == 0:
                color = range.COLORS["BLUE"]
            elif timer % 50 == 0:
                color = range.COLORS["RED"]
            pygame.display.update()


if __name__ == "__main__":
    main.run()
