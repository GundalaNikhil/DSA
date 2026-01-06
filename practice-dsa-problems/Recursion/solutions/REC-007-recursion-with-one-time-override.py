import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    l_limit = int(input_data[ptr])
    ptr += 1
    r_limit = int(input_data[ptr])
    ptr += 1
    invalid_count = 0
    for _ in range(n):
        val = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        if not (l_limit <= val <= r_limit):
            invalid_count += 1
            
    if invalid_count <= 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
