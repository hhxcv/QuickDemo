from seek import SeekFirstEnemy


class ActiveSkill(object):

    def __init__(self):
        self.name = ""
        self.description = ""
        self.priority = 0
        self.seek_targets_strategy = SeekFirstEnemy()

    def get_priority(self):
        return self.priority

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def seek_targets(self, hero, battle_ground):
        return self.seek_targets_strategy.seek_targets(hero, battle_ground)

    def check_condition(self, hero, battle_ground):
        """
        check the condition of whether the skill can be casted
        :param hero: the hero who will cast this skill
        :param battle_ground: the current battle_ground
        :return: true if condition is met
        """
        pass

    def on_before_cast(self, hero, target_list):
        pass

    def on_after_cast(self, hero, target_list):
        pass

    def on_cast(self, hero, target_list):
        pass

    def cast(self, hero, battle_ground):
        """
        cast the skill to targets
        :param hero: the hero who will cast this skill
        :param battle_ground: the current battle_ground
        :return: the result
        """
        target_list = self.seek_targets(hero, battle_ground)
        self.on_before_cast(hero, target_list)
        self.on_cast(hero, target_list)
        self.on_after_cast(hero, target_list)
        pass


class BasicAttack(ActiveSkill):

    def __init__(self):
        super(BasicAttack, self).__init__()
        self.name = "BasicAttack"
        self.description = "BasicAttack"

    def check_condition(self, hero, battle_ground):
        target_list = self.seek_targets(hero, battle_ground)
        if target_list is not None and len(target_list) > 0:
            return True
        return False

    def on_before_cast(self, hero, target):
        pass

    def on_after_cast(self, hero, target):
        pass

    def on_cast(self, hero, target_list):
        if target_list is None:
            return
        for target in target_list:
            damage = hero.get_atk()
            self.on_before_cast(hero, target)
            final_damage = target.take_damage(hero, self, damage)
            self.on_after_cast(hero, target)
            hero.print_action_log("basic attack %s of %s at %d, final damage:%d, target hp remains:%d"
                                  % (target.get_name(), target.get_player().get_name(), target.get_position(),
                                     final_damage, target.get_hp()))


class AngerBasicAttack(BasicAttack):

    def __init__(self):
        super().__init__()

    def on_after_cast(self, hero, target):
        hero.add_battle_resource(25)
