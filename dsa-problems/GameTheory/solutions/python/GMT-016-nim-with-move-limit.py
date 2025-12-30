from typing import List

def nim_limit(n: int, A: List[int], L: List[int]) -> str:
    xor_sum = 0
    for i in range(n):
        xor_sum ^= (A[i] % (L[i] + 1))
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
        A = []
        for _ in range(n):
            A.append(int(next(iterator)))
        L = []
        for _ in range(n):
            L.append(int(next(iterator)))
            
        print(nim_limit(n, A, L))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
