"""
Controller for Aim Trainer
"""
import pygame
from pygame.locals import *

class AimTrainerController:
    """
    Tracks and takes user input

    Attributes:
        _status: a instance
    """

    pygame.init()

    def __init__(self, status):
        """
        Saves instance of AimTrainerRange

        status: a instance of AimTrainerRange
        """
        self._status = status

    def event_detect(self, game_state):
        """
        Loops through pygame events checking for a event activation and then depending on game state calls needed function.

        Args:
            game_state: a string stating what part of the game the programs in
        """
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                #self.mouse_pos()
                #print('mouse')
                self._status.MOUSE_X = event.pos[0]
                self._status.MOUSE_Y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if game_state == "start":
                    #print('start')
                    self._status.populate_config(self.choose_difficulty())
                elif game_state == "range":
                    #print('range button clicked')
                    self._status.check_target_hit()
                elif game_state == "end":
                    #print("end")
                    return True
            if event.type == QUIT:
                self._status.terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self._status.terminate()


    def end_screen_check(self):
        """
        Checks to see if user wants to start another game by clicking on the screen

        Returns:
            a boolean dependent on choice
        """
        # check to see if player is trying to exit game
        return True

    def choose_difficulty(self):
        """
        Takes player choice on difficulty by logging if player clicks on a position occupied by the difficulty text

        Returns:
            a string stating a difficulty
        """
        # Check to see what difficulty player chose
        if self._status.difficulty_boxes()[0].collidepoint(
            pygame.mouse.get_pos()
        ):
            return "easy"
        if self._status.difficulty_boxes()[1].collidepoint(
            pygame.mouse.get_pos()
        ):
            return "medium"
        if self._status.difficulty_boxes()[2].collidepoint(
            pygame.mouse.get_pos()
        ):
            return "hard"

        return None

    def mouse_pos(self):
        """
        Saves mouse position when mouse is clicked
        """
        self._status.MOUSE_X = pygame.mouse.get_pos()[0]
        self._status.MOUSE_Y = pygame.mouse.get_pos()[1]

    def exit_program(self):
        """
        Checks if player is trying to escape or close game window and then closes it
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self._status.terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self._status.terminate()
