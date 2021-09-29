from app.hero import Hero


class Warrior(Hero):

    def __init__(self):
        super().__init__()
        self.speed = 300
        self.hp = 1000
        self.atk = 75

