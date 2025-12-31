import sys
from collections import Counter

def misra_gries(stream, k):
    counts = Counter()
    
    for x in stream:
        if x in counts:
            counts[x] += 1
        elif len(counts) < k - 1:
            counts[x] = 1
        else:
            # Decrement all
            to_remove = []
            for key in counts:
                counts[key] -= 1
                if counts[key] == 0:
                    to_remove.append(key)
            for key in to_remove:
                del counts[key]
                
    return sorted(counts.keys())

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        stream = []
        for _ in range(n):
            stream.append(int(next(iterator)))
            
        res = misra_gries(stream, k)
        print(" ".join(str(x) for x in res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
