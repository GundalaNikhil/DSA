import sys

def range_sigma(L: int, R: int) -> int:
    MOD = 1000000007
    sigma = [0] * (R + 1)
    
    for i in range(1, R + 1):
        for j in range(i, R + 1, i):
            sigma[j] += i
            
    total = 0
    for i in range(L, R + 1):
        total = (total + sigma[i]) % MOD
        
    return total

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    L = int(data[0])
    R = int(data[1])
    print(range_sigma(L, R))

if __name__ == "__main__":
    main()
