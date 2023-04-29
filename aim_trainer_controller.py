"""
aim trainer controller
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerController:
    """ """

    for event in pygame.event.get():
        # Check to see if plauer wants to end game
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()

        # Check to see what difficulty player chose
        if event.type == MOUSEBUTTONDOWN:
            if difficultyRects[0].collidepoint(pygame.mouse.get_pos()):
                game("easy")

            if difficultyRects[1].collidepoint(pygame.mouse.get_pos()):
                game("medium")

            if difficultyRects[2].collidepoint(pygame.mouse.get_pos()):
                game("hard")

        # Indicate chose made with box
        for rect in difficultyRects:
            pygame.draw.rect(windowSurface, RED, rect)

        # Prompt user to pick difficulty
        drawText(
            "Pick a difficulty",
            windowSurface,
            90,
            150,
            pygame.font.SysFont(None, 112),
            color,
        )
        # Display difficulties
        drawText("Easy", windowSurface, 83, 485, FONT, BLACK)
        drawText("Medium", windowSurface, 312, 485, FONT, BLACK)
        drawText("Hard", windowSurface, 580, 485, FONT, BLACK)
