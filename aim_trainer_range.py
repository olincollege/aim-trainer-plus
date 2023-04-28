"""
Window, colors, and targets and timer
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerRange:
    """
    Window for game and active elements.

    Attributes:
        BLACK: a tuple of ints that represent a RGBA code
        WHITE: a tuple of ints that represent a RGBA code
        RED: a tuple of ints that represent a RGBA code
        BLUE: a tuple of ints that represent a hex code
        WINDOWHEIGHT: a int being the number of pixels high the window will be
        WINDOWWIDTH: a int being the number of pixels wide the window will be
        FONT:
    """

    # Start and end pygame
    pygame.init()

    def terminate():
        """
        Closes Pygame
        """
        pygame.quit()
        sys.exit()

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
    main_clock = pygame.time.Clock()
    pygame.display.set_caption("sniper")

    # Game audio
    SHOOT_SOUND = pygame.mixer.Sound("snipersound.wav")
    HIT_SOUND = pygame.mixer.Sound("metalHit.wav")
    SHOOT_SOUND.set_volume(0.25)
    HIT_SOUND.set_volume(1)

    targets = []

    def __init__(self):
        """
        Clock and score
        """

    def populate_config(difficulty):
        """
        Resizes image based on difficulty selected. A harder difficulty generates a smaller image.

        Args:
            a string with the value of the difficulty

        Returns:
            a pixel array of the resized target
        """
        # Settings for difficulty. (time, amount of target, size of target)
        DIFFICULTY_SETTINGS = {
            "easy": (9, 2, 40),
            "medium": (6, 4, 30),
            "hard": (5, 5, 20),
        }
        # Takes imported image
        target_image = pygame.image.load("target.png")
        config = {}
        # Saves settings to config per difficulty
        if difficulty == "easy":
            config = DIFFICULTY_SETTINGS["easy"]
        elif difficulty == "medium":
            config = DIFFICULTY_SETTINGS["medium"]
        elif difficulty == "hard":
            config = DIFFICULTY_SETTINGS["hard"]

        # Scale image according to config
        target_image = pygame.transform.scale(
            target_image, (config[2], config[2])
        )
        return config

    def game(difficulty):
        config = populate_config(difficulty)

        pygame.mouse.set_visible(False)

        # Area which targets will be placed
        MOUSE_Y = round(WINDOW_HEIGHT / 2)
        MOUSE_X = round(WINDOW_WIDTH / 2)

        # Game variables
        tick_counter = 0
        targets = []
        amount_targets = 0
        score = 0
        FPS = 75
        hit_shots = 0
        total_shots = 0
        STARTING_TIME = config[0]
        CIRCLE_RADIUS = 150
        while True:
            # Monitor if game is over my watching time
            if config[0] <= 0:
                # end game and display player stats
                game_over(total_shots, hit_shots, difficulty, score)
            tick_counter += 1
            if tick_counter % FPS == 0:
                # game still going subtract from time
                config[0] -= 1
            # Player still has time, keep status white
            self.window_surface.fill(COLORS["WHITE"])

            # Detect that game hasnt started and sets initial parameters
            if amount_targets == 0:
                config[0] = STARTING_TIME
                while amount_targets != config[1]:
                    # Saves target positions for use
                    targets.append(
                        pygame.Rect(
                            (random.randint(0, WINDOW_WIDTH - config[2])),
                            (random.randint(0, WINDOW_HEIGHT - config[2])),
                            config[2],
                            config[2],
                        )
                    )
                    if (
                        targets[amount_targets].topleft[0] < 135
                        and targets[amount_targets].topleft[1] < 65
                    ):
                        targets.pop(amount_targets)
                    else:
                        amount_targets += 1
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    pass
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        terminate()
                if event.type == MOUSEMOTION:
                    MOUSE_X = event.pos[0]
                    MOUSE_Y = event.pos[1]
                if event.type == MOUSEBUTTONDOWN:
                    pygame.mixer.Channel(0).play(SHOOT_SOUND)
                    total_shots += 1
                    for target in targets[:]:
                        if (
                            MOUSE_X > target.topleft[0]
                            and MOUSE_X < target.bottomright[0]
                            and MOUSE_Y > target.topleft[1]
                            and MOUSE_Y < target.bottomright[1]
                        ):
                            pygame.mixer.Channel(1).play(HIT_SOUND)
                            targets.remove(target)
                            amount_targets -= 1
                            score += 1
                            hit_shots += 1

            pygame.draw.circle(
                window_surface,
                COLORS["WHITE"],
                (MOUSE_X, MOUSE_Y),
                CIRCLE_RADIUS,
                0,
            )
            for target in targets:
                window_surface.blit(target_image, target)
            pygame.draw.circle(
                window_surface,
                COLORS["BLACK"],
                (MOUSE_X, MOUSE_Y),
                CIRCLE_RADIUS + 1,
                3,
            )
            pygame.draw.line(
                window_surface,
                COLORS["BLACK"],
                (MOUSE_X, MOUSE_Y + 150),
                (MOUSE_X, MOUSE_Y - 150),
                2,
            )
            pygame.draw.line(
                window_surface,
                COLORS["BLACK"],
                (MOUSE_X + 150, MOUSE_Y),
                (MOUSE_X - 150, MOUSE_Y),
                2,
            )
            drawText("Time: " + str(config.get("time")), window_surface, 8, 8)
            drawText("Score: " + str(score), window_surface, 8, 38)
            pygame.display.update()
            main_clock.tick(FPS)
