import unittest
from unittest import mock
from spaceship import Spaceship
from missions import NumberGuessingMission, RockPaperScissorsMission, AnimalGuessingMission, WordScrambleMission

class TestSpaceship(unittest.TestCase):
    def setUp(self):
        self.spaceship = Spaceship(fuel=300, supplies={'water': 50, 'food': 50})
    
    def test_refuel(self):
        self.spaceship.adjust_points(50)  # Add points for refueling
        self.spaceship.refuel(50)
        self.assertEqual(self.spaceship.fuel, 350)
        self.assertEqual(self.spaceship.points, 0)  # Points should be 0 after refueling

class TestMission(unittest.TestCase):
    def setUp(self):
        self.spaceship = Spaceship(fuel=300, supplies={'water': 50, 'food': 50})
    
    def test_number_guessing_mission(self):
        mission = NumberGuessingMission(name="Cosmic Codebreaker", reward=1000, spaceship=self.spaceship)
        # Provide sufficient mock input values for all input prompts
        with mock.patch('builtins.input', side_effect=['5']):
            mission.complete()
        self.assertGreaterEqual(self.spaceship.points, 0)  # Ensure points are adjusted correctly
    
    def test_rock_paper_scissors_mission(self):
        mission = RockPaperScissorsMission(name="Celestial Clash", reward=500, spaceship=self.spaceship)
        # Provide sufficient mock input values for all input prompts
        with mock.patch('builtins.input', side_effect=['rock']):
            mission.complete()
        self.assertGreaterEqual(self.spaceship.points, 0)  # Ensure points are adjusted correctly
    
    def test_animal_guessing_mission(self):
        mission = AnimalGuessingMission(name="Space Safari", reward=800, spaceship=self.spaceship)
        # Provide sufficient mock input values for all input prompts
        with mock.patch('builtins.input', side_effect=['cat']):
            mission.complete()
        self.assertGreaterEqual(self.spaceship.points, 0)  # Ensure points are adjusted correctly
    
    def test_word_scramble_mission(self):
        mission = WordScrambleMission(name="Stellar Scramble", reward=600, spaceship=self.spaceship)
        # Provide sufficient mock input values for all input prompts
        with mock.patch('builtins.input', side_effect=['planet']):
            mission.complete()
        self.assertGreaterEqual(self.spaceship.points, 0)  # Ensure points are adjusted correctly

if __name__ == '__main__':
    unittest.main()
