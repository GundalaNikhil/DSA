import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    q = int(input_data[1])
    ptr = 2
    for _ in range(q):
        l = int(input_data[ptr]) - 1
        r = int(input_data[ptr + 1]) - 1
        ptr += 2
        sub = s[l : r + 1]
        m = len(sub)
        ans = 0
        for i in range(m):
            num = 0
            for j in range(i, m):
                num = (num << 1) | int(sub[j])
                ans ^= num
                
        print(ans)


if __name__ == "__main__":
    solve()
