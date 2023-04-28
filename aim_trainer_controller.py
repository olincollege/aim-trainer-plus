"""
aim trainer controller
"""


class AimTrainerController:
    """ """

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()

        if event.type == MOUSEBUTTONDOWN:
            if difficultyRects[0].collidepoint(pygame.mouse.get_pos()):
                game("easy")

            if difficultyRects[1].collidepoint(pygame.mouse.get_pos()):
                game("medium")

            if difficultyRects[2].collidepoint(pygame.mouse.get_pos()):
                game("hard")

        for rect in difficultyRects:
            pygame.draw.rect(windowSurface, RED, rect)

        drawText(
            "Pick a difficulty",
            windowSurface,
            90,
            150,
            pygame.font.SysFont(None, 112),
            color,
        )
        drawText("Easy", windowSurface, 83, 485, FONT, BLACK)
        drawText("Medium", windowSurface, 312, 485, FONT, BLACK)
        drawText("Hard", windowSurface, 580, 485, FONT, BLACK)
