"""
Aim Trainer Text Prompts
"""
from aim_trainer_range import AimTrainerRange

window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


def drawText(text, surface, x, y, font=FONT, color=RED):
    textObject = font.render(text, 1, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)
