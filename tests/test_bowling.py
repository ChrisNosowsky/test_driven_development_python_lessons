import unittest
import src.bowling as bowling

class TestBowlingCalculator(unittest.TestCase):
    def setUp(self):
        self.game = bowling.BowlingGame()

    def test_roll_all_gutter(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_roll_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_roll_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.assertEqual(self.game.score(), 16)

    def test_roll_strike(self):
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(3)
        self.assertEqual(self.game.score(), 26)

    def test_all_strikes(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

    def roll_many(self, rolls, pins):
        for roll in range(rolls):
            self.game.roll(pins)

# if __name__ == '__main__':
#     unittest.main()
