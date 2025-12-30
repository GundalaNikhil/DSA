from typing import List

def interval_removal_game(n: int, intervals: List[List[int]]) -> str:
    xor_sum = 0
    for l, r in intervals:
        length = r - l
        xor_sum ^= length
    return "First" if xor_sum > 0 else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        intervals = []
        for _ in range(n):
            l = int(next(iterator))
            r = int(next(iterator))
            intervals.append([l, r])
            
        print(interval_removal_game(n, intervals))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
