# 4. ** Создайте программу для игры с конфетами человек против человека.

#    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#    Все конфеты оппонента достаются сделавшему последний ход.
#    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#    1. Добавьте игру против бота
#    2. Подумайте как наделить бота "интеллектом"

from random import shuffle

def bot_run(candies: int) -> int:
    if candies <= CANDIES_LIMIT:
        result = candies
    else:
        result = CANDIES_LIMIT
        cnt_step = candies // CANDIES_LIMIT
        if candies % CANDIES_LIMIT > 0:
            cnt_step += 1

        if cnt_step % 2 == 0:
            if candies - CANDIES_LIMIT < CANDIES_LIMIT:
                result = candies - (CANDIES_LIMIT - 1)
    return result


def check_wins():
    global rest_candies, active_player
    if get_candies not in range(1, CANDIES_LIMIT + 1):
        print('Wrong move!')
    else:
        rest_candies -= get_candies
        if rest_candies > 0:
            if "bot" in players:
                active_player = "human" if active_player == "bot" else "bot"
            else:
                active_player = "human" if active_player == "person" else "person"
        else:
            print(f'The player {active_player} won!')


def main():
    global get_candies
    while rest_candies > 0:
        print(f'\nThere are {rest_candies} sweets on the table, you can take [1 .. {CANDIES_LIMIT}]')
        print(f"Player {active_player}'s move")

        if active_player == "bot":
            get_candies = bot_run(rest_candies)
            print(f'The bot took {get_candies} candies')
        else:
            while True:
                get_candies = int(input(f'How many candies do you want {active_player}: '))
                if get_candies > rest_candies:
                    print("Wrong!Look at the remaining amount of candy")
                    continue
                else:
                    break
        check_wins()

# CANDIES = 2021
CANDIES = 117
CANDIES_LIMIT = 28
rest_candies = CANDIES

players = ["human", 'bot' if int(input('Play with bot 1 - yes, 0 - no? ')) else 'person']
shuffle(players)

active_player = players[0]
print(f'1 player - {players[0]}, 2 player - {players[1]}')

main()


