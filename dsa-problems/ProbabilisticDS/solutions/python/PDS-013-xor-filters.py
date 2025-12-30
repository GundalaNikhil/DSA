import math
import sys

def xor_filter_stats(n: int, b: int):
    cells = math.ceil(1.23 * n)
    mem = int(cells * b)
    fpr = 2.0 ** -b
    return mem, fpr

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    b = int(data[1])
    mem, fpr = xor_filter_stats(n, b)
    print(f"{mem} {fpr:.6f}")

if __name__ == "__main__":
    main()
