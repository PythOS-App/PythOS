import math

def root(number, root=2, returnStr=False):
    if number < 0:
        res = complex(number) ** (1 / root)
        
        # Extract the real and imaginary parts
        real = res.real
        imag = res.imag
        
        # If either part is effectively zero, snap it to exactly 0.0
        if math.isclose(real, 0, abs_tol=1e-15):
            real = 0.0
        if math.isclose(imag, 0, abs_tol=1e-15):
            imag = 0.0
            
        # Reconstruct the cleaned complex number
        result = complex(real, imag)
    else:
        result = number ** (1 / root)

    if returnStr: 
        # 1. Convert to string and strip outer parentheses
        clean_str = str(result).strip('()')
        # 2. Swap j for i, then simplify 1i (and +1i / -1i) to just i
        return clean_str.replace('j', 'i').replace('1i', 'i')
    else:
        return result
