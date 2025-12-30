import math
import sys

def design_bloom(n: int, f: float):
    ln2 = math.log(2)
    
    # Calculate m
    m_float = -(n * math.log(f)) / (ln2 ** 2)
    m = math.ceil(m_float)
    
    # Calculate k
    k_float = (m / n) * ln2
    k = round(k_float)
    
    # Calculate actual FPR
    exponent = -(k * n) / m
    fpr = (1 - math.exp(exponent)) ** k
    
    return m, k, fpr

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    f = float(data[1])
    m, k, fpr = design_bloom(n, f)
    print(f"{m} {k} {fpr:.6f}")

if __name__ == "__main__":
    main()
