import math
import sys

def hll_estimate(m: int, registers):
    if m == 16:
        alpha = 0.673
    elif m == 32:
        alpha = 0.697
    elif m == 64:
        alpha = 0.709
    else:
        alpha = 0.7213 / (1.0 + 1.079 / m)
        
    sum_val = 0.0
    zeros = 0
    for val in registers:
        sum_val += math.pow(2.0, -val)
        if val == 0:
            zeros += 1
            
    E = alpha * m * m / sum_val
    
    if E <= 2.5 * m:
        if zeros > 0:
            E = m * math.log(m / zeros)
            
    return E

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    registers = list(map(int, data[1:]))
    print(f"{hll_estimate(m, registers):.6f}")

if __name__ == "__main__":
    main()
