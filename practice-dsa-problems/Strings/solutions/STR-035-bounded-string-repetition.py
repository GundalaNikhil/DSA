import sys
import math
def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        return
    a = input_data[0]
    b = input_data[1]
    r_limit = int(input_data[2])
    n, m = len(a), len(b)
    base_reps = math.ceil(m / n)
    for reps in range(base_reps, base_reps + 3):
        if reps > r_limit:
            break
        pass
    test_str = a * (base_reps + 1)
    idx = test_str.find(b)
    if idx != -1:
        needed = math.ceil((idx + m) / n)
        if needed <= r_limit:
            print(needed)
        else:
            print("-1")
    else:
        print("-1")
if __name__ == '__main__':
    solve()