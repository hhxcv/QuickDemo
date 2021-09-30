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
        print("loop count:" + str(self.loop_count) + "==========================")
        action_list = self.battle_ground.get_action_order_list()
        for c in action_list:
            c.act(self.battle_ground)
        self.battle_ground.print_info()

    def start(self):
        self.loop_count = 0
        self.battle_ground.init_players()
        while not self.battle_ground.is_end():
            self.loop()
