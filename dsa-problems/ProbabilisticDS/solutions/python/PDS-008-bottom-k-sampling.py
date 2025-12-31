import sys

def jaccard_estimate(a, b):
    matches = 0
    k = len(a)
    for i in range(k):
        if a[i] == b[i]:
            matches += 1
    return matches / k

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        a = []
        for _ in range(k):
            a.append(float(next(iterator)))
        b = []
        for _ in range(k):
            b.append(float(next(iterator)))
            
        print(f"{jaccard_estimate(a, b):.6f}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
