import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        target = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return


    if any(x > target for x in a):
        print("-1")
        return
        
    print(target - min(a))

if __name__ == "__main__":
    solve()
