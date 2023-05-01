"""
Window, colors, and targets and timer
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerRange:
    """
    Target and Active Game Variables

    Attributes:
        config
        tick_counter
        targets
        amount_targets
        score
        FPS
        hit_shots
        total_shots
        STARTING_TIME
        CIRCLE_RADIUS

    """

    # Colors
    COLORS = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "BLUE": (0, 0, 255),
    }

    # Window Size
    WINDOW_HEIGHT = 750
    WINDOW_WIDTH = 750

    # Bounds for window
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # time
    main_clock = pygame.time.Clock()

    def __init__(self):
        """ """
        # Game variables
        self._config = []
        self._tick_counter = 0
        self._targets = []
        self._amount_targets = 0
        self._score = 0
        self.FPS = 75
        self._hit_shots = 0
        self._total_shots = 0
        # self._STARTING_TIME = self._config[0]
        self.CIRCLE_RADIUS = 150

    def config(self):
        """ """
        return self._config

    def targets(self):
        """ """
        return self._targets

    def score(self):
        """
        Return score of player

        Returns:
            a int being the score
        """
        return self._score

    def terminate():
        """ """
        pygame.quit()
        sys.exit()

    def difficulty_boxes(self):
        """ """
        difficulty_rects = []
        difficulty_rects.append(pygame.Rect(5, 450, 240, 100))
        difficulty_rects.append(pygame.Rect(255, 450, 240, 100))
        difficulty_rects.append(pygame.Rect(505, 450, 240, 100))
        return difficulty_rects

    def populate_config(self, difficulty):
        """
        Resizes image based on difficulty selected. A harder difficulty generates a smaller image.

        Args:
            a string representing the difficulty

        Returns:
            a pixel array of the resized target
        """
        # Settings for difficulty. (time, amount of target, size of target)
        DIFFICULTY_SETTINGS = {
            "easy": [9, 2, 40],
            "medium": [6, 4, 30],
            "hard": [5, 5, 20],
        }
        # Saves settings to config per difficulty
        if difficulty == "easy":
            self._config = DIFFICULTY_SETTINGS["easy"]
        elif difficulty == "medium":
            self._config = DIFFICULTY_SETTINGS["medium"]
        elif difficulty == "hard":
            self._config = DIFFICULTY_SETTINGS["hard"]
        return self._config

    def resize_target(self):
        """ """
        # Takes imported image
        target_image = pygame.image.load("target.png")
        # Scale image according to config
        target_image = pygame.transform.scale(
            target_image, (self._config[2], self._config[2])
        )
        return target_image

    def generate_targets(self):
        """
        Generate random placement of targets and add those cords to a list
        """
        self._targets.append(
            pygame.Rect(
                (random.randint(0, self.WINDOW_WIDTH - self._config[2])),
                (random.randint(0, self.WINDOW_HEIGHT - self._config[2])),
                self._config[2],
                self._config[2],
            )
        )

    def check_valid_target(self):
        """
        Check to see if target is in bound if is remove target from list and if not add to target counter
        """
        if (
            self._targets[self._amount_targets].topleft[0] < 135
            and self._targets[self._amount_targets].topleft[1] < 65
        ):
            self._targets.pop(self._amount_targets)
        else:
            self._amount_targets += 1

    def time_actions(self):
        """
        Check time to see whether time is up or not. If times up, play game over function. If not subtract time from clock
        """
        # Monitor if game is over my watching time
        if self._config[0] <= 0:
            # end game and display player stats
            return False
        self.tick_counter += 1

        if self._tick_counter % self.FPS == 0:
            # game still going subtract from time
            self._config[0] -= 1
        return True

    def accuracy(self):
        """
        Calculates accuracy

        Returns:
            accuracy: a int being accuracy
        """
        # Calculate score
        if self._totalShots != 0 and self._hitShots != 0:
            accuracy = round(self._hitShots / self._totalShots * 100)
        else:
            accuracy = 0

        return accuracy
