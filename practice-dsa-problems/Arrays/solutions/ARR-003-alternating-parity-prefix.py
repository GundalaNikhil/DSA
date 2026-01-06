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
        
    
    length = 1
    for i in range(1, n):
        if (a[i] % 2) != (a[i-1] % 2):
            length += 1
        else:
            break
            
    print(length)

if __name__ == "__main__":
    solve()
