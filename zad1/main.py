from grammar import parse
from evaluator import NumeralsNormalizer, NumeralsTransformer
from math import *

from socket import * 
from string import * 

if __name__ == "__main__":

    UDPSock = socket(AF_INET,SOCK_DGRAM) 
    UDPSock.bind(('',1964))

    f = open("examples.txt", "a")


    normalizer = NumeralsNormalizer("numerals.txt")
    transformer = NumeralsTransformer(normalizer)

    while True: 
        data,addr = UDPSock.recvfrom(1969) 
        if not data: 
            print("Program has exited!") 
            break 
        else:
            x = data.decode('utf-8')
            f.write(x)
            f.write("\n")
            print(x.ljust(50), addr[0])
            try:
                result = parse(transformer.replace_with_numbers(x.lower()))
                print("result: " + str(eval(result)) + "\n")
            except:
                pass


    UDPSock.close()


    #normalizer = NumeralsNormalizer("numerals.txt")
    #transformer = NumeralsTransformer(normalizer)

    #with open("examples.txt") as f:
    #    examples = f.readlines()

    #for example in examples:
    #    print(example)
    #    result = parse(transformer.replace_with_numbers(example))
    #    print(str(eval(result)) + "\n")
