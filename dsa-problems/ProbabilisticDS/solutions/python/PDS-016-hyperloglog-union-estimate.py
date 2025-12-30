import math
import sys

def hll_union_estimate(m: int, a, b):
    if m == 16:
        alpha = 0.673
    elif m == 32:
        alpha = 0.697
    elif m == 64:
        alpha = 0.709
    else:
        alpha = 0.7213 / (1.0 + 1.079 / m)
        
    sum_val = 0.0
    for val_a, val_b in zip(a, b):
        val = max(val_a, val_b)
        sum_val += math.pow(2.0, -val)
            
    return alpha * m * m / sum_val

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    # The next m integers are A
    a = []
    idx = 1
    for _ in range(m):
        a.append(int(data[idx]))
        idx += 1
    # The next m integers are B
    b = []
    for _ in range(m):
        b.append(int(data[idx]))
        idx += 1
        
    print(f"{hll_union_estimate(m, a, b):.6f}")

if __name__ == "__main__":
    main()
