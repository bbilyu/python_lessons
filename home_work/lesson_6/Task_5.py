# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# in
# 10 True
#
# out
#
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']
#
# in
# 10 False
#
# out
#
# ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый', 'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый', 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']


from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def creating_jokes(quantity: int, uniqueness: bool):
    if uniqueness == True:
        joke_list = []
        for _ in range(len(min(nouns, adverbs, adjectives))):
            nouns_tmp, adverbs_tmp, adjectives_tmp = choice(nouns), choice(adverbs), choice(adjectives)
            joke_list.append(f"{nouns_tmp} {adverbs_tmp} {adjectives_tmp}")
            nouns.remove(nouns_tmp), adverbs.remove(adverbs_tmp), adjectives.remove(adjectives_tmp)
        print(joke_list)
    else:
        print([f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}" for _ in range(quantity)])


creating_jokes(int(input("Enter integer number: ")), True)
