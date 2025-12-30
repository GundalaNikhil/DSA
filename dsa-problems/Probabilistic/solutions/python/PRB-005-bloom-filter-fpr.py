import sys
import math

def bloom_fpr(m: float, k: float, n: float) -> float:
    exponent = -k * n / m
    term = 1.0 - math.exp(exponent)
    return math.pow(term, k)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = float(data[0])
    k = float(data[1])
    n = float(data[2])
    print(f"{bloom_fpr(m, k, n):.6f}")

if __name__ == "__main__":
    main()
