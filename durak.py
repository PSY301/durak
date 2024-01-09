names = []  # имена игроков
deck = {}  # оставшиеся в колоде карты
dict_of_deck = {}  # словарь для расшифровки строчных элементов deck(валет и т.д)
players_cards = []  # карты на руках у игроков
kos = ''  # козырь(черви)
table_cards = []  # карты на столе
over_players = []


def hi():  # функция для заполнения names, players_cards
    pass


def comfortable_sort(player):  # сортировка карт на руке
    pass


def attack(player):  # универсальная функция для атаки
    pass


def defend(player):  # универсальная функция для нападения
    pass


def turn(player):  # универсальная функция для ввода в курс дела игрока
    pass


with open('разрешение_на_игру.txt') as file:
    if any(i == 'РАЗРЕШЕНО' for i in file):
        pass

    else:
        print('игра запрещена')
