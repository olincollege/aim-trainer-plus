"""
Aim Trainer Text Prompts
"""
from abc import ABC, abstractclassmethod

class AimTrainerView(ABC):
    """
    Opens window for game and prompts user text.

    Attributes:
    
    """

    def __init__(self)
        
    def drawText(text, surface, x, y, font=FONT, color=RED):
        textObject = font.render(text, 1, color)
        textRect = textObject.get_rect()
        textRect.topleft = (x, y)
        surface.blit(textObject, textRect)

