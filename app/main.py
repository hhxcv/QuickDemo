from app import prefabs
from app.core import Engine

if __name__ == "__main__":
    engine = Engine()
    for i in range(0, 6):
        engine.battle_ground.p1.add_hero(prefabs.Warrior())
    for i in range(0, 6):
        engine.battle_ground.p2.add_hero(prefabs.Warrior())
    engine.start()
