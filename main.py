from sword import Sword
from bow import Bow

MONSTER_START_HEALTH = 100
MIN_MONSTER_HEALTH = 0
SWORD_DAMAGE = 15
BOW_DAMAGE = 10
UNKNOWN_COMMAND_MESSAGE = 'Неизвестная команда. Попробуйте снова'

monster_health = MONSTER_START_HEALTH

commands = {
    '1': 'Атаковать мечом',
    '2': 'Атаковать из лука',
    '3': 'Выйти из программы'
}

SWORD_ATTACK_COMMAND, BOW_ATTACK_COMMAND, EXIT_COMMAND = commands.keys()


def print_commands():
    for number, command in commands.items():
        print(f'{number}: {command}')


def check_monster_death(health: int) -> bool:
    if health <= MIN_MONSTER_HEALTH:
        print('Монстр побежден!')
        return True
    else:
        return False


is_program_running = True

while is_program_running:
    print(f'Текущее здоровье монстра: {monster_health}')
    print()
    print_commands()
    user_command_number = input('Выберете тип оружия и укажите его номер: ').strip()

    if user_command_number in commands:
        if user_command_number == SWORD_ATTACK_COMMAND:
            print(Sword().attack())
            monster_health = monster_health - SWORD_DAMAGE
            print(f'Нанесено {SWORD_DAMAGE} единиц урона')

            if check_monster_death(monster_health):
                is_program_running = False
        elif user_command_number == BOW_ATTACK_COMMAND:
            print(Bow().attack())
            monster_health = monster_health - BOW_DAMAGE
            print(f'Нанесено {BOW_DAMAGE} единиц урона')

            if check_monster_death(monster_health):
                is_program_running = False
        elif user_command_number == EXIT_COMMAND:
            print('Выход из программы')
            is_program_running = False
        else:
            print(UNKNOWN_COMMAND_MESSAGE)
    else:
        print(UNKNOWN_COMMAND_MESSAGE)
