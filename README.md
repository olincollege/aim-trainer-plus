# Aim Trainer

## Description
Aim Trainer spawns targets randomly around the for the player to click on. The more targets you click, the higher your score. Accuracy is tracked, so randomly clicking will hurt both your accuracy and score. There are three difficulties to choose from, which determine the number of targets spawned at once and the size of the targets. Once the program is initialized, the player can continue to replay the game without needing to rerun the program. The player can exit the program at any time using ESCAPE or QUIT. Another fun feature is the user ability to select their own target image. The user will be prompted to choose a file after choosing the difficulty.

## Requirements
To install required packages and libraries: 'pip install -r requirements.txt'

## How to Play
1. Run 'python aim_trainer_game.py'
2. Select difficulty
3. From the file menu choose desired PNG from root of rep
4. Click on targets
5. When time is up click on end screen to restart
6. Exit or Escape out at any time

## Using Custom Images
Four images are provides to you to use.
- target.png
- silhouette.png
- trump.png
- alien.png

If you want to use your own image you have to add it to the root of repo. While it appears you can use any file on your device, the program will not allow this due to privacy settings.

## Notes
Unit tests not added for controller.py and view.py as they could not be implemented reasonably
