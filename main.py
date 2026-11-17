from sword import Sword
from bow import Bow
from enemy import Enemy

ENEMY_START_HEALTH = 100
MIN_ENEMY_HEALTH = 0

UNKNOWN_COMMAND_MESSAGE = 'Неизвестная команда. Попробуйте снова'

enemy = Enemy(ENEMY_START_HEALTH)

commands = {
    '1': 'Атаковать мечом',
    '2': 'Атаковать из лука',
    '3': 'Выйти из программы'
}

SWORD_ATTACK_COMMAND, BOW_ATTACK_COMMAND, EXIT_COMMAND = commands.keys()


def print_commands():
    for number, command in commands.items():
        print(f'{number}: {command}')


def check_enemy_death(health: int) -> bool:
    if health <= MIN_ENEMY_HEALTH:
        print('Враг побежден!')

        return True
    else:
        return False


is_program_running = True

print(f'Текущее здоровье врага: {enemy.get_health()}')

while is_program_running:
    print()
    print_commands()
    user_command_number = input('Выберете тип оружия и укажите его номер: ').strip()

    if user_command_number in commands:
        if user_command_number == SWORD_ATTACK_COMMAND:
            weapon = Sword()
        elif user_command_number == BOW_ATTACK_COMMAND:
            weapon = Bow()
        elif user_command_number == EXIT_COMMAND:
            print('Выход из программы')
            is_program_running = False

        if is_program_running:
            attack_result = weapon.attack(enemy)
            print(attack_result)

            if check_enemy_death(enemy.get_health()):
                is_program_running = False
    else:
        print(UNKNOWN_COMMAND_MESSAGE)
