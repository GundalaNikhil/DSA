import sys

def count_ways(n: int, jumps):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for jump in jumps:
            if i >= jump:
                dp[i] = (dp[i] + dp[i - jump]) % MOD
                
    return dp[n]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    jumps = [int(x) for x in data[2:]]
    print(count_ways(n, jumps))

if __name__ == "__main__":
    main()
