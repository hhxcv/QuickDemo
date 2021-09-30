
class ActiveSkill(object):

    def __init__(self):
        self.name = ""
        self.description = ""
        self.priority = 0

    def get_priority(self):
        return self.priority

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def check_condition(self, hero, battle_ground):
        """
        check the condition of whether the skill can be casted
        :param hero: the hero who will cast this skill
        :param battle_ground: the current battle_ground
        :return: true if condition is met
        """
        pass

    def cast(self, hero, battle_ground):
        """
        cast the skill to targets
        :param hero: the hero who will cast this skill
        :param battle_ground: the current battle_ground
        :return: the result
        """
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

    def cast(self, hero, battle_ground):
        target_list = self.seek_targets(hero, battle_ground)
        self.attack(hero, target_list)

    def seek_targets(self, hero, battle_ground):
        enemy_list, ally_list = battle_ground.get_enemies_and_allies(hero.get_player())
        target_list = []
        for enemy in enemy_list:
            if not enemy.is_dead:
                target_list.append(enemy)
                return target_list
        return None

    def attack(self, hero, target_list):
        if target_list is None:
            return
        for target in target_list:
            target.take_damage(hero, self, hero.get_atk())
            hero.print_action_log("basic attack %s of %s at %d, damage:%d, target hp remains:%d"
                                  % (target.get_name(), target.get_player().get_name(), target.get_position(),
                                     hero.get_atk(), target.get_hp()))
