from operator import attrgetter

from app.player import Player


class BattleGround:

    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()

    def set_player(self, player1: Player, player2: Player):
        self.p1 = player1
        self.p2 = player2
        if self.p1.name is "":
            self.p1.name = "P1"
        if self.p2.name is "":
            self.p2.name = "P2"

    def is_end(self):
        return self.p1.is_all_hero_dead() or self.p2.is_all_hero_dead()

    def get_action_list(self):
        merge_list = self.p1.get_hero_list() + self.p2.get_hero_list()
        sc = sorted(merge_list, key=attrgetter('speed'))
        return sc

    def print_info(self):
        self.p1.print_info()
        self.p2.print_info()

    def get_enemies_and_allies(self, player):
        if player is self.p1:
            return self.p2.get_hero_list(), self.p1.get_hero_list()
        if player is self.p2:
            return self.p1.get_hero_list(), self.p2.get_hero_list()
        return None, None
