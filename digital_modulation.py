from imports import *

def digital_modulation(bits, M):

    L = int(math.log2(M))
    N = int(len(bits) // L)

    symbols = []

    for i in range(N):
        bit_group = []
        start_index = i * L
        
        for j in range(L):
            current_index = start_index + j
            bit_group.append(bits[current_index])

        decimal = 0
        for j, bit in enumerate(bit_group):
            power = L - 1 - j
            decimal += bit * (2 ** power)

        if M == 2:
            if decimal == 0:
                symbols.append(-1)
            elif decimal == 1:
                symbols.append(1)
                
        elif M == 4:
            if decimal == 0:
                symbols.append(3)
            elif decimal == 1:
                symbols.append(1)
            elif decimal == 2:
                symbols.append(-1)
            elif decimal == 3:
                symbols.append(-3)
                
        elif M == 8:
            if decimal == 0:
                symbols.append(-7)
            elif decimal == 1:
                symbols.append(-5)
            elif decimal == 2:
                symbols.append(-3)
            elif decimal == 3:
                symbols.append(-1)
            elif decimal == 4:
                symbols.append(1)
            elif decimal == 5:
                symbols.append(3)
            elif decimal == 6:
                symbols.append(5)
            elif decimal == 7:
                symbols.append(7)

    return symbols