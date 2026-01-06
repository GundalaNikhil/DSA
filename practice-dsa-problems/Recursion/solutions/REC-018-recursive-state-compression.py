import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        a.append(int(input_data[ptr]))
        ptr += 1
        
    # Check if sum(a) divisible by m
    # Simple check, no complex recursion needed actually?
    # Filename says "recursive state compression", maybe simple mod sum is recursive in spirit?
    if sum(a) % m == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
