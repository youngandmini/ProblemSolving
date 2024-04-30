from itertools import product

def solution(word):
    chars = ["A","E","I","O","U"]
    
    words = []
    
    for length in range(1, 6):
        for prod in product(chars, repeat=length):
            words.append("".join(prod))
    
    words.sort()
    return words.index(word)+1