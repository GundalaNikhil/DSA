import sys

def minimize_max_pair_xor(a: list[int]) -> int:
    n = len(a)
    memo = {}

    def solve(mask):
        if mask == (1 << n) - 1:
            return 0
        if mask in memo:
            return memo[mask]
        
        # Find first unset bit
        i = 0
        while (mask >> i) & 1:
            i += 1
            
        res = float('inf')
        
        # Try pairing i with j
        for j in range(i + 1, n):
            if not ((mask >> j) & 1):
                pair_xor = a[i] ^ a[j]
                rem_max = solve(mask | (1 << i) | (1 << j))
                res = min(res, max(pair_xor, rem_max))
        
        memo[mask] = res
        return res

    return solve(0)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
        
    result = minimize_max_pair_xor(a)
    print(result)

if __name__ == "__main__":
    main()
