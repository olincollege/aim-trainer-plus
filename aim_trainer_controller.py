"""
aim trainer controller
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerController:
    """ """

    def end_screen_check(self):
        """ """
        # check to see if player is trying to exit game
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                range.window_surface.fill(COLORS[WHITE])
                Menu()
            if event.type == KEYDOWN:
                terminate()

    def choose_difficulty(self):
        """ """
        # Check to see what difficulty player chose
        if pygame.event.type == MOUSEBUTTONDOWN:
            if difficulty_rects[0].collidepoint(pygame.mouse.get_pos()):
                return "easy"
            if difficulty_rects[1].collidepoint(pygame.mouse.get_pos()):
                return "medium"
            if difficulty_rects[2].collidepoint(pygame.mouse.get_pos()):
                return "hard"

    def check_target_hit(self):
        """ """
        # Check to see if mouse position overlaps with targets
        for target in targets[:]:
            # if target hit play hit sound, remove target, and add to score
            if (
                MOUSE_X > target.topleft[0]
                and MOUSE_X < target.bottomright[0]
                and MOUSE_Y > target.topleft[1]
                and MOUSE_Y < target.bottomright[1]
            ):
                targets.remove(target)
                amount_targets -= 1
                score += 1
                hit_shots += 1
