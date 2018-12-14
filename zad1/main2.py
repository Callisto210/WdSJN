from grammar import parse
from evaluator import NumeralsNormalizer, NumeralsTransformer
from math import *
from socket import * 
from string import *

if __name__ == "__main__":
    normalizer = NumeralsNormalizer("numerals.txt")
    transformer = NumeralsTransformer(normalizer)

    UDPSock = socket(AF_INET,SOCK_DGRAM) 
    UDPSock.bind(('',1964)) 

    # Receive messages 
    while True: 
        data,addr = UDPSock.recvfrom(1964) 
        if not data: 
            print ("Program has exited!") 
            break 
        else: 
            example = data.decode('utf-8').ljust(500)
            example = example.lower()
            try:
                print(example)
                result = parse(transformer.replace_with_numbers(example))
                print(str(eval(result)) + "\n")
            except TypeError:
                pass

    UDPSock.close()
