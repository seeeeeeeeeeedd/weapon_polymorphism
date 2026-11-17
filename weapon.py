from enemy import Enemy


class Weapon:
    def __init__(self, damage: int):
        self.__damage = damage

    def attack(self, target: Enemy) -> str:
        return target.take_damage(self.__damage)
