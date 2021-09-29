class Properties(object):

    def __init__(self):
        self.hp = 0
        self.speed = 0
        self.atk = 0
        self.energy = 0

    def get_hp(self):
        return self.hp

    def get_atk(self):
        return self.atk

    def get_speed(self):
        return self.speed

    def get_energy(self):
        return self.energy

    def copy(self):
        a_copy = Properties()
        a_copy.hp = self.hp
        a_copy.speed = self.speed
        a_copy.atk = self.atk
        a_copy.energy = self.energy
        return a_copy


class Hero(object):

    def __init__(self):
        self.initial_properties = Properties()
        self.current_properties = Properties()
        self.energy_type = "anger"
        self.player = None
        self.is_dead = False
        self.position = 0
        self.name = self.__class__.__name__

    def init_properties(self):
        self.current_properties = self.initial_properties.copy()

    def get_player(self):
        return self.player

    def get_atk(self):
        return self.current_properties.get_atk()

    def seek_target(self, enemy_list):
        for enemy in enemy_list:
            if not enemy.is_dead:
                return enemy
        return None

    def attack(self, target):
        if target is None:
            return
        target.take_damage(self.g)

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
        print("%s of %s at pos %d, speed:%d action:%s" % (
        self.name, self.player.name, self.position, self.speed, action_info))

    def print_info(self):
        print("%s pos:%d hp:%d atk:%d speed:%d" % (self.name, self.position, self.hp, self.atk, self.speed))
