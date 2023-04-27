"""
Run and stop trainer
"""
import pygame, random, sys, os
from pygame.locals import *

from aim_trainer_range import AimTrainerRange
from aim_trainer_view import AimTrainerView
from aim_trainer_controller import

def main():

    range = AimTrainerRange()
    view = AimTrainerView()

    pygame.init()

    def terminate():
        pygame.quit()
        sys.exit()

    def gameOver(totalShots, hitShots, difficulty, score):
        pygame.mouse.set_visible(True)
        if totalShots != 0 and hitShots != 0:
            accuracy = round(hitShots/totalShots * 100)
        else:
            accuracy = 0
        range.windowSurface.fill(BLACK)
        view.drawText("GAME OVER", range.windowSurface, 200, 325, pygame.font.SysFont(None, 72, True))
        view.drawText("Click anywhere to restart", range.windowSurface, 170, 380)
        view.drawText("Accuracy: " + str(accuracy) + "%", range.windowSurface, 269, 414)
        view.drawText("Score: " + str(score), range.windowSurface, 308, 450)
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

if __name__ == '__main__':
    main.run()