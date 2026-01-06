import sys

MOD = 10**9 + 7
BASE = 31


class OnlinePalindrome:
    def __init__(self, max_q=200000):
        self.s = []
        self.n = 0
        self.pow_base = [1] * (max_q + 1)
        for i in range(1, max_q + 1):
            self.pow_base[i] = (self.pow_base[i - 1] * BASE) % MOD
            self.ft_fwd = [0] * (max_q + 1)
            self.ft_bwd = [0] * (max_q + 1)
            self.max_idx = max_q

    def update(self, ft, i, delta):
        while i <= self.max_idx:
            ft[i] = (ft[i] + delta) % MOD
            i += i & (-i)

    def query(self, ft, i):
        res = 0
        while i > 0:
            res = (res + ft[i]) % MOD
            i -= i & (-i)
            
        return res

    def append(self, char):
        self.n += 1
        val = ord(char) - ord("a") + 1
        self.s.append(char)
        fwd_delta = (val * self.pow_base[self.n - 1]) % MOD
        self.update(self.ft_fwd, self.n, fwd_delta)
        bwd_delta = (val * self.pow_base[self.max_idx - self.n]) % MOD
        self.update(self.ft_bwd, self.n, bwd_delta)

    def is_palindrome(self, l, r):
        l += 1
        r += 1
        length = r - l + 1
        if length <= 1:
            return True
        h_fwd = (self.query(self.ft_fwd, r) - self.query(self.ft_fwd, l - 1)) % MOD
        h_bwd = (self.query(self.ft_bwd, r) - self.query(self.ft_bwd, l - 1)) % MOD
        val_fwd = (h_fwd * self.pow_base[self.max_idx - l + 1]) % MOD
        val_bwd = (h_bwd * self.pow_base[r]) % MOD
        return val_fwd == val_bwd


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    q = int(input_data[0])
    op = OnlinePalindrome(q)
    for i in range(1, 1 + q):
        line = input_data[i].split()
        if line[0] == "APPEND":
            op.append(line[1])
        elif line[0] == "QUERY":
            print("YES" if op.is_palindrome(int(line[1]), int(line[2])) else "NO")


if __name__ == "__main__":
    solve()
