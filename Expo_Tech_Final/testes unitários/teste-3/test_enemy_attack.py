import unittest
from enemy_attack import Enemy, FakePlayer

class TestEnemyAttack(unittest.TestCase):
    def test_attack_hits_player(self):
        enemy = Enemy()
        player = FakePlayer()
        enemy.bodies_in_hitbox.append(player)

        enemy.attack()

        self.assertEqual(player.hp, 0)
        self.assertFalse(player.is_alive)
        self.assertTrue(enemy.can_attack)

    def test_attack_does_not_repeat_while_on_cooldown(self):
        enemy = Enemy()
        player = FakePlayer()
        enemy.bodies_in_hitbox.append(player)

        # Start first attack
        enemy.attack()
        # Try to attack again immediately (should not work)
        enemy.is_attacking = True  # simulate in-progress
        player.hp = 10  # reset
        enemy.attack()
        self.assertEqual(player.hp, 10)  # should not be hit again

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
