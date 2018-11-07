from collections import defaultdict

from grammar import parse


def numerals_to_number(numerals, numwords={}):
    if not numwords:
        units = [
            "zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem",
            "dziewięć", "dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście",
            "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście",
        ]

        tens = [
            "", "", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt",
            "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"
        ]

        hundreds = [
            "", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset",
            "siedemset", "osiemset", "dziewięćset"
        ]

        scales = ["tysiąc", "milion", "miliard", "bilion"]

        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(hundreds):
            numwords[word] = (1, idx * 100)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 + 3), 0)

    current = result = 0
    for word in numerals:
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


def normalize_numerals(textnum, d=defaultdict(list)):
    if not d:
        with open("numerals.txt") as file:
            for line in file:
                forms = line.split(";")
                d[forms[1]].append(forms[0])

    normalized = [d.get(x, [x])[0] for x in textnum.split()]
    return " ".join(normalized)


def replace_numerals_with_numbers(text, numerals_list=[]):
    if not numerals_list:
        with open("numerals.txt") as file:
            for line in file:
                z = line.split(";")
                numerals_list.append(z[0])

    res = []
    numerals = []
    for word in text.split():
        if word in numerals_list:
            numerals.append(word)
        else:
            if numerals:
                res.append(numerals_to_number(numerals))
            res.append(word)
            numerals = []
    if numerals:
        res.append(numerals_to_number(numerals))
    return " ".join([str(r) for r in res])


data = ('''osiemset trzy miliony dwieście osiemdziesiąt trzy tysiące dziewięćdziesiąt trzy dodać pięć '''
        '''podzielić przez otwórz nawias cztery razy trzy zamknij nawias '''
        '''pomnóż przez dziewięć minus sinus dziewięćdziesięciu ośmiu plus czterdzieści pięć''')

result = parse(replace_numerals_with_numbers(normalize_numerals(data)))
from math import *
print(eval(result))
