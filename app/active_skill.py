
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

    def check_condition(self, battle_ground):
        """
        check the condition of whether the skill can be casted
        :param battle_ground: the current battle_ground
        :return: true if condition is met
        """
        pass

    def cast(self, battle_ground):
        """
        cast the skill to targets
        :param battle_ground: the current battle_ground
        :return: the result
        """
        pass
