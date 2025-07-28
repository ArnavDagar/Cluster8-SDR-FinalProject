from imports import *

def decode_symbols(symbols, M = 2):
    
    L = int(math.log2(M))
    bits = []
    
    for symbol in symbols:
        if M == 2:
            if symbol == -1:
                decimal = 0
            elif symbol == 1:
                decimal = 1
                
        elif M == 4:
            if symbol == 3:
                decimal = 0
            elif symbol == 1:
                decimal = 1
            elif symbol == -1:
                decimal = 2
            elif symbol == -3:
                decimal = 3
                
        elif M == 8:
            if symbol == -7:
                decimal = 0
            elif symbol == -5:
                decimal = 1
            elif symbol == -3:
                decimal = 2
            elif symbol == -1:
                decimal = 3
            elif symbol == 1:
                decimal = 4
            elif symbol == 3:
                decimal = 5
            elif symbol == 5:
                decimal = 6
            elif symbol == 7:
                decimal = 7
        
        bit_group = []
        for i in range(L):
            power = L - 1 - i
            bit = (decimal >> power) & 1
            bit_group.append(bit)
        
        bits.extend(bit_group)
    
    return bits 