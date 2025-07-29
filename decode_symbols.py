from imports import *

def decode_symbols(symbols, M = 2):
    
    L = int(math.log2(M))
    bits = []
    
    for symbol in symbols:
        decimal = 0
        
        if M == 2:
            # Fix phase inversion: swap the mapping
            if abs(symbol - (-1)) < abs(symbol - 1):
                decimal = 1  # Changed from 0
            else:
                decimal = 0  # Changed from 1
                
        elif M == 4:
            # Fix for M=4 (swap constellation mapping)
            distances = [abs(symbol - 3), abs(symbol - 1), abs(symbol - (-1)), abs(symbol - (-3))]
            min_idx = distances.index(min(distances))
            # Invert the mapping
            mapping = [1, 0, 3, 2]  # Inverted from [0, 1, 2, 3]
            decimal = mapping[min_idx]
                
        elif M == 8:
            constellation = [-7, -5, -3, -1, 1, 3, 5, 7]
            distances = [abs(symbol - point) for point in constellation]
            min_idx = distances.index(min(distances))
            # Invert the mapping
            mapping = [7, 6, 5, 4, 3, 2, 1, 0]  # Inverted from [0, 1, 2, 3, 4, 5, 6, 7]
            decimal = mapping[min_idx]
        
        bit_group = []
        for i in range(L):
            power = L - 1 - i
            bit = (decimal >> power) & 1
            bit_group.append(bit)
        
        bits.extend(bit_group)
    
    return bits