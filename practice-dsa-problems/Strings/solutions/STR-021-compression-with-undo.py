import sys


def compress(s):
    if not s:
        return ""
    res = []
    i = 0
    n = len(s)
    while i < n:
        char = s[i]
        j = i
        while j < n and s[j] == char:
            j += 1
            res.append(f"{char}{j - i}")
            i = j
            
    return "".join(res)


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    s = input_data[0]
    q = int(input_data[1])
    history = [s]
    current = s
    for i in range(2, 2 + q):
        line = input_data[i].split()
        op = line[0]
        if op == "C":
            current = compress(current)
            history.append(current)
        elif op == "U":
            k = int(line[1])
            for _ in range(k):
                history.pop()
                current = history[-1]
                print(current)


if __name__ == "__main__":
    solve()
