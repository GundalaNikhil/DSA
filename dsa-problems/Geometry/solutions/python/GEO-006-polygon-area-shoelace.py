from typing import List

def polygon_area(xs: List[int], ys: List[int]) -> int:
    n = len(xs)
    total = 0
    for i in range(n):
        j = (i + 1) % n
        total += xs[i] * ys[j] - xs[j] * ys[i]
    return abs(total) // 2

if __name__ == "__main__":
    main()
