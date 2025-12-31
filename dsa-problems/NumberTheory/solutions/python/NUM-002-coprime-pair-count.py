import sys

def count_coprime_pairs(N: int) -> int:
    if N < 2:
        return 0
        
    phi = list(range(N + 1))
    
    for i in range(2, N + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, N + 1, i):
                phi[j] -= phi[j] // i
                
    return sum(phi[2:])

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    print(count_coprime_pairs(N))

if __name__ == "__main__":
    main()
