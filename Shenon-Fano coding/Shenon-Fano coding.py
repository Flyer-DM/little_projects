from collections import Counter
from fractions import Fraction
from math import log


def get_letter_chances(message: str) -> tuple:
    letters = dict(Counter(message))
    message_length = len(message)
    letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))
    letter_chances = {i: Fraction(letters[i], message_length) for i in letters}
    entropy = -(sum(map(lambda x: letter_chances[x] * log(letter_chances[x]), letter_chances)))
    entropy = round(entropy, 1)
    letter_chances = dict(sorted(letter_chances.items(), key=lambda x: x[1], reverse=True))
    return letter_chances, entropy


Code = [] 


def splitter(group: list, code=None, where=None) -> None:
    half = sum([i[1] for i in group]) / 2
    left, right = [], []
    sum_right = Fraction(0, 1)
    for i in range(len(group)):
        if sum_right + group[i][1] >= half:
            left.append(group[i])
            right.extend(group[i+1:])
            break
        else:
            left.append(group[i])
            sum_right += group[i][1]

    if len(left) == 1 and code is None and where is None:
        Code.append((left[0], '0'))
        if len(right) == 1:
            Code.append((right[0], '1'))
        else:
            splitter(right, '1', 'r')
    if len(left) > 1 and code is None and where is None:
        splitter(left, '0', 'l')
        if len(right) == 1:
            Code.append((right[0], '1'))
        else:
            splitter(right, '1', 'r')
    if len(left) > 1 and where == 'l':
        c = code + '0'
        splitter(left, c, 'l')
        c = code + '1'
        if len(right) == 1:
            Code.append((right[0], c))
        else:
            splitter(right, c, 'l')
    if len(left) == 1 and where == 'l':
        c = code + '0'
        Code.append((left[0], c))
        c = code + '1'
        if len(right) == 1:
            Code.append((right[0], c))
        else:
            splitter(right, c, 'l')

    if len(right) > 1 and where == 'r':
        c = code + '1'
        splitter(right, c, 'r')
        c = code + '0'
        if len(left) == 1:
            Code.append((left[0], c))
        else:
            splitter(left, c, 'r')
    if len(right) == 1 and where == 'r':
        c = code + '1'
        Code.append((right[0], c))
        c = code + '0'
        if len(left) == 1:
            Code.append((left[0], c))
        else:
            splitter(left, c, 'r')


def encode(letter_chances: dict, entropy: float) -> dict:
    group = list(letter_chances.items())
    splitter(group)
    encoded_chances = Code.copy()
    encoded_chances.sort(key=lambda x: x[0][1], reverse=True)
    lengths = Counter([len(i[1]) for i in encoded_chances])
    lengths_sum = len(encoded_chances)
    math_expect = sum(map(lambda x: x * Fraction(lengths[x], lengths_sum), lengths))
    math_expect = round(float(math_expect), 3)
    code_economy = round(entropy / math_expect, 3)
    beauty_encoded_chances = {i[0][0]: i[1] for i in encoded_chances}
    print("Математическое ожидание длины закодированной буквы равно", math_expect)
    print("Экономность кода равна", code_economy)
    return beauty_encoded_chances
    

def get_codes(codes: dict) -> None:
    for symbol in codes:
        print("|Символ {0:1} закодирован как {1:10}|".format(symbol, codes[symbol]))
    


test0, test1 = get_letter_chances('дверь_коридор_лестница')
get_codes(encode(test0, test1))
