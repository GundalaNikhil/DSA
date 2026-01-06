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

    if n == 0:
        print(0)
        return
    if n == 1:
        print(1) # Is a single element a peak? Original code printed 1.
        return
        
    count = 0
    for i in range(n):
        prev_idx = (i - 1 + n) % n
        next_idx = (i + 1) % n
        if a[i] > a[prev_idx] and a[i] > a[next_idx]:
            count += 1
            
    print(count)

if __name__ == "__main__":
    solve()
