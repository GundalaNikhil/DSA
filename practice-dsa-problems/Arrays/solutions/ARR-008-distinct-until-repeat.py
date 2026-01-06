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
    
    seen = set()
    length = 0
    for x in a:
        if x in seen:
            break
        seen.add(x)
        length += 1
        
    print(length)

if __name__ == "__main__":
    solve()
