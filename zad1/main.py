from grammar import parse
from evaluator import NumeralsNormalizer, NumeralsTransformer
from math import *

if __name__ == "__main__":
    normalizer = NumeralsNormalizer("numerals.txt")
    transformer = NumeralsTransformer(normalizer)

    with open("examples.txt") as f:
        for example in f:
            print("example: " + example.rstrip())
            result = parse(transformer.replace_with_numbers(example.lower()))
            print("parsed: " + result)
            try:
                print("result: " + str(eval(result)) + "\n")
            except:
                pass
