import sys
from math import gcd
from typing import List

def prefix_gcds(a: List[int]) -> List[int]:
    if not a:
        return []
    
    n = len(a)
    pref = [0] * n
    pref[0] = abs(a[0])
    
    for i in range(1, n):
        pref[i] = gcd(pref[i-1], abs(a[i]))
        
    return pref

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]
        
        pref = prefix_gcds(a)
        
        results = []
        for _ in range(q):
            r = int(next(iterator))
            results.append(str(pref[r]))
            
        print('\n'.join(results))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
