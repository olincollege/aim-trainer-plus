"""
Run and stop trainer
"""
import pygame, random, sys, os
from pygame.locals import *

from aim_trainer_range import AimTrainerRange
from aim_trainer_view import AimTrainerView
from aim_trainer_controller import AimTrainerController


def main():
    """ """
    pygame.init()

    range = AimTrainerRange()
    view = AimTrainerView(range)
    controller = AimTrainerController(range)

    # Start screen
    start = False
    while start == False:
        controller.exit_program()
        view.start_screen()
        range.populate_config(controller.choose_difficulty())
        if range.config != []:
            start = True
        pygame.display.update()

    # game
    while start == True:
        controller.exit_program()
        view.game_background()
        view.game_status()
        view.display_targets()
        controller.check_target_hit()
        start = range.time_actions()
        pygame.display.update()

    # end screen
    view.endgame_screen
    if controller.end_screen_check():
        main()
    pygame.display.update()


if __name__ == "__main__":
    main()
