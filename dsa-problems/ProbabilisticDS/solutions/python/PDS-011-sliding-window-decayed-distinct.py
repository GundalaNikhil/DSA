import math
import sys

def decayed_distinct(T: int, lam: float, times):
    total = 0.0
    for t in times:
        total += math.exp(-lam * (T - t))
    return total

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        T = int(next(iterator))
        lam = float(next(iterator))
        m = int(next(iterator))
        times = []
        for _ in range(m):
            times.append(int(next(iterator)))
            
        print(f"{decayed_distinct(T, lam, times):.6f}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
