from imports import *
from digital_modulation import digital_modulation

def encode_bits(bits, M = 2):
    
    symbols = digital_modulation(bits, M)
    
    return symbols 