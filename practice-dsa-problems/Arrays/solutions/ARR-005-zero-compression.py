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
    
    res = []
    in_zero_block = False
    
    for x in a:
        if x != 0:
            res.append(x)
            in_zero_block = False
        else:
            if not in_zero_block:
                res.append(0)
                in_zero_block = True
    
    print(len(res))
    print(*(res))

if __name__ == "__main__":
    solve()
