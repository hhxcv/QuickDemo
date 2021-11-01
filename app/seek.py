class SeekFirstEnemy:

    def seek_targets(self, hero, battle_ground):
        enemy_list, ally_list = battle_ground.get_enemies_and_allies(hero.get_player())
        target_list = []
        for enemy in enemy_list:
            if not enemy.is_dead:
                target_list.append(enemy)
                return target_list
        return None