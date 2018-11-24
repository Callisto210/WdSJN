from grammar import parse
from evaluator import NumeralsNormalizer, NumeralsTransformer
from math import *

if __name__ == "__main__":
    normalizer = NumeralsNormalizer("numerals.txt")
    transformer = NumeralsTransformer(normalizer)

    with open("examples.txt") as f:
        examples = f.readlines()

    for example in examples:
        print(example)
        result = parse(transformer.replace_with_numbers(example))
        print(str(eval(result)) + "\n")
