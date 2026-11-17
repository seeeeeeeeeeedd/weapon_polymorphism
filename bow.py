from weapon import Weapon
from enemy import Enemy
from random import random


class Bow(Weapon):
    def __init__(self):
        self.BOW_DAMAGE = 10
        self.CRITICAL_CHANCE = 0.3
        self.CRITICAL_MULTIPLIER = 3
        super().__init__(self.BOW_DAMAGE)

    def attack(self, enemy: Enemy):
        return f'Атака из лука! {super().attack(enemy)}'

    def get_damage(self) -> int:
        if random.random() < self.CRITICAL_CHANCE:
            critical_damage = self.BOW_DAMAGE * self.CRITICAL_MULTIPLIER

            return critical_damage

        return super().get_damage()
