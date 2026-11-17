from weapon import Weapon
from enemy import Enemy


class Sword(Weapon):
    def __init__(self):
        super().__init__(20)

    def attack(self, enemy: Enemy) -> str:
        return f'Атака мечом! {super().attack(enemy)}'
