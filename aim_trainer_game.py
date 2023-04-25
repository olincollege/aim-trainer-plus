"""
Run and stop trainer
"""
from aim_trainer_range import AimTrainerRange
from aim_trainer_view import
from aim_trainer_controller import

pygame.init()

def terminate():
    pygame.quit()
    sys.exit()

def main():
    window((WINDOWWIDTH, WINDOWHEIGHT))