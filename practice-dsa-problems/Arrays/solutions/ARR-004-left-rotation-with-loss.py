import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    if n == 0:
        return
        
    k = k % n
    if k == 0:
        print(*(a))
        return
        
    
    wrapped = []
    for i in range(k):
        val = max(0, a[i] - 1)
        wrapped.append(val)
        
    res = a[k:] + wrapped
    print(*(res))

if __name__ == "__main__":
    solve()
