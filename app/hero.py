from operator import attrgetter


class Properties(object):

    def __init__(self):
        self.hp = 0
        self.speed = 0
        self.atk = 0
        self.energy = 0
        self.max_energy = 0

    def get_hp(self):
        return self.hp

    def get_atk(self):
        return self.atk

    def get_speed(self):
        return self.speed

    def get_energy(self):
        return self.energy

    def get_max_energy(self):
        return self.max_energy

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
        self.active_skill_list = []
        self.name = self.__class__.__name__

    def init_properties(self):
        self.current_properties = self.initial_properties.copy()

    def get_name(self):
        return self.name

    def get_player(self):
        return self.player

    def get_position(self):
        return self.position

    def get_hp(self):
        return self.current_properties.get_hp()

    def get_atk(self):
        return self.current_properties.get_atk()

    def get_speed(self):
        return self.current_properties.get_speed()

    def take_damage(self, src_hero, src_skill, damage):
        self.current_properties.hp -= damage
        if self.current_properties.hp <= 0:
            self.is_dead = True

    def get_top_priority_castable_skill(self, battle_ground):
        self.active_skill_list = sorted(self.active_skill_list, key=attrgetter('priority'), reverse=True)
        for sk in self.active_skill_list:
            if sk.check_condition(self, battle_ground):
                return sk
        return None

    def act(self, battle_ground):
        if self.is_dead:
            return
        skill = self.get_top_priority_castable_skill(battle_ground)
        if skill is not None:
            skill.cast(self, battle_ground)
        else:
            self.print_action_log("no action")

    def print_action_log(self, action_info: str):
        print("%s of %s at pos %d, speed:%d action:%s" % (
            self.get_name(), self.player.get_name(), self.get_position(), self.get_speed(), action_info))

    def print_info(self):
        print("%s pos:%d hp:%d atk:%d speed:%d" % (self.get_name(), self.get_position(), self.get_hp(),
                                                   self.get_atk(), self.get_speed()))
