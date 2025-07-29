from imports import *
from receive_function import receive_bits
#import adi
from comms_lib.pluto import Pluto
#from cosmos_final import Pluto

def simple_receive(usb_address="usb:1.5.5", expected_bits=8, M=2, K=5):
    
    sdr = Pluto(usb_address)
    
    # Configure SDR
    sdr.sample_rate = int(1e6)
    sdr.rx_lo = int(915e6)
    sdr.rx_hardwaregain_chan0 = 30
    
    print(f"Connected to PlutoSDR at {usb_address}")
    print(f"Receiving {expected_bits} bits with M={M}, K={K}")
    
    # Receive the bits
    received_bits = receive_bits(sdr, expected_bits, M, K)
    
    print(f"Received bits: {received_bits}")
    
    return received_bits

if __name__ == "__main__":
    simple_receive() 