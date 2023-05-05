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

    clock = view.game_clock
    # Start screen
    start = False
    while start == False:
        time_delta = clock.tick(60) / 1000.0
        controller.event_detect("start", time_delta)
        view.start_screen()
        pygame.display.update()
        if range.config() != []:
            # ask for file
            pygame.event.pump()
            start = True

    # range.set_target("target.png")
    while range.target_image is None:
        time_delta = clock.tick(60) / 1000.0
        controller.event_detect("file", time_delta)
        view.display_picker()

    # game
    while start is True:
        time_delta = clock.tick(60) / 1000.0
        view.game_background()
        view.game_status()
        range.generate_targets()
        # range.check_valid_target()
        view.display_targets()
        controller.event_detect("range", time_delta)
        # range.check_target_hit()
        start = range.time_actions()
        pygame.display.update()

    # end screen
    # print("end function")
    while start is False:
        time_delta = clock.tick(60) / 1000.0
        # print("end screen")
        view.endgame_screen()
        if controller.event_detect("end", time_delta):
            # print("repeat game")
            main()
            return
        pygame.display.update()


if __name__ == "__main__":
    main()
