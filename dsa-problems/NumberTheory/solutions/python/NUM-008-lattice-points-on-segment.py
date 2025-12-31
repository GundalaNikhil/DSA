import sys
from math import gcd

def lattice_points(x1: int, y1: int, x2: int, y2: int) -> int:
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return gcd(dx, dy) + 1

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    x1, y1, x2, y2 = map(int, data)
    print(lattice_points(x1, y1, x2, y2))

if __name__ == "__main__":
    main()
