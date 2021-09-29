from app.hero import Hero


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