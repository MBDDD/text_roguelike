# Формат текста
class color:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'

# Класс параметров героя
class parameter:
    name = 0
    hp = 3
    money = 100
    treasure = 0
    adventure = 0
    command = 0

# Класс для подсчёта статистики похода
class adventure:
    hp = 0
    room = 0
    treasure = 0