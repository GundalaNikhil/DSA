import sys

def build_prefix_distinct(N: int):
    f = [0] * (N + 1)
    
    # Modified Sieve
    for i in range(2, N + 1):
        if f[i] == 0:  # i is prime
            for j in range(i, N + 1, i):
                f[j] += 1
                
    pref = [0] * (N + 1)
    for i in range(1, N + 1):
        pref[i] = pref[i-1] + f[i]
        
    return pref

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        N = int(next(iterator))
        q = int(next(iterator))
        
        pref = build_prefix_distinct(N)
        
        results = []
        for _ in range(q):
            l = int(next(iterator))
            r = int(next(iterator))
            results.append(str(pref[r] - pref[l-1]))
            
        print('\n'.join(results))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
