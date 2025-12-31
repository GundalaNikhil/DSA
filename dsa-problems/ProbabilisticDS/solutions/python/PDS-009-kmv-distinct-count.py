import sys

def kmv_estimate(hashes):
    k = len(hashes)
    if k == 0:
        return 0.0
    hk = hashes[-1]
    return (k - 1) / hk

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        k = int(next(iterator))
        hashes = []
        for _ in range(k):
            hashes.append(float(next(iterator)))
            
        print(f"{kmv_estimate(hashes):.6f}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
