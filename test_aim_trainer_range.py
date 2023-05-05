"""
Unit tests for aim trainer range
"""
import pytest

from aim_trainer_range import AimTrainerRange

#Difficulty Boxes
def test_difficulty_boxes_amount():
    """
    Check that correct amount of boxes are added to list
    """
    game_range = AimTrainerRange()
    assert len(game_range.difficulty_boxes()) == 3


def test_difficulty_boxes_content():
    """
    Check that content of difficulty boxes list contains proper cords.
    """
    game_range = AimTrainerRange()
    assert game_range.difficulty_boxes() == [
        (5, 450, 240, 100),
        (255, 450, 240, 100),
        (505, 450, 240, 100),
    ]

#Populate Config
def test_populate_config_easy():
    """
    Check that populate config returns proper list settings for difficulty
    """
    game_range = AimTrainerRange()
    assert game_range.populate_config("easy") == [15, 5, 60]


def test_populate_config_medium():
    """
    Check that populate config returns proper list settings for difficulty
    """
    game_range = AimTrainerRange()
    assert game_range.populate_config("medium") == [15, 5, 40]


def test_populate_config_hard():
    """
    Check that populate config returns proper list settings for difficulty
    """
    game_range = AimTrainerRange()
    assert game_range.populate_config("hard") == [15, 5, 20]


def test_populate_config_empty():
    """
    Check that populate config returns a empty list if None is given
    """
    game_range = AimTrainerRange()
    assert game_range.populate_config(None) == []

#Generate Targets
def test_generate_targets_max():
    """
    Check to see that no more targets are generated when max is met
    """
    range_game = AimTrainerRange()

    range_game._config = [10, 5, 20]
    range_game._targets = [1, 2, 3, 4, 5]
    range_game.generate_targets()
    assert len(range_game._targets) == 5

def test_generate_targets_needed():
    """
    Check to see that targets are added if needed
    """
    range_game = AimTrainerRange()

    range_game._config = [10, 5, 20]
    range_game._targets = [1, 2, 3]
    range_game.generate_targets()
    assert len(range_game._targets) == 4

#Time Actions
def test_time_actions_time_out():
    """
    Check that if time is out returns false
    """
    range_game = AimTrainerRange()
    range_game._config.append(0)
    assert range_game.time_actions() is False


def test_time_actions_time_left():
    """
    Check that if time is left returns True
    """
    range_game = AimTrainerRange()
    range_game._config.append(5)
    assert range_game.time_actions() is True

#Accuracy
def test_accuracy_0_shots():
    """
    Check that accuracy is 0 if no shots are taken
    """
    range_game = AimTrainerRange()
    range_game._total_shots = 0
    range_game._hit_shots = 0
    assert range_game.accuracy() == 0


def test_accuracy_0_accuracy():
    """
    Check that accuracy is 0 if no hits are made
    """
    range_game = AimTrainerRange()
    range_game._total_shots = 5
    range_game._hit_shots = 0
    assert range_game.accuracy() == 0


def test_accuracy_100_accuracy():
    """
    Check that accuracy is 100 if all shots are hits
    """
    range_game = AimTrainerRange()
    range_game._total_shots = 5
    range_game._hit_shots = 5
    assert range_game.accuracy() == 100


def test_accuracy_50_accuracy():
    """
    Check that accuracy is 50 if half of shots are hits
    """
    range_game = AimTrainerRange()
    range_game._total_shots = 10
    range_game._hit_shots = 5
    assert range_game.accuracy() == 50
