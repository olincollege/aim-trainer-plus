def populateConfig(self, difficulty):
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

    if self.difficulty == "easy":
        difficultyFile = open("easy.txt", "r")

    elif self.difficulty == "medium":
        difficultyFile = open("medium.txt", "r")

    elif self.difficulty == "hard":
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
