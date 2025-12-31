MOD = 1_000_000_007

def decode_ways(s: str) -> int:
    n = len(s)
    if n == 0 or s[0] == "0":
        return 0
    prev2 = prev1 = 1
    for i in range(1, n):
        c = s[i]
        pair = int(s[i-1:i+1])
        cur = 0
        if c != "0":
            cur = (cur + prev1) % MOD
            if pair == 20 or (10 < pair <= 26):
                cur = (cur + prev2) % MOD
        else:
            if pair == 20:
                cur = (cur + prev2) % MOD
        prev2, prev1 = prev1, cur
    return prev1 % MOD


def main():
    s = input().strip()
    print(decode_ways(s))

if __name__ == "__main__":
    main()
