import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    if n < 4:
        print("-1")
        return

    for i in range(n - 3):
        if a[i] < a[i + 1] < a[i + 2] < a[i + 3]:
            print(i + 1)
            return
            
    print("-1")

if __name__ == "__main__":
    solve()
