class Weapon:
    def __init__(self, damage: int):
        self.__damage = damage

    def attack(self):
        return 'Атака не выполнена. Оружие не выбрано'
