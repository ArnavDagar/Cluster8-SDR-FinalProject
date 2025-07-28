from imports import *

def create_message(symbols, K = 5):
    
    symbols = np.array(symbols)
    
    m_t = np.repeat(symbols, K)
    
    return m_t