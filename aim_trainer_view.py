"""
View for Aim Trainer
"""
import pygame
from pygame.locals import *


class AimTrainerView:
    """
    Prompts text and images for aim trainer

    FONT: a method which sets text parameters
    start_bg_raw: a image
    end_bg_raw: a image
    range_bg_raw: a image
    _status: a instance of AimTrainerRange
    _start_bg: a reformated image
    _end_bg: a reformated image
    _range_bg: a reformated image
    """

    pygame.init()

    FONT = pygame.font.Font('cs_regular.ttf', 48)

    start_bg_raw = pygame.image.load("range-start.png")
    end_bg_raw = pygame.image.load("range-end.png")
    range_bg_raw = pygame.image.load("range2.png")

    def __init__(self, status):
        """
        Args:
            status: a instance of AimTrainerRange
        """
        self._status = status
        self._start_bg = pygame.transform.scale(
            self.start_bg_raw,
            (self._status.WINDOW_WIDTH, self._status.WINDOW_HEIGHT),
        )
        self._end_bg = pygame.transform.scale(
            self.end_bg_raw,
            (self._status.WINDOW_WIDTH, self._status.WINDOW_HEIGHT),
        )
        self._range_bg = pygame.transform.scale(
            self.range_bg_raw,
            (self._status.WINDOW_WIDTH, self._status.WINDOW_HEIGHT),
        )

    def draw_text(
        self,
        text,
        surface,
        x,
        y,
        font=None,
        color=None,
    ):
        """
        Displays text on screen
        """
        if font is None:
            font = self.FONT
        if color is None:
            color = self._status.COLORS["RED"]
        # Load text
        text_object = font.render(text, 1, color)
        # get area of text
        text_rect = text_object.get_rect()
        # align text
        text_rect.topleft = (x, y)
        # display on surface
        surface.blit(text_object, text_rect)

    def endgame_screen(self):
        """
        Endgame text and final status and prompts user of next steps
        """
        self._status.window_surface.blit(self._end_bg, (0, 0))
        # End of game prompt
        self.draw_text(
            "GAME OVER",
            self._status.window_surface,
            200,
            325,
            pygame.font.SysFont('cs_regular.ttf', 72, True),
        )
        # Restart game prompt
        self.draw_text(
            "Click anywhere to restart", self._status.window_surface, 170, 380
        )
        # Game stats prompt
        self.draw_text(
            "Accuracy: " + str(self._status.accuracy()) + "%",
            self._status.window_surface,
            269,
            414,
        )
        self.draw_text(
            "Score: " + str(self._status.score()),
            self._status.window_surface,
            308,
            450,
        )
        pygame.display.update()

    def game_status(self):
        """
        Display time and and score of ongoing game
        """
        #print("CONFIG: ", self._status.config())

        # display game status to player
        self.draw_text(
            "Time: " + str(self._status.config()[0]),
            self._status.window_surface,
            8,
            8,
        )
        self.draw_text(
            "Score: " + str(self._status.score()),
            self._status.window_surface,
            8,
            38,
        )

    def display_targets(self):
        """
        Spawn targets in cords of pre-made list
        """
        for target in self._status.targets():
            #print(self._status.resize_target(), target)
            self._status.window_surface.blit(
                self._status.resize_target(), target
            )

    def game_background(self):
        """
        Set background to range image
        """
        self._status.window_surface.blit(self._range_bg, (0, 0))

    def start_screen(self):
        """
        Display text to pick difficulty alongside the different difficulty levels all in pre-made boxes
        """
        self._status.window_surface.blit(self._start_bg, (0, 0))
        # Display difficulties
        for rect in self._status.difficulty_boxes():
            pygame.draw.rect(
                self._status.window_surface, self._status.COLORS["RED"], rect
            )
            self.draw_text(
                "Pick a difficulty",
                self._status.window_surface,
                90,
                150,
                pygame.font.SysFont('cs_regular.ttf', 112),
            )
            self.draw_text(
                "Easy",
                self._status.window_surface,
                83,
                485,
                self.FONT,
                self._status.COLORS["BLACK"],
            )
            self.draw_text(
                "Medium",
                self._status.window_surface,
                312,
                485,
                self.FONT,
                self._status.COLORS["BLACK"],
            )
            self.draw_text(
                "Hard",
                self._status.window_surface,
                580,
                485,
                self.FONT,
                self._status.COLORS["BLACK"],
            )
