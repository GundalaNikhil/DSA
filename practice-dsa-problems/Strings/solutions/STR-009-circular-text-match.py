import sys


def solve():
    content = sys.stdin.read().splitlines()
    s1 = content[0] if len(content) > 0 else ""
    s2 = content[1] if len(content) > 1 else ""
    if len(s1) != len(s2):
        print("false")
        return
    if s2 in (s1 + s1):
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    solve()
