from godot import exposed, export
from godot import Vector2
from godot import ProjectSettings

@exposed
class Player(CharacterBody2D):

    # Variáveis de controle de movimento
    speed = 160.0
    jump_velocity = -300.0
    max_jumps = 2  # Máximo de pulos permitidos
    jumps = 0  # Contador de pulos realizados

    # Variáveis para controle de entrada
    dir = 0
    gravity = ProjectSettings.get_setting("physics/2d/default_gravity")
    can_shot: bool = True
    is_alive = True
    is_shooting: bool = False

    # Exportações
    left = export(str, default="ui_left")  # Default input para esquerda
    right = export(str, default="ui_right")  # Default input para direita
    jump = export(str, default="ui_up")  # Default input para pulo
    shoot_action = export(str, default="ui_accept")  # Default input para atirar

    # Referências de nós
    sprite = None
    arrow_placement = None
    _Arrow = None

    def _ready(self):
        # Inicialização dos nós
        self.sprite = self.get_node("AnimatedSprite2D")
        self.arrow_placement = self.get_node("ArrowPlacement")
        self._Arrow = preload("res://Scenes/arrow.tscn")

    def move(self, delta):
        if self.is_alive:
            # Obtém a direção de movimento a partir das entradas
            self.dir = Input.get_axis(self.left, self.right)

            # Ajusta a velocidade com base na direção
            if self.dir != 0:
                self.velocity.x = self.dir * self.speed
            else:
                self.velocity.x = 0

            # Aplica a gravidade se o jogador não está no chão
            if not self.is_on_floor():
                self.velocity.y += self.gravity * delta
            else:
                # Reseta o contador de pulos quando o jogador está no chão
                self.jumps = 0

            # Verifica se o jogador pode pular
            if self.is_alive and Input.is_action_just_pressed(self.jump) and self.jumps < self.max_jumps:
                self.velocity.y = self.jump_velocity
                self.jumps += 1  # Aumenta o contador de pulos

            # Aplica o movimento
            self.move_and_slide()

    def animations(self):
        if self.is_shooting:
            return  # Evita trocar a animação durante o tiro

        if self.velocity.x != 0 and self.is_on_floor():
            self.sprite.play("Run")
        elif self.velocity.x == 0 and self.is_on_floor():
            self.sprite.play("Idle")

        if not self.is_on_floor() and self.jumps >= 1:
            self.sprite.play("Jump")

        # Flips para a direção do sprite
        if self.dir > 0:
            self.sprite.flip_h = False
        elif self.dir < 0:
            self.sprite.flip_h = True

    def _physics_process(self, delta):
        self.move(delta)
        # Aqui você pode adicionar a função de disparo (caso necessário)
        self.animations()
