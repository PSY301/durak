import random

names = []  # имена игроков
deck_52 = [{'suit': 'черви', 'value': 2}, {'suit': 'черви', 'value': 3}, {'suit': 'черви', 'value': 4}, {'suit': 'черви', 'value': 5}, {'suit': 'черви', 'value': 6}, {'suit': 'черви', 'value': 7}, {'suit': 'черви', 'value': 8}, {'suit': 'черви', 'value': 9}, {'suit': 'черви', 'value': 10}, {'suit': 'черви', 'value': 'валет'}, {'suit': 'черви', 'value': 'дама'}, {'suit': 'черви', 'value': 'король'}, {'suit': 'черви', 'value': 'туз'}, {'suit': 'пики', 'value': 2}, {'suit': 'пики', 'value': 3}, {'suit': 'пики', 'value': 4}, {'suit': 'пики', 'value': 5}, {'suit': 'пики', 'value': 6}, {'suit': 'пики', 'value': 7}, {'suit': 'пики', 'value': 8}, {'suit': 'пики', 'value': 9}, {'suit': 'пики', 'value': 10}, {'suit': 'пики', 'value': 'валет'}, {'suit': 'пики', 'value': 'дама'}, {'suit': 'пики', 'value': 'король'}, {'suit': 'пики', 'value': 'туз'}, {'suit': 'крести', 'value': 2}, {'suit': 'крести', 'value': 3}, {'suit': 'крести', 'value': 4}, {'suit': 'крести', 'value': 5}, {'suit': 'крести', 'value': 6}, {'suit': 'крести', 'value': 7}, {'suit': 'крести', 'value': 8}, {'suit': 'крести', 'value': 9}, {'suit': 'крести', 'value': 10}, {'suit': 'крести', 'value': 'валет'}, {'suit': 'крести', 'value': 'дама'}, {'suit': 'крести', 'value': 'король'}, {'suit': 'крести', 'value': 'туз'}, {'suit': 'буби', 'value': 2}, {'suit': 'буби', 'value': 3}, {'suit': 'буби', 'value': 4}, {'suit': 'буби', 'value': 5}, {'suit': 'буби', 'value': 6}, {'suit': 'буби', 'value': 7}, {'suit': 'буби', 'value': 8}, {'suit': 'буби', 'value': 9}, {'suit': 'буби', 'value': 10}, {'suit': 'буби', 'value': 'валет'}, {'suit': 'буби', 'value': 'дама'}, {'suit': 'буби', 'value': 'король'}, {'suit': 'буби', 'value': 'туз'}]  # оставшиеся в колоде карты
deck_36 = [{'suit': 'черви', 'value': 6}, {'suit': 'черви', 'value': 7}, {'suit': 'черви', 'value': 8}, {'suit': 'черви', 'value': 9}, {'suit': 'черви', 'value': 10}, {'suit': 'черви', 'value': 'валет'}, {'suit': 'черви', 'value': 'дама'}, {'suit': 'черви', 'value': 'король'}, {'suit': 'черви', 'value': 'туз'}, {'suit': 'крести', 'value': 6}, {'suit': 'крести', 'value': 7}, {'suit': 'крести', 'value': 8}, {'suit': 'крести', 'value': 9}, {'suit': 'крести', 'value': 10}, {'suit': 'крести', 'value': 'валет'}, {'suit': 'крести', 'value': 'дама'}, {'suit': 'крести', 'value': 'король'}, {'suit': 'крести', 'value': 'туз'}, {'suit': 'пики', 'value': 6}, {'suit': 'пики', 'value': 7}, {'suit': 'пики', 'value': 8}, {'suit': 'пики', 'value': 9}, {'suit': 'пики', 'value': 10}, {'suit': 'пики', 'value': 'валет'}, {'suit': 'пики', 'value': 'дама'}, {'suit': 'пики', 'value': 'король'}, {'suit': 'пики', 'value': 'туз'}, {'suit': 'буби', 'value': 6}, {'suit': 'буби', 'value': 7}, {'suit': 'буби', 'value': 8}, {'suit': 'буби', 'value': 9}, {'suit': 'буби', 'value': 10}, {'suit': 'буби', 'value': 'валет'}, {'suit': 'буби', 'value': 'дама'}, {'suit': 'буби', 'value': 'король'}, {'suit': 'буби', 'value': 'туз'}]
dict_of_deck = {'валет': 11, "дама": 12, "король": 13, "туз": 14}  # словарь для расшифровки строчных элементов deck(валет и т.д)
players_cards = []  # карты на руках у игроков
kos = ''  # козырь(черви)
table_cards = []  # карты на столе
over_players = [] # вышедшие игроки


def hi():  # функция для заполнения names, players_cards
    if input("сколько карт будет у вас в колоде?") == 36:
        random.shuffle(deck_36)
        deck = deck_36
    else:
        random.shuffle(deck_52)
        deck = deck_52
    for i in range(int(input('сколько игроков будет играть?'))):
        player = input(f'введите имя {i + 1} игрока')
        names.append(player)
        players_cards.append([])
        for l in range(6):
            players_cards[i].append(deck[0])
            deck.pop(0)
    print(deck, names, players_cards, sep='\n')


def comfortable_sort(player):  # сортировка карт на руке
    pass


def attack(player):  # универсальная функция для атаки
    pass


def defend(player):  # универсальная функция для нападения
    pass


def turn(player):  # универсальная функция для ввода в курс дела игрока
    pass


with open('разрешение_на_игру.txt') as file:
    if any(i == '____ok____alright____\n' for i in file):
        hi()

    else:
        print('игра запрещена')
