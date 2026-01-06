import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        d = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return


    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
        
    res = []
    for j in range(n):
        l = max(0, j - d)
        r = min(n - 1, j + d)
        
        # Sum is pref[r+1] - pref[l]
        total = pref[r + 1] - pref[l]
        res.append(str(total))
        
    print(*(res))

if __name__ == "__main__":
    solve()
