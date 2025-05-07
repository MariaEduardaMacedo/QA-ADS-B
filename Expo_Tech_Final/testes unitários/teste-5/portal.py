import time

class FakePlayer:
    def __init__(self, name):
        self.name = name
        self.groups = ["players"]
        self.freed = False

    def is_in_group(self, group_name):
        return group_name in self.groups

    def queue_free(self):
        self.freed = True

class NotAPlayer:
    def is_in_group(self, group_name):
        return False

class FakeTree:
    def __init__(self):
        self.changed_scene = None

    def create_timer(self, wait_time):
        time.sleep(wait_time)
        return self

    @property
    def timeout(self):
        return True

    def change_scene_to_file(self, scene_path):
        self.changed_scene = scene_path

class FakePortal:
    def __init__(self, scene_path="res://Scenes/level_2.tscn"):
        self.scene = scene_path
        self.players_in_portal = []
        self.tree = FakeTree()

    def get_tree(self):
        return self.tree

    def _on_body_entered(self, body):
        if body.is_in_group("players") and body not in self.players_in_portal:
            self.players_in_portal.append(body)

            time.sleep(0.3)
            body.queue_free()

            if len(self.players_in_portal) >= 2:
                time.sleep(0.5)
                self.get_tree().change_scene_to_file(self.scene)
