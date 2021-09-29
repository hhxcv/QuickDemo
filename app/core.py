from operator import attrgetter

from app.battle_ground import BattleGround


class Engine:

    def __init__(self):
        self.battle_ground = BattleGround()
        self.loop_count = 0

    def get_battle_ground(self):
        return self.battle_ground

    def loop(self):
        self.loop_count += 1
        print("loop count:" + str(self.loop_count))
        action_list = self.battle_ground.get_action_list()
        for c in action_list:
            enemy_list, ally_list = self.battle_ground.get_enemies_and_allies(c.get_player())
            c.act(enemy_list, ally_list)
        self.battle_ground.print_info()

    def start(self):
        self.loop_count = 0
        while not self.battle_ground.is_end():
            self.loop()
