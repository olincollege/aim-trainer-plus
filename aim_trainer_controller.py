"""
Controller for Aim Trainer
"""
import pygame
from pygame_gui import UI_BUTTON_PRESSED


class AimTrainerController:
    """
    Tracks and takes user input

    Attributes:
        game_range: a instance
    """

    def __init__(self, status):
        """
        Saves instance of AimTrainerRange

        status: a instance of AimTrainerRange
        """
        self.game_range = status

    def event_detect(self, game_state, time_delta):
        """
        Loops through pygame events checking for a event activation and then
        depending on game state calls needed function.

        Args:
            game_state: a string stating what part of the game the programs in
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_range.terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_range.terminate()

            if game_state == "file":
                if (
                    event.type == pygame.USEREVENT
                    and event.user_type == UI_BUTTON_PRESSED
                ):
                    if (
                        event.ui_element
                        == self.game_range.file_picker.ok_button
                    ):
                        self.game_range.set_target(
                            self.game_range.file_picker.current_file_path
                        )
                self.game_range.manager.process_events(event)
                continue

            if event.type == pygame.MOUSEMOTION:
                self.game_range.mouse_x = event.pos[0]
                self.game_range.mouse_y = event.pos[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "start":
                     #print("start")
                    self.choose_difficulty()
                elif game_state == "range":
                    #print("Clicked")
                    self.game_range.check_target_hit()
                elif game_state == "end":
                    return True
            self.game_range.manager.process_events(event)
        self.game_range.manager.update(time_delta)

    def end_screen_check(self):
        """
        Checks to see if user wants to start another game by clicking on the
        screen

        Returns:
            a boolean dependent on choice
        """
        # check to see if player is trying to exit game
        return True

    def choose_difficulty(self):
        """
        Takes player choice on difficulty by logging if player clicks on a
        position occupied by the difficulty text

        Returns:
            a string stating a difficulty
        """
        # Check to see what difficulty player chose
        diff = None
        if self.game_range.difficulty_boxes()[0].collidepoint(
            pygame.mouse.get_pos()
        ):
            diff = "easy"
        if self.game_range.difficulty_boxes()[1].collidepoint(
            pygame.mouse.get_pos()
        ):
            diff = "medium"
        if self.game_range.difficulty_boxes()[2].collidepoint(
            pygame.mouse.get_pos()
        ):
            diff = "hard"

        if diff:
            self.game_range.populate_config(diff)

    def mouse_pos(self):
        """
        Saves mouse position when mouse is clicked
        """
        self.game_range.mouse_x = pygame.mouse.get_pos()[0]
        self.game_range.mouse_y = pygame.mouse.get_pos()[1]

    def exit_program(self):
        """
        Checks if player is trying to escape or close game window and then
        closes it
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_range.terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_range.terminate()
