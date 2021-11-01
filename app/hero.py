from operator import attrgetter


class BattleResource(object):

    def __init__(self):
        self.value = 0
        self.type = "energy"
        self.max_value = 0

    def copy(self):
        a_copy = BattleResource()
        a_copy.value = self.value
        a_copy.type = self.type
        a_copy.max_value = self.max_value
        return a_copy

    def get_value(self):
        return self.value

    def add(self, amount):
        if self.value + amount <= self.max_value:
            self.value += amount
        else:
            self.value = self.max_value

    def minus(self, amount):
        if self.value - amount >= 0:
            self.value -= amount
        else:
            self.value = 0

    def clear(self):
        self.value = 0


class Properties(object):

    def __init__(self):
        self.hp = 0
        self.speed = 0
        self.atk = 0
        self.armor = 0
        self.battle_resource = BattleResource()

    def get_hp(self):
        return self.hp

    def get_atk(self):
        return self.atk

    def get_speed(self):
        return self.speed

    def get_armor(self):
        return self.armor

    def get_battle_resource(self):
        return self.battle_resource

    def add_battle_resource(self, amount):
        self.battle_resource.add(amount)

    def clear_battle_resource(self):
        self.battle_resource.clear()

    def copy(self):
        a_copy = Properties()
        a_copy.hp = self.hp
        a_copy.speed = self.speed
        a_copy.atk = self.atk
        a_copy.armor = self.armor
        a_copy.battle_resource = self.battle_resource.copy()
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

    # getter
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

    def get_armor(self):
        return self.current_properties.get_armor()

    def get_armor_factor(self):
        return float(1000)/(self.get_armor() + 1000)

    def get_speed(self):
        return self.current_properties.get_speed()

    def get_battle_resource(self):
        return self.current_properties.get_battle_resource()

    # modifier
    def add_battle_resource(self, amount):
        self.get_battle_resource().add(amount)

    # callbacks
    def on_before_damage_take(self, src_hero, src_skill, damage):
        pass

    def on_after_damage_take(self, src_hero, src_skill, damage, real_damage):
        pass

    # base method define
    def take_damage(self, src_hero, src_skill, damage):
        self.on_before_damage_take(src_hero, src_skill, damage)
        armor_factor = self.get_armor_factor()
        final_damage = int(damage * armor_factor)
        if final_damage > 0:
            self.current_properties.hp -= final_damage
        if self.current_properties.hp <= 0:
            self.is_dead = True
        self.on_after_damage_take(src_hero, src_skill, damage, final_damage)
        return final_damage

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
        print("%s pos:%d hp:%d atk:%d speed:%d, battle_resource:%d" % (self.get_name(), self.get_position(), self.get_hp(),
                                                   self.get_atk(), self.get_speed(), self.get_battle_resource().get_value()))
