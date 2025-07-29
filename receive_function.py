from imports import *
from decode_message import decode_message
from decode_symbols import decode_symbols

def receive_bits(sdr, expected_bits, M=2, K=5):
    
    print(f"Receiving {expected_bits} bits...")
    
    # Calculate expected signal length
    expected_symbols = expected_bits // int(np.log2(M))
    expected_samples = expected_symbols * K
    print(f"Expecting {expected_samples} samples ({expected_symbols} symbols)")
    
    # Step 1: Receive signal from SDR
    rx_signal = sdr.rx()
    print(f"Received {len(rx_signal)} samples")
    
    # Take only expected length
    rx_signal = rx_signal[:expected_samples]
    
    # Step 2: Convert signal to symbols
    symbols = decode_message(rx_signal, K)
    print(f"Decoded {len(symbols)} symbols")
    
    # Step 3: Convert symbols to bits
    data_bits = decode_symbols(symbols, M)
    print(f"Decoded {len(data_bits)} bits")
    
    # Take only expected number of bits
    data_bits = data_bits[:expected_bits]
    print("Reception complete!")
    
    return data_bits 