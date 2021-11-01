from app.active_skill import BasicAttack, ActiveSkill, AngerBasicAttack
from app.hero import Hero


class AngryAttack(ActiveSkill):

    def __init__(self):
        super(AngryAttack, self).__init__()
        self.priority = 1

    def check_condition(self, hero, battle_ground):
        target_list = self.seek_targets(hero, battle_ground)
        if target_list is not None and len(target_list) > 0:
            br = hero.get_battle_resource()
            if br.value >= br.max_value:
                return True
            return False
        return False

    def on_cast(self, hero, target_list):
        if target_list is None:
            return
        hero.get_battle_resource().clear()
        for target in target_list:
            damage = int(hero.get_atk() * 2.5)
            self.on_before_cast(hero, target)
            final_damage = target.take_damage(hero, self, damage)
            self.on_after_cast(hero, target)
            hero.print_action_log("anger attack %s of %s at %d, final damage:%d, target hp remains:%d"
                                  % (target.get_name(), target.get_player().get_name(), target.get_position(),
                                     final_damage, target.get_hp()))


class Warrior(Hero):

    def __init__(self):
        super().__init__()
        self.initial_properties.speed = 300
        self.initial_properties.hp = 1000
        self.initial_properties.atk = 75
        self.initial_properties.armor = 200
        self.initial_properties.battle_resource.type = "anger"
        self.initial_properties.battle_resource.value = 0
        self.initial_properties.battle_resource.max_value = 100
        self.active_skill_list.append(AngerBasicAttack())
        self.active_skill_list.append(AngryAttack())

    def on_after_damage_take(self, src_hero, src_skill, damage, real_damage):
        self.current_properties.battle_resource.add(10)
