from operator import attrgetter


class Hero(object):

    def __init__(self):
        self.speed = 0
        self.hp = 0
        self.atk = 0
        self.player = None
        self.is_dead = False
        self.position = 0
        self.name = self.__class__.__name__

    def get_player(self):
        return self.player

    def seek_target(self, enemy_list):
        for enemy in enemy_list:
            if not enemy.is_dead:
                return enemy
        return None

    def attack(self, target):
        if target is None:
            return
        target.take_damage(self.atk)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.is_dead = True

    def act(self, enemy_list, ally_list):
        if self.is_dead:
            return
        target = self.seek_target(enemy_list)
        self.attack(target)
        if target is None:
            self.print_action_log("attack None")
        else:
            self.print_action_log("attack " + target.name + " at pos " + str(target.position))

    def print_action_log(self, action_info: str):
        print("%s of %s at pos %d, speed:%d action:%s" % (self.name, self.player.name, self.position, self.speed, action_info))

    def print_info(self):
        print("%s pos:%d hp:%d atk:%d speed:%d" % (self.name, self.position, self.hp, self.atk, self.speed))


class Player:

    def __init__(self):
        self.hero_list = []
        self.name = ""

    def add_hero(self, hero: Hero):
        hero.player = self
        self.hero_list.append(hero)
        hero.position = self.hero_list.index(hero)

    def is_all_hero_dead(self):
        for hero in self.hero_list:
            if not hero.is_dead:
                return False
        return True

    def get_hero_list(self):
        return self.hero_list

    def print_info(self):
        print(self.name + " info:")
        for hero in self.hero_list:
            hero.print_info()


class BattleGround:

    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        self.p1.name = "P1"
        self.p2.name = "P2"

    def is_end(self):
        return self.p1.is_all_hero_dead() or self.p2.is_all_hero_dead()

    def get_action_list(self):
        return self.p1.get_hero_list() + self.p2.get_hero_list()

    def print_info(self):
        self.p1.print_info()
        self.p2.print_info()

    def get_enemies_and_allies(self, player):
        if player is self.p1:
            return self.p2.get_hero_list(), self.p1.get_hero_list()
        if player is self.p2:
            return self.p1.get_hero_list(), self.p2.get_hero_list()
        return None, None

class Engine:

    def __init__(self):
        self.battle_ground = BattleGround()
        self.loop_count = 0

    def loop(self):
        self.loop_count += 1
        print("loop count:" + str(self.loop_count))
        action_list = self.battle_ground.get_action_list()
        sc = sorted(action_list, key=attrgetter('speed'))
        for c in sc:
            enemy_list, ally_list = self.battle_ground.get_enemies_and_allies(c.get_player())
            c.act(enemy_list, ally_list)
        self.battle_ground.print_info()

    def start(self):
        self.loop_count = 0
        while not self.battle_ground.is_end():
            self.loop()

