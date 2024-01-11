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
otb_table_cards = []
ber_stat = []
players_pass = []

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
        ber_stat.append(False)
        players_pass.append(0)
        player = input(f'введите имя {i + 1} игрока')
        names.append(player)
        players_cards.append([])
        for _ in range(6):
            players_cards[i].append(deck[0])
            deck.pop(0)


def print_cards(player):
    for i in players_cards[player]:
        mast, number = i.values()
        print(str(players_cards[player].index(i) + 1) + ' -', number, mast, sep=' ')


@logger.catch()
def print_char(player, task):
    print('\n' * 100, f"очередь игрока {names[player]}", sep='')
    print('ваше действие - ' + task)
    print('ваши карты:')
    print_cards(player)
    print('козырь - ' + list(kos.values())[0])
    print("сейчас в колоде " + str(len(deck)) + " карты")


@logger.catch
def turn(player):  # универсальная функция для хода
    if ber_stat[player] == False:
        table_cards = []
        otb_table_cards = []
        players_pass = []
        for i in range(len(names)):
            players_pass.append(0)
        for i in range(len(names)):
            for o in range(6 - len(players_cards[i])):
                if len(deck) == 0 and len(players_cards[i]) == 0:
                    names.pop(i)
                    players_cards.pop(i)
                    tasks.pop(i)
                    ber_stat.pop(i)
                    over_players.append(i)
                    return 0
                elif len(deck) == 0:
                    print('в колоде не осталось карт')
                    break
                players_cards[i].append(deck[0])
                deck.pop(0)
        print_char(player, 'атака')
        for i in range(len(names)):
            if i == player:
                tasks[i] = 'attack'
            elif i == player + 1:
                tasks[i] = 'defend'
            else:
                tasks[i] = 'dop_attack'
        player2 = player + 1 if player + 1 < len(names) else 0
        # первоначальная атака
        print(f'вы играете под игрока {names[player2]}')
        while True:
            attack_cards = input('из своих карт, выберете какой хотите сходить и введите ее порядковый номер или введите пасс')
            if attack_cards == 'пасс':
                break
            else:
                attack_cards = int(attack_cards)
            table_cards.append(players_cards[player][attack_cards - 1])
            players_cards[player].pop(attack_cards - 1)
            print('теперь у вас на руках:')
            print_cards(player)
        # первоначальная защита
        print_char(player2, 'защита')
        while True:
            print('вы должны покрыть эти карты', end='\n')
            for i in table_cards:
                mast, card = i.values()
                print(mast, card)
            otb_card = input('из карт на столе выберете какую вы хотите покрыть и введите ее порядковый номер или введите беру')
            if otb_card == 'беру':
                for i in table_cards:
                    players_cards[player2].append(i)
                ber_stat[player2] = True
                return 0
            else:
                otb_card = int(otb_card)
                your_card = int(input('выберете из своих карт какой вы хотите покрыться и введите ее номер'))
                otb_table_cards.append(table_cards[otb_card - 1])
                otb_table_cards.append(players_cards[player2][your_card - 1])
                table_cards.pop(otb_card - 1)
                players_cards[player2].pop(your_card - 1)
                print('ваши карты:')
                print_cards(player2)
            if len(table_cards) == 0:
                break
        # остальной ход
        while players_pass.count(1) != len(names) - 1 and len(players_cards[player2]) > 0:
            print_char(player, 'дополнительная атака')
            print('на столе лежат эти карты:')
            for i in otb_table_cards:
                mast, number = i.values()
                print(number, mast, sep=' ', end='\n')
            print(f'вы играете под игрока {names[player2]}')
            while True:
                attack_cards = input('из своих карт, выберете какой хотите сходить и введите ее порядковый номер или введите пасс')
                print(table_cards, len(table_cards))
                if attack_cards == 'пасс':
                    if len(table_cards) == 0:
                        players_pass[player] = 1
                    break
                else:
                    attack_cards = int(attack_cards)
                table_cards.append(players_cards[player][attack_cards - 1])
                players_cards[player].pop(attack_cards - 1)
                print('теперь у вас на руках:')
                print_cards(player)
                print('НАПОМИНАНИЕ: на столе лежат эти карты(не считая тех которые были добавлены в дополнительную атаку:')
                for i in otb_table_cards:
                    mast, number = i.values()
                    print(number, mast, sep=' ', end='\n')

            for iterate in range(len(names)):
                if tasks[iterate] != 'defend' and tasks[iterate] != 'attack':
                    print_char(iterate, 'дополнительная атака')
                    print('на столе лежат эти карты:')
                    for i in otb_table_cards:
                        mast, number = i.values()
                        print(number, mast, sep=' ', end='\n')
                    print(f'вы играете под игрока {names[player2]}')
                    while True:
                        attack_cards = input('из своих карт, выберете какой хотите сходить и введите ее порядковый номер или введите пасс')
                        if attack_cards == 'пасс':
                            if len(table_cards) == 0:
                                players_pass[iterate] = 1
                            break
                        else:
                            attack_cards = int(attack_cards)
                        table_cards.append(players_cards[iterate][attack_cards - 1])
                        players_cards[iterate].pop(attack_cards - 1)
                        print('теперь у вас на руках:')
                        for i in players_cards[iterate]:
                            mast, number = i.values()
                            print(number, mast, sep=' ', end='\n')
                        print('НАПОМИНАНИЕ: на столе лежат эти карты(не считая тех которые были добавлены в дополнительную атаку:')
                        for i in otb_table_cards:
                            mast, number = i.values()
                            print(number, mast, sep=' ', end='\n')
                    print_char(player2, 'защита')
                    while True:
                        print('вы должны покрыть эти карты', end='\n')
                        for i in table_cards:
                            mast, card = i.values()
                            print(mast, card)
                        otb_card = input(
                            'из карт на столе выберете какую вы хотите покрыть и введите ее порядковый номер или введите беру')
                        if otb_card == 'беру':
                            for i in table_cards:
                                players_cards[player2].append(i)
                            ber_stat[player2] = True
                            return 0
                        else:
                            otb_card = int(otb_card)
                            your_card = int(
                                input('выберете из своих карт какой вы хотите покрыться и введите ее номер'))
                            otb_table_cards.append(table_cards[otb_card - 1])
                            otb_table_cards.append(players_cards[player2][your_card - 1])
                            table_cards.pop(otb_card - 1)
                            players_cards[player2].pop(your_card - 1)
                            print('ваши карты:')
                            print_cards(player2)
                        if len(table_cards) == 0:
                            break
        else:
            ber_stat[player] = False

with open('разрешение_на_игру.txt') as file:
    if any(i == '____ok____alright____\n' for i in file):
        hi()
        for i in range(10000):
            if len(over_players) > len(names) - 2:
                break
            for k in range(len(names)):
                if k > len(names):
                    turn((k + 1) % len(names))
                else:
                    turn(k % len(names))
        print(f'игра законченна, дураком остался {names[0]}')
    else:
        print('игра запрещена')
