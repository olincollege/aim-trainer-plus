"""
Module for Aim Trainer
"""
import random
import pygame

class AimTrainerRange:
    """
    aim trainer functions that handle data

    Attributes:
        COLORS: a dict with a string key indicating a color mapped to a tuple
        of ints representing a RGBa code
        WINDOW_HEIGHT: a int representing the amount of pixels wanted for height
        WINDOW_WIDTH: a int representing the amount of pixels wanted for width
        window_surface: a function that displays a window with given height and
        width
        main_clock: an object that helps track time
        _config: a list containing ints that determine game difficulty settings
        _tick_counter: a int of the time gone by in milliseconds
        _targets: a list containing cords for upcoming target spawn
        _amount_targets: a int indicating the amount of valid targets in play
        _score: a int indicating the score of the player
        fps: a int indicating the FPS the game is being played at
        _hit_shots: a int indicating the amount of shots that hit a target
        _total_shots: a int indicating the amount of shots taken
        mouse_x: a int for the starting position of the mouse on the x axis
        mouse_y: a int for the starting position of the mouse on the y axis

    """

    # Colors
    COLORS = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "BLUE": (0, 0, 255),
    }

    # Window Size
    # WINDOW_HEIGHT = 768
    # WINDOW_WIDTH = 1366
    WINDOW_HEIGHT = 750
    WINDOW_WIDTH = 750

    # Bounds for window

    # time

    def __init__(self):
        """
        Sets starting variables
        """
        self.window_surface = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        )
        # Game variables
        self._config = []
        self._tick_counter = 0
        self._targets = []
        self._amount_targets = 0
        self._score = 0
        self.fps = 60
        self._hit_shots = 0
        self._total_shots = 0
        self._target_image = None
        # Mouse position
        self.mouse_x = round(self.WINDOW_HEIGHT / 2)
        self.mouse_y = round(self.WINDOW_WIDTH / 2)
        self.MOUSE_Y = round(self.WINDOW_HEIGHT / 2)
        self.MOUSE_X = round(self.WINDOW_WIDTH / 2)
        self.file_picker = None
        self.manager = None

    @property
    def target_image(self):
        return self._target_image

    def config(self):
        """
        Returns:
            a list of ints being difficulty settings
        """
        return self._config

    def targets(self):
        """
        Returns:
            targets: a list of ints being future target spawn cords
        """
        return self._targets

    def score(self):
        """
        Returns:
            a int being the score
        """
        return self._score

    def terminate(self):
        """
        Ends Pygame
        """
        pygame.quit()
        sys.exit()

    def difficulty_boxes(self):
        """
        Generates box placement cords for difficulty text to be placed on

        Returns:
            a list of tuples containing ints which are cords/dim for boxes
        """
        difficulty_rects = []
        difficulty_rects.append(pygame.Rect(5, 450, 240, 100))
        difficulty_rects.append(pygame.Rect(255, 450, 240, 100))
        difficulty_rects.append(pygame.Rect(505, 450, 240, 100))
        return difficulty_rects

    def populate_config(self, difficulty):
        """
        Determine which settings will be used for game based off difficulty
        selected

        Args:
            a string representing the difficulty

        Returns:
            a list containing ints that determine game difficulty settings
        """
        # Settings for difficulty. (time, amount of target, size of target)
        difficulty_settings = {
            "easy": [15, 5, 60],
            "medium": [15, 5, 40],
            "hard": [15, 5, 20],
        }
        # Saves settings to config per difficulty
        if difficulty == "easy":
            self._config = difficulty_settings["easy"]
        elif difficulty == "medium":
            self._config = difficulty_settings["medium"]
        elif difficulty == "hard":
            self._config = difficulty_settings["hard"]
        return self._config

    def set_target(self, path):
        """
        Args:
        path (str): path to target image
        """
        img = pygame.image.load(path)
        self._target_image = pygame.transform.scale(
            img, (self._config[2], self._config[2])
        )

    def generate_targets(self):
        """
        Generate random placement of targets and add those cords to a list
        """
        if len(self._targets) < self._config[1]:
            target_cords = pygame.Rect(
                (random.randint(0, self.WINDOW_WIDTH - self._config[2])),
                (random.randint(0, self.WINDOW_HEIGHT - self._config[2])),
                self._config[2],
                self._config[2],
            )
            # print("TARGET COORDS: ", target_cords)
            if self.check_valid_target(target_cords):
                self._targets.append(target_cords)

    def check_valid_target(self, target_cords):
        """
        Check to see if target is in bound if is remove target from list and if
        not add to target counter
        """
        if target_cords.topleft[0] < 135 and target_cords.topleft[1] < 65:
            return False
        return True

    def check_target_hit(self):
        """
        Check to see if mouse position is the same as a target. If so remove
        target from scree, subtract from amount of visible targets, add to
        score, and add to hit count
        """
        # Check to see if mouse position overlaps with targets
        #print('check target function')
        for target in self._targets[:]:
            #print(self.mouse_x)
            #print(self.mouse_y)
            #print(target.topleft[0],target.topleft[1])
            #print(target.bottomright[0],target.bottomright[1])
            #print('checking')
            # if target hit play hit sound, remove target, and add to score
            if (
                self.mouse_x > target.topleft[0]
                and self.mouse_x < target.bottomright[0]
                and self.mouse_y > target.topleft[1]
                and self.mouse_y < target.bottomright[1]
            ):
                # print('should remove target')
                print("should remove target")
                self._targets.remove(target)
                # self._amount_targets -= 1
                self._score += 1
                self._hit_shots += 1
        self._total_shots += 1

    def time_actions(self):
        """
        Check time to see whether time is up or not. If times up, return False.
        If not subtract time from clock and return True

        Returns:
            a boolean determining if the game should continue or not
        """
        # Monitor if game is over my watching time
        if self._config[0] <= 0:
            # end game and display player stats
            return False
        self._tick_counter += 1

        if self._tick_counter % self.fps == 0:
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
        # print(self._total_shots)
        # print(self._total_shots)
        if self._total_shots != 0 and self._hit_shots != 0:
            accuracy = round(self._hit_shots / self._total_shots * 100)
        else:
            accuracy = 0

        return accuracy
