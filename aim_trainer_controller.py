"""
aim trainer controller
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerController:
    """ """

    pygame.init()

    def __init__(self, status):
        """ """
        self._status = status
        # Mouse position
        self._MOUSE_Y = round(self._status.WINDOW_HEIGHT / 2)
        self._MOUSE_X = round(self._status.WINDOW_WIDTH / 2)

    def end_screen_check(self):
        """ """
        # check to see if player is trying to exit game
        if pygame.event == QUIT:
            self._status.terminate()
        if pygame.event == MOUSEBUTTONDOWN:
            return True
        if pygame.event == KEYDOWN:
            self._status.terminate()

    def choose_difficulty(self):
        """ """
        # Check to see what difficulty player chose
        if pygame.event == MOUSEBUTTONDOWN:
            if self._status.difficulty_boxes[0].collidepoint(
                pygame.mouse.get_pos()
            ):
                return "easy"
            if self._status.difficulty_boxes[1].collidepoint(
                pygame.mouse.get_pos()
            ):
                return "medium"
            if self._status.difficulty_boxes[2].collidepoint(
                pygame.mouse.get_pos()
            ):
                return "hard"

    def check_target_hit(self):
        """ """
        # Check to see if mouse position overlaps with targets
        for target in self._status.targets[:]:
            # if target hit play hit sound, remove target, and add to score
            if (
                self._MOUSE_X > target.topleft[0]
                and self._MOUSE_X < target.bottomright[0]
                and self._MOUSE_Y > target.topleft[1]
                and self._MOUSE_Y < target.bottomright[1]
            ):
                self._status.targets.remove(target)
                amount_targets -= 1
                score += 1
                hit_shots += 1

    def exit_program(self):
        """ """
        if pygame.event == QUIT:
            self._status.terminate()
        if pygame.event == KEYDOWN:
            if pygame.event.key == K_ESCAPE:
                self._status.terminate()
