import unittest
from player_attack import FakePlayer, FakeArrow
import time

class TestPlayerAttack(unittest.TestCase):
    def test_attack_creates_arrow(self):
        player = FakePlayer()

        # Antes de atacar
        self.assertEqual(player.mana, 100)

        arrow = player.shoot()

        # Verifique se a flecha foi criada
        self.assertIsInstance(arrow, FakeArrow)
        self.assertEqual(arrow.position, (10, 0))
        self.assertEqual(player.mana, 90)

    def test_attack_does_not_create_arrow_when_no_mana(self):
        player = FakePlayer()
        player.mana = 5  # Menos de 10 de mana

        arrow = player.shoot()

        # Verifique que nenhuma flecha foi criada, já que a mana é insuficiente
        self.assertIsNone(arrow)
        self.assertEqual(player.mana, 5)

    def test_attack_does_not_repeat_until_cooldown(self):
        player = FakePlayer()

        # Primeiro ataque
        arrow = player.shoot()
        self.assertIsInstance(arrow, FakeArrow)

        # Esperar 0.5 segundos (menor que o cooldown) e tentar atacar
        time.sleep(0.5)
        arrow = player.shoot()

        # Verifique que o segundo ataque não foi realizado, porque o cooldown não passou
        self.assertIsNone(arrow)

        # Esperar mais 1 segundo (tempo de cooldown) e tentar atacar novamente
        time.sleep(1.0)
        arrow = player.shoot()

        # Agora deve criar a flecha
        self.assertIsInstance(arrow, FakeArrow)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
