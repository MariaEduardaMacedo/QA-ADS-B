import unittest
from double_jump import try_jump

class TestJump(unittest.TestCase):
    def test_double_jump(self):
        max_jumps = 2
        jump_velocity = -300.0
        jumps = 0

        # Primeiro pulo
        velocity_y, jumps = try_jump(jumps, max_jumps, jump_velocity)
        self.assertEqual(velocity_y, -300.0)
        self.assertEqual(jumps, 1)

        # Segundo pulo
        velocity_y, jumps = try_jump(jumps, max_jumps, jump_velocity)
        self.assertEqual(velocity_y, -300.0)
        self.assertEqual(jumps, 2)

        # Terceiro tentativa (deve falhar)
        velocity_y, jumps = try_jump(jumps, max_jumps, jump_velocity)
        self.assertIsNone(velocity_y)
        self.assertEqual(jumps, 2)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
