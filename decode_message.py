from imports import *

def decode_message(m_t, K = 5):
    
    m_t = np.array(m_t)
    
    symbols = m_t[::K]
    
    return symbols 