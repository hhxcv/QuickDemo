from app import prefabs
from app.core import Engine
from app.player import Player


def create_players():
    p1 = Player()
    p2 = Player()
    for index in range(0, 6):
        p1.add_hero(prefabs.Warrior())
    for index in range(0, 6):
        p2.add_hero(prefabs.Warrior())
    return p1, p2


if __name__ == "__main__":
    engine = Engine()
    battle_ground = engine.get_battle_ground()
    player1, player2 = create_players()
    battle_ground.set_player(player1, player2)
    engine.start()
