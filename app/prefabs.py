from app.active_skill import BasicAttack
from app.hero import Hero


class Warrior(Hero):

    def __init__(self):
        super().__init__()
        self.initial_properties.speed = 300
        self.initial_properties.hp = 1000
        self.initial_properties.atk = 75
        self.initial_properties.energy = 0
        self.initial_properties.max_energy = 100
        self.active_skill_list.append(BasicAttack())

