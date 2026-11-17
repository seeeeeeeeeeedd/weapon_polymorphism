from enemy import Enemy


class Weapon:
    def __init__(self, damage: int):
        self.__damage = damage

    def attack(self, enemy: Enemy) -> str:
        return enemy.take_damage(self.__damage)
