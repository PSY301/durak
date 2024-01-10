import random
from loguru import logger
kos = {}
tasks = []
deck = []
names = []  # имена игроков
deck_52 = [{'suit': 'черви', 'value': 2}, {'suit': 'черви', 'value': 3}, {'suit': 'черви', 'value': 4}, {'suit': 'черви', 'value': 5}, {'suit': 'черви', 'value': 6}, {'suit': 'черви', 'value': 7}, {'suit': 'черви', 'value': 8}, {'suit': 'черви', 'value': 9}, {'suit': 'черви', 'value': 10}, {'suit': 'черви', 'value': 'валет'}, {'suit': 'черви', 'value': 'дама'}, {'suit': 'черви', 'value': 'король'}, {'suit': 'черви', 'value': 'туз'}, {'suit': 'пики', 'value': 2}, {'suit': 'пики', 'value': 3}, {'suit': 'пики', 'value': 4}, {'suit': 'пики', 'value': 5}, {'suit': 'пики', 'value': 6}, {'suit': 'пики', 'value': 7}, {'suit': 'пики', 'value': 8}, {'suit': 'пики', 'value': 9}, {'suit': 'пики', 'value': 10}, {'suit': 'пики', 'value': 'валет'}, {'suit': 'пики', 'value': 'дама'}, {'suit': 'пики', 'value': 'король'}, {'suit': 'пики', 'value': 'туз'}, {'suit': 'крести', 'value': 2}, {'suit': 'крести', 'value': 3}, {'suit': 'крести', 'value': 4}, {'suit': 'крести', 'value': 5}, {'suit': 'крести', 'value': 6}, {'suit': 'крести', 'value': 7}, {'suit': 'крести', 'value': 8}, {'suit': 'крести', 'value': 9}, {'suit': 'крести', 'value': 10}, {'suit': 'крести', 'value': 'валет'}, {'suit': 'крести', 'value': 'дама'}, {'suit': 'крести', 'value': 'король'}, {'suit': 'крести', 'value': 'туз'}, {'suit': 'буби', 'value': 2}, {'suit': 'буби', 'value': 3}, {'suit': 'буби', 'value': 4}, {'suit': 'буби', 'value': 5}, {'suit': 'буби', 'value': 6}, {'suit': 'буби', 'value': 7}, {'suit': 'буби', 'value': 8}, {'suit': 'буби', 'value': 9}, {'suit': 'буби', 'value': 10}, {'suit': 'буби', 'value': 'валет'}, {'suit': 'буби', 'value': 'дама'}, {'suit': 'буби', 'value': 'король'}, {'suit': 'буби', 'value': 'туз'}]  # оставшиеся в колоде карты
deck_36 = [{'suit': 'черви', 'value': 6}, {'suit': 'черви', 'value': 7}, {'suit': 'черви', 'value': 8}, {'suit': 'черви', 'value': 9}, {'suit': 'черви', 'value': 10}, {'suit': 'черви', 'value': 'валет'}, {'suit': 'черви', 'value': 'дама'}, {'suit': 'черви', 'value': 'король'}, {'suit': 'черви', 'value': 'туз'}, {'suit': 'крести', 'value': 6}, {'suit': 'крести', 'value': 7}, {'suit': 'крести', 'value': 8}, {'suit': 'крести', 'value': 9}, {'suit': 'крести', 'value': 10}, {'suit': 'крести', 'value': 'валет'}, {'suit': 'крести', 'value': 'дама'}, {'suit': 'крести', 'value': 'король'}, {'suit': 'крести', 'value': 'туз'}, {'suit': 'пики', 'value': 6}, {'suit': 'пики', 'value': 7}, {'suit': 'пики', 'value': 8}, {'suit': 'пики', 'value': 9}, {'suit': 'пики', 'value': 10}, {'suit': 'пики', 'value': 'валет'}, {'suit': 'пики', 'value': 'дама'}, {'suit': 'пики', 'value': 'король'}, {'suit': 'пики', 'value': 'туз'}, {'suit': 'буби', 'value': 6}, {'suit': 'буби', 'value': 7}, {'suit': 'буби', 'value': 8}, {'suit': 'буби', 'value': 9}, {'suit': 'буби', 'value': 10}, {'suit': 'буби', 'value': 'валет'}, {'suit': 'буби', 'value': 'дама'}, {'suit': 'буби', 'value': 'король'}, {'suit': 'буби', 'value': 'туз'}]
#dict_of_deck = {'валет': 11, "дама": 12, "король": 13, "туз": 14}  # словарь для расшифровки строчных элементов deck(валет и т.д)
players_cards = []  # карты на руках у игроков
table_cards = []  # карты на столе
over_players = []  # вышедшие игроки

logger.add('for_durak.log', format="{time} {level} {message}", level='DEBUG')


@logger.catch
def hi():  # функция для заполнения names, players_cards
    global deck, kos, tasks
    if int(input("сколько карт будет у вас в колоде?")) == 36:
        random.shuffle(deck_36)
        deck = deck_36
    else:
        random.shuffle(deck_52)
        deck = deck_52
    kos = deck[0]
    deck.pop(0)
    for i in range(int(input('сколько игроков будет играть?'))):
        tasks.append('защита')
        player = input(f'введите имя {i + 1} игрока')
        names.append(player)
        players_cards.append([])
        for _ in range(6):
            players_cards[i].append(deck[0])
            deck.pop(0)


@logger.catch
def turn(player):  # универсальная функция для хода
    table_cards = []
    for i in range(len(names)):
        for o in range(6 - len(players_cards[player])):
            players_cards[player].append(deck[0])
            deck.pop(0)
    print('\n' * 100, f"очередь игрока {names[player]}", sep='')
    print('ваши карты:')
    for i in players_cards[player]:
        mast, number = i.values()
        print(number, mast, sep=' ', end='\n')
    print('козырь - ' + list(kos.values())[0])
    for i in range(len(names)):
        if i == player:
            tasks[i] = 'attack'
        elif i == player + 1:
            tasks[i] = 'defend'
        else:
            tasks[i] = 'dop_attack'

    if tasks[player] == 'attack':
        try:
            print(f'вы играете под игрока {names[player + 1]}')
        except IndexError:
            print(f'вы играете под игрока {names[0]}')
        while True:
            attack_cards = input('из своих карт, выберете какой хотите сходить')
            if attack_cards == 'пасс':
                break
            else:
                attack_cards = int(attack_cards)
            table_cards.append(players_cards[player][attack_cards - 1])
            players_cards[player].pop(attack_cards - 1)
            for i in players_cards[player]:
                mast, number = i.values()
                print(number, mast, sep=' ', end='\n')

with open('разрешение_на_игру.txt') as file:
    if any(i == '____ok____alright____\n' for i in file):
        hi()
        for i in range(len(names)):
            if len(over_players) > len(names) - 2:
                break
            turn(i)
        print(f'игра законченна, дураком остался {names[0]}')
    else:
        print('игра запрещена')
