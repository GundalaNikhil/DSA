import sys

def total_size(sizes):
    S = 0
    for s in sizes:
        S += s * s
    return S

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        t = int(next(iterator))
        sizes = []
        for _ in range(t):
            sizes.append(int(next(iterator)))
            
        S = total_size(sizes)
        print(f"{S} {'YES' if S <= 4 * n else 'NO'}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
