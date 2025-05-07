# test_walk.py (ou direto no Colab)
import unittest
from walk import move_player

class TestPlayerMovement(unittest.TestCase):
    def test_move_left(self):
        result = move_player(-1, 140.0)
        self.assertEqual(result, -140.0)

unittest.main(argv=[''], exit=False)
