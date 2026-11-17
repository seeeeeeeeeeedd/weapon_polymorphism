class Enemy:
    def __init__(self, health):
        self.__health = health

    def take_damage(self, damage: int) -> str:
        self.__health -= damage

        return f'Враг получил {damage} урона. Осталось здоровья: {self.__health}'
