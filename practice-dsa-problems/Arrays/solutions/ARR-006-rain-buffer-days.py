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

    count = 0
    if n >= 3:
        for i in range(n - 2):
            if a[i] < 0 and a[i + 1] > 0 and a[i + 2] > 0:
                count += 1
                
    print(count)

if __name__ == "__main__":
    solve()
