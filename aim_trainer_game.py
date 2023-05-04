"""
Compiles aim trainer mvc files.
"""
import pygame
from pygame.locals import *

from aim_trainer_range import AimTrainerRange
from aim_trainer_view import AimTrainerView
from aim_trainer_controller import AimTrainerController


def main():
    """
    Runs aim trainer
    """
    pygame.init()

    range = AimTrainerRange()
    view = AimTrainerView(range)
    controller = AimTrainerController(range)

    # Start screen
    start = False
    while start == False:
        view.start_screen()
        controller.event_detect("start")
        if range.config() != []:
            start = True
        pygame.display.update()

    # game
    while start == True:
        view.game_background()
        view.game_status()
        range.generate_targets()
        # range.check_valid_target()
        view.display_targets()
        controller.event_detect("range")
        #range.check_target_hit()
        start = range.time_actions()
        pygame.display.update()

    # end screen
    #print("end function")
    while start == False:
        #print("end screen")
        view.endgame_screen()
        if controller.event_detect("end"):
            #print("repeat game")
            main()
            return
        pygame.display.update()


if __name__ == "__main__":
    main()
