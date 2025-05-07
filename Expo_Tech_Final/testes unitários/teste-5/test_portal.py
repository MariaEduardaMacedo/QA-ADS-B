import unittest
from portal import FakePortal, FakePlayer, NotAPlayer

class TestPortal(unittest.TestCase):

    def test_single_player_enters(self):
        portal = FakePortal()
        player1 = FakePlayer("Player1")
        portal._on_body_entered(player1)

        self.assertTrue(player1.freed)
        self.assertEqual(len(portal.players_in_portal), 1)
        self.assertIsNone(portal.get_tree().changed_scene)

    def test_two_players_enter_triggers_scene_change(self):
        portal = FakePortal()
        player1 = FakePlayer("Player1")
        player2 = FakePlayer("Player2")

        portal._on_body_entered(player1)
        portal._on_body_entered(player2)

        self.assertTrue(player1.freed)
        self.assertTrue(player2.freed)
        self.assertEqual(len(portal.players_in_portal), 2)
        self.assertEqual(portal.get_tree().changed_scene, portal.scene)

    def test_ignores_non_player_bodies(self):
        portal = FakePortal()
        obj = NotAPlayer()
        portal._on_body_entered(obj)

        self.assertEqual(len(portal.players_in_portal), 0)
        self.assertIsNone(portal.get_tree().changed_scene)

if __name__ == "__main__":
    unittest.main()
