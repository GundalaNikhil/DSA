import sys
import math

def expected_height(n: int, p: float) -> float:
    # Avoid division by zero if p=1 (though constraints say p < 1)
    if p >= 1.0:
        return float('inf')
    return math.log(n) / math.log(1.0 / p)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    p = float(data[1])
    print(expected_height(n, p))

if __name__ == "__main__":
    main()
