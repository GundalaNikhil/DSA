import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    min_worst_case_per_step = float("inf")
    for _ in range(a_count):
        k = int(input_data[ptr])
        ptr += 1
        max_cost = -float("inf")
        for _ in range(k):
             cost = int(input_data[ptr])
             ptr += 1
             if cost > max_cost:
                 max_cost = cost
                 
        if max_cost < min_worst_case_per_step:
             min_worst_case_per_step = max_cost
             
    if min_worst_case_per_step != float("inf"):
        print(n * min_worst_case_per_step)
    else:
        print(0)


if __name__ == "__main__":
    solve()
