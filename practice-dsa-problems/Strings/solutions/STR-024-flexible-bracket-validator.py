import sys


def solve():
    s = sys.stdin.read().strip()
    if not s:
        print("true")
        return
    min_open = 0
    max_open = 0
    for char in s:
        if char == "(":
            min_open += 1
            max_open += 1
        elif char == ")":
            min_open -= 1
            max_open -= 1
        elif char == "*":
            min_open -= 1
            max_open += 1
            if max_open < 0:
                print("false")
                return
            if min_open < 0:
                min_open = 0
                
    if min_open == 0:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    solve()
