import sys


def get_grundy(n, l, r):
    return (n % (l + r)) // l


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    l = int(input_data[1])
    r = int(input_data[2])
    runs = []
    i = 0
    n = len(s)
    xor_sum = 0
    while i < n:
        char = s[i]
        j = i
        while j < n and s[j] == char:
            j += 1
            run_len = j - i
            xor_sum ^= get_grundy(run_len, l, r)
            i = j
        if xor_sum > 0:
            print("FIRST")
        else:
            print("SECOND")


if __name__ == "__main__":
    solve()
