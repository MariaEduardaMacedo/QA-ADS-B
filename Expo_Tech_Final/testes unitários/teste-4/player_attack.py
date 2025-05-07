import time

class FakeArrow:
    def __init__(self, speed, position=(10, 0)):  # Definindo a posição como (10, 0) por padrão
        self.speed = speed
        self.position = position  # Usando a posição fornecida
        self.flip_h = False

class FakePlayer:
    def __init__(self):
        self.mana = 100
        self.can_shot = True
        self.is_shooting = False
        self.arrow_placement = (10, 0)  # Localização inicial da flecha
        self.arrow_speed = 5
        self.last_shot_time = 0  # Para controlar o tempo do último ataque
        self.attack_cooldown = 1  # Cooldown de 1 segundo para o ataque

    def shoot(self):
        current_time = time.time()

        # Verificar cooldown e mana suficiente
        if self.mana < 10 or (current_time - self.last_shot_time) < self.attack_cooldown:
            return None  # Não cria a flecha se estiver no cooldown ou sem mana suficiente

        # Se o cooldown passou, cria o ataque
        self.mana -= 10  # Gasta mana
        self.last_shot_time = current_time  # Atualiza o tempo do último ataque
        return FakeArrow(self.arrow_speed, self.arrow_placement)  # Passando a posição correta
