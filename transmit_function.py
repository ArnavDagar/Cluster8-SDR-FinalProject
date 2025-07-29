from imports import *
from encode_bits import encode_bits
from create_message import create_message

def transmit_bits(sdr, data_bits, M=2, K=5):

    print(f"Transmitting {len(data_bits)} bits...")
    
    # Step 1: Convert bits to symbols
    symbols = encode_bits(data_bits, M)
    print(f"Generated {len(symbols)} symbols")
    
    # Step 2: Convert symbols to continuous signal
    message_signal = create_message(symbols, K)
    print(f"Created message signal: {len(message_signal)} samples")
    
    # Step 3: Transmit through SDR
    sdr.tx(message_signal)
    print("Transmission complete!")
    
    return len(symbols), len(message_signal) 