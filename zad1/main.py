from grammar import parse
from evaluator import NumeralsNormalizer, NumeralsTransformer
from math import *


if __name__ == "__main__":

    data = ('''minus otwórz nawias osiemset trzy miliony dwieście osiemdziesiąt sześć tysięcy dziewięćdziesiąt jeden dodać siedem zamknij nawias'''
            '''podzielić przez otwórz nawias minus cztery razy minus trzy zamknij nawias '''
            '''pomnóż przez dziewięć minus sinus cosinus dziewięćdziesięciu ośmiu minus sinus jeden razy cosinus jeden plus minus otwórz nawias minus czterdzieści pięć zamknij nawias do potęgi dwa do potęgi minus dwa''')

    normalizer = NumeralsNormalizer("numerals.txt")
    transformer = NumeralsTransformer(normalizer)

    result = parse(transformer.replace_with_numbers(data))

    print(eval(result))
