from typing import List

def take_or_split(n: int, heaps: List[int]) -> str:
    xor_sum = 0
    for x in heaps:
        xor_sum ^= (x - 1)
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
        heaps = []
        for _ in range(n):
            heaps.append(int(next(iterator)))
            
        print(take_or_split(n, heaps))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
