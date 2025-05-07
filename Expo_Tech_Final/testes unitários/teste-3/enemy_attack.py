# enemy_attack.py

import time

class FakePlayer:
    def __init__(self):
        self.hp = 10
        self.is_alive = True

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.is_alive = False

class Enemy:
    def __init__(self):
        self.can_attack = True
        self.is_attacking = False
        self.is_hitbox_active = False
        self.bodies_in_hitbox = []
        self.HITBOX_START = 0.4
        self.HITBOX_DURATION = 0.2
        self.ATTACK_COOLDOWN = 1.5

    def attack(self):
        if not self.can_attack or self.is_attacking:
            return

        self.is_attacking = True
        self.can_attack = False

        # Simular tempo antes de ativar hitbox
        time.sleep(self.HITBOX_START)
        self.activate_hitbox()

        # Hitbox ativa por duração
        time.sleep(self.HITBOX_DURATION)
        self.deactivate_hitbox()

        # Fim do ataque
        self.is_attacking = False
        time.sleep(self.ATTACK_COOLDOWN)
        self.can_attack = True

    def activate_hitbox(self):
        self.is_hitbox_active = True
        for body in self.bodies_in_hitbox:
            if hasattr(body, "take_damage") and getattr(body, "is_alive", False):
                body.take_damage(10)

    def deactivate_hitbox(self):
        self.is_hitbox_active = False
