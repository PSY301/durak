import random
import itertools
from collections import namedtuple
import durak_funcs
from loguru import logger

logger.add('for_durak.log', format="{time} {level} {message}", level='DEBUG')


@logger.catch
def game(n):

    # функция для замены карт 11, 12, 13 или 14
    def card_convert(card):
        return obr_list[card - 11]

    # функция для вывода карт
    def print_cards(player):
        for z in players[player].cards:
            if z[1] > 10:
                print(players[player].cards.index(z) + 1, "-", z[0], card_convert(z[1]), sep=" ")
            else:
                print(players[player].cards.index(z) + 1, "-", z[0], z[1], sep=" ")

    # функция для вывода характеристики игрока
    def print_char(player, task):
        print("\n" * 100, f"очередь игрока {players[player].name}", sep="")
        print("ваше действие -", task)
        print("ваши карты:")
        print_cards(player)
        print("козырь -", kos[0])
        print("сейчас в колоде", len(deck), "карты")
        print("сейчас в игре", n, "игрока")

    # функция для атаки
    def attack(player, player2, task="атака"):
        if len(players[player].cards) != 0:
            print_char(player, task)
            print(f"вы играете под игрока {players[player2].name}")
            if task == "дополнительная атака":
                print("карты на столе")
                for j in table[1]:
                    print(j[0], j[1] if j[1] < 11 else card_convert(j[1]))
                for j in table[0]:
                    print(j[0], j[1] if j[1] < 11 else card_convert(j[1]))
            player_cards_length = len(players[player].cards)
            player2_cards_length = 6 if len(players[player2].cards) + len(table[1]) / 2 > 6 \
                else len(players[player2].cards) + len(table[1]) / 2
            while len(table[1]) // 2 + len(table[0]) <= player2_cards_length - 1:
                attack_card = durak_funcs.auto_error_fix(slice(1, len(players[player].cards)), "пас",
                                                         usl="введите порядковый номер карты, "
                                                             "которой хотите сыграть или введите пас ")
                mb_crd = [k[1] for k in table[0]]
                for t in table[1]:
                    mb_crd.append(t[1])
                if attack_card == "пас":
                    if task == "дополнительная атака" and player_cards_length == len(players[player].cards):
                        return 1
                    else:
                        return 0
                elif (len(table[0]) == 0 and len(table[1]) == 0) \
                        or players[player].cards[attack_card - 1][1] in mb_crd:
                    attack_card = int(attack_card)
                    table[0].append(players[player].cards[attack_card - 1])
                    players[player].cards.pop(attack_card - 1)
                    print("теперь у вас на руках:")
                    print_cards(player)
                else:
                    print("вы жульничаете!")
            return 0

        return 1

    # функция для защиты
    def defend(player2):
        print_char(player2, "защита")
        while len(table[0]) != 0:
            print("карты на столе", end="\n")
            for j in table[0]:
                print(f"{table[0].index(j) + 1} -", j[0], j[1] if j[1] < 11 else card_convert(j[1]))
            otb_card = durak_funcs.auto_error_fix(slice(1, len(table[0])), "беру",
                                                  message="",
                                                  usl="из карт на столе выберете ту, "
                                                  "которую хотите покрыть и введите ее порядковый номер "
                                                  "или введите беру ")
            otb_card = durak_funcs.is_int(otb_card)
            if type(otb_card) == str:
                for k in table[0]:
                    players[player2].cards.append(k)
                for k in table[1]:
                    players[player2].cards.append(k)
                return 2
            your_card = durak_funcs.auto_error_fix(slice(1, len(players[player2].cards)), "беру",
                                                   usl="введите порядковый номер карты, "
                                                   "которой хотите покрыться или введите беру ")
            your_card = durak_funcs.is_int(your_card)
            if type(your_card) == str:
                for k in table[0]:
                    players[player2].cards.append(k)
                for k in table[1]:
                    players[player2].cards.append(k)
                return 2
            else:
                defend_card = players[player2].cards[your_card - 1]
                pok_card = table[0][otb_card - 1]
                if (defend_card[0] == pok_card[0]
                    and defend_card[1] > pok_card[1]) \
                        or (defend_card[0] == kos[0] and pok_card[0] != kos[0]):
                    table[1].append(pok_card)
                    table[1].append(defend_card)
                    table[0].pop(otb_card - 1)
                    players[player2].cards.pop(your_card - 1)
                else:
                    print("вы жульничаете!")
                print("ваши карты:")
                print_cards(player2)
        return 0

    # программа для запуска
    need_name = 0
    while n > 1:
        table[0] = []
        table[1] = []
        iter_names = []
        names = [r.name for r in players]
        otb_player = need_name + 1 if need_name + 1 < n else 0
        for u in range(1, n):
            next_name = names[need_name + u] if need_name + u < n else names[u - (n - need_name)]
            iter_names.append(next_name)
        if players_status[need_name] != 2:
            players_status[need_name] = attack(player=need_name, player2=otb_player, task="атака")
            players_status[otb_player] = defend(player2=otb_player)
            if players_status[otb_player] != 2:
                otb_player_cards_length = 6 if len(players[otb_player].cards) > 6 \
                    else len(players[otb_player].cards)
                while len(players[otb_player].cards) != 0 and \
                        len(table[1]) // 2 + len(table[0]) <= otb_player_cards_length and \
                        players_status.count(1) != n - 1:
                    players_status[need_name] = attack(player=need_name, player2=otb_player,
                                                       task="дополнительная атака")
                    for e in range(n):
                        if e != otb_player and e != need_name:
                            players_status[e] = attack(player=e, player2=otb_player, task="дополнительная атака")
                    players_status[otb_player] = defend(player2=otb_player)
                    if players_status[otb_player] == 2:
                        break
        else:
            players_status[need_name] = 0
        minus_for_loop = 0
        for e in range(n):
            e -= minus_for_loop
            for _ in range(6 - len(players[e].cards)):
                if len(deck) != 0:
                    players[e].cards.append(deck[0])
                    deck.pop(0)
                elif len(players[e].cards) == 0:
                    if n != 1:
                        minus_for_loop += 1
                        players.pop(e)
                        players_status.pop(e)
                        n -= 1
                    break
                else:
                    break
        if n < 2:
            print(f"игра законченна, дураком остался {players[0].name}")
            break
        for g in iter_names:
            if g in names:
                need_name = names.index(g)
                break


