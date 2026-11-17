from weapon import Weapon
from enemy import Enemy


class Sword(Weapon):
    def __init__(self):
        self.SWORD_DAMAGE = 20
        super().__init__(self.SWORD_DAMAGE)

    def attack(self, enemy: Enemy) -> str:
        return f'Атака мечом! {super().attack(enemy)}'
