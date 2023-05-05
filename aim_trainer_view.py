"""
View for Aim Trainer
"""
from typing import TYPE_CHECKING
import pygame
import pygame_gui

if TYPE_CHECKING:
    from aim_trainer_range import AimTrainerRange


class AimTrainerView:
    """
    Prompts text and images for aim trainer

    font: a method which sets text parameters
    game_clock: a method which is used to track time
    start_bg_raw: a image
    end_bg_raw: a image
    range_bg_raw: a image
    _status: a instance of AimTrainerRange
    _start_bg: a reformated image
    _end_bg: a reformated image
    _range_bg: a reformated image
    """

    pygame.init()

    font = pygame.font.Font("cs_regular.ttf", 48)

    game_clock = pygame.time.Clock()

    #Import Backgrounds
    start_bg_raw = pygame.image.load("range-start.png")
    end_bg_raw = pygame.image.load("range-end.png")
    range_bg_raw = pygame.image.load("range2.png")

    def __init__(self, status):
        """
        Args:
            status: a instance of AimTrainerRange
        """
        self._status = status

        #File Search Code
        self.manager = pygame_gui.UIManager(
            (self._status.WINDOW_WIDTH, self._status.WINDOW_HEIGHT)
        )
        rect = pygame.Rect(
            (0, 0), (self._status.WINDOW_WIDTH / 2, self._status.WINDOW_HEIGHT / 2)
        )
        rect.center = self._status.WINDOW_WIDTH / 2, self._status.WINDOW_HEIGHT / 2
        self.file_picker = pygame_gui.windows.UIFileDialog(
            rect=rect,
            manager=self.manager,
            window_title="Select Target",
        )
        status.manager = self.manager
        status.file_picker = self.file_picker

        #Reformate Background images
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
        x_axis,
        y_axis,
        font=None,
        color=None,
    ):
        """
        Displays text on screen
        """
        if font is None:
            font = self.font
        if color is None:
            color = self._status.COLORS["WHITE"]
        # Load text
        text_object = font.render(text, 1, color)
        # Loaded text outline
        text_object_outline = font.render(text, 1, self._status.COLORS["BLACK"])
        
        # Create a new surface for the final text with a stroke
        text_stroke = pygame.Surface(
            (text_object.get_width() + 4, text_object.get_height() + 4),
            pygame.SRCALPHA,
        )
        # Blit the white text surface with a slight offset to create the stroke
        # effect
        text_stroke.blit(text_object_outline, (2, 2))
        # Blit the black text surface onto the final text surface
        text_stroke.blit(text_object, (0, 0))

        # get area of text
        text_rect = text_object.get_rect()
        # align text
        text_rect.topleft = (x_axis, y_axis)

        # display on surface
        surface.blit(text_stroke, text_rect)

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
            pygame.font.Font("cs_regular.ttf", 72),
        )
        # Restart game prompt
        self.draw_text(
            "Click anywhere to restart",
            self._status.window_surface,
            100,
            380,
            None,
            self._status.COLORS["WHITE"],
        )
        # Game stats prompt
        self.draw_text(
            "Accuracy: " + str(self._status.accuracy()) + "%",
            self._status.window_surface,
            269,
            414,
            None,
            self._status.COLORS["WHITE"],
        )
        self.draw_text(
            "Score: " + str(self._status.score()),
            self._status.window_surface,
            308,
            450,
            None,
            self._status.COLORS["WHITE"],
        )
        pygame.display.update()

    def display_picker(self):
        """
        Display file input dialog
        """
        self._status.window_surface.blit(self._end_bg, (0, 0))
        self.manager.draw_ui(self._status.window_surface)
        pygame.display.update()

    def game_status(self):
        """
        Display time and and score of ongoing game
        """
        # print("CONFIG: ", self._status.config())

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
            # print(self._status.resize_target(), target)
            self._status.window_surface.blit(self._status.target_image, target)
            # self._status.window_surface.blit(
            #     self._status.resize_target(), target
            # )

    def game_background(self):
        """
        Set background to range image
        """
        self._status.window_surface.blit(self._range_bg, (0, 0))

    def start_screen(self):
        """
        Display text to pick difficulty alongside the different difficulty
        levels all in pre-made boxes
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
                pygame.font.Font("cs_regular.ttf", 80),
            )
            self.draw_text(
                "Easy",
                self._status.window_surface,
                83,
                485,
                self.font,
                self._status.COLORS["WHITE"],
            )
            self.draw_text(
                "Medium",
                self._status.window_surface,
                312,
                485,
                self.font,
                self._status.COLORS["WHITE"],
            )
            self.draw_text(
                "Hard",
                self._status.window_surface,
                580,
                485,
                self.font,
                self._status.COLORS["WHITE"],
            )