if __name__ == "__main__":
    # инициализация колоды
    deck_len = durak_funcs.auto_error_fix(36, 52,
                                          message="вы хотите играть колодой в 36 карт или в 52 карты?",
                                          usl="введите 36 или 52 ")
    obr_list = ["валет", "дама", "король", "туз"]
    if deck_len == 36:
        lists = [["черви", "бубе", "пики", "крести"],
                 [6, 7, 8, 9, 10, 11, 12, 13, 14]]
        deck = list(itertools.product(*lists))
    else:
        lists = [["черви", "бубе", "крести", "пики"],
                 [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
        deck = list(itertools.product(*lists))
    random.shuffle(deck)
    # козырь
    kos = deck[0]
    deck[0], deck[deck_len - 1] = deck[deck_len - 1], deck[0]
    # инициализация стола
    table = [[], []]
    # инициализация игроков
    value_of_people = durak_funcs.auto_error_fix(slice(2, 8),
                                                 message="сколько игроков будет играть?",
                                                 usl="введите цифру от 2 до 8 ")
    Player = namedtuple("Player", ["name", "cards"])
    players = []
    players_status = []
    for i in range(value_of_people):
        name = input(f"введите имя {i + 1} игрока ")
        cards = []
        for _ in range(6):
            cards.append(deck[0])
            deck.pop(0)
        players.append(Player(name=name, cards=cards))
        # инициализация статуса игроков
        # возможные статусы: готов=0, пас=1, беру=2
        players_status.append(0)
    game(value_of_people)


# PROBLEMS:
# 1 - из-за именного кортежа в players не получается объединить players_status и players.
# 2 - неправильное построение основного цикла (смотреть РЕЦЕПТ ОТ ЮРЫ в конце main.py).
# 3 - пока что нет говорения игроку что он ввел 2 или больше одинаковых имен.
# 4 - при выводе некоторых слов моя программа не учитывает их склонения.
# 5 - если в первоначальной атаки написать первым словом пас, то программа не будет считать это как ошибку.
# 6 - в моей игре нельзя подкидывать карты после беру
