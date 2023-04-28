"""
Window, colors, and targets and timer
"""
import pygame, random, sys, os
from pygame.locals import *


class AimTrainerRange:
    """
    Window for game and active elements.

    Attributes:
        BLACK: a tuple of ints that represent a hex code
        WHITE: a tuple of ints that represent a hex code
        RED: a tuple of ints that represent a hex code
        BLUE: a tuple of ints that represent a hex code
        WINDOWHEIGHT: a int being the number of pixels high the window will be
        WINDOWWIDTH: a int being the number of pixels wide the window will be
        FONT:
    """

    # Colors

    COLORS = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "BLUE": (0, 0, 255),
    }

    # Window Size
    WINDOWHEIGHT = 750
    WINDOWWIDTH = 750

    FONT = pygame.font.SysFont(cs_regular.ttf, 48)

    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("sniper")

    shootSound = pygame.mixer.Sound("snipersound.wav")
    hitSound = pygame.mixer.Sound("metalHit.wav")
    shootSound.set_volume(0.25)
    hitSound.set_volume(1)

    targets = []

    def __init__(self):
        """
        Clock and score
        """
        self._clock = pygame.time.Clock()
        # self._hits =

    def populateConfig(difficulty):
        """
        Resizes image based on difficulty selected. A harder difficulty generates a smaller image.

        Args:
            a string with the value of the difficulty

        Returns:
            a pixel array of the resized target
        """
        global targetImage
        targetImage = pygame.image.load("target.png")
        config = {}
        if difficulty == "easy":
            difficultyFile = open("easy.txt", "r")
        elif difficulty == "medium":
            difficultyFile = open("medium.txt", "r")
        elif difficulty == "hard":
            difficultyFile = open("hard.txt", "r")
        for line in difficultyFile:
            splitLine = line.split(":")
            splitLine[1] = splitLine[1].strip("\n")
            config[splitLine[0]] = int(splitLine[1])
        targetImage = pygame.transform.scale(
            targetImage, (config["enemySize"], config["enemySize"])
        )
        difficultyFile.close()
        return config

    def game(difficulty):
        config = populateConfig(difficulty)

        pygame.mouse.set_visible(False)

        mouseY = round(WINDOWHEIGHT / 2)
        mouseX = round(WINDOWWIDTH / 2)

        tickCounter = 0
        enemies = []
        amountOfEnemies = 0
        score = 0
        FPS = 75
        hitShots = 0
        totalShots = 0
        STARTINGTIME = config.get("time")
        CIRCLERADIUS = 150
        while True:
            if config.get("time") <= 0:
                gameOver(totalShots, hitShots, difficulty, score)
            tickCounter += 1
            if tickCounter % FPS == 0:
                config["time"] -= 1
            self.windowSurface.fill(COLORS["WHITE"])

            if amountOfEnemies == 0:
                config["time"] = STARTINGTIME
                while amountOfEnemies != config.get("maxAmountOfEnemies"):
                    enemies.append(
                        pygame.Rect(
                            (
                                random.randint(
                                    0, WINDOWWIDTH - config.get("enemySize")
                                )
                            ),
                            (
                                random.randint(
                                    0, WINDOWHEIGHT - config.get("enemySize")
                                )
                            ),
                            config.get("enemySize"),
                            config.get("enemySize"),
                        )
                    )
                    if (
                        enemies[amountOfEnemies].topleft[0] < 135
                        and enemies[amountOfEnemies].topleft[1] < 65
                    ):
                        enemies.pop(amountOfEnemies)
                    else:
                        amountOfEnemies += 1
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    pass
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        terminate()
                if event.type == MOUSEMOTION:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                if event.type == MOUSEBUTTONDOWN:
                    pygame.mixer.Channel(0).play(shootSound)
                    totalShots += 1
                    for enemy in enemies[:]:
                        if (
                            mouseX > enemy.topleft[0]
                            and mouseX < enemy.bottomright[0]
                            and mouseY > enemy.topleft[1]
                            and mouseY < enemy.bottomright[1]
                        ):
                            pygame.mixer.Channel(1).play(hitSound)
                            enemies.remove(enemy)
                            amountOfEnemies -= 1
                            score += 1
                            hitShots += 1

            pygame.draw.circle(
                windowSurface,
                COLORS["WHITE"],
                (mouseX, mouseY),
                CIRCLERADIUS,
                0,
            )
            for enemy in enemies:
                windowSurface.blit(targetImage, enemy)
            pygame.draw.circle(
                windowSurface,
                COLORS["BLACK"],
                (mouseX, mouseY),
                CIRCLERADIUS + 1,
                3,
            )
            pygame.draw.line(
                windowSurface,
                self.COLORS["BLACK"],
                (mouseX, mouseY + 150),
                (mouseX, mouseY - 150),
                2,
            )
            pygame.draw.line(
                windowSurface,
                self.COLORS["BLACK"],
                (mouseX + 150, mouseY),
                (mouseX - 150, mouseY),
                2,
            )
            drawText("Time: " + str(config.get("time")), windowSurface, 8, 8)
            drawText("Score: " + str(score), windowSurface, 8, 38)
            pygame.display.update()
            mainClock.tick(FPS)
