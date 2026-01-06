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
        p = []
        for _ in range(n):
            p.append(int(next(iterator)))
    except StopIteration:
        return


    b = [a[i] * p[i] for i in range(n)]
    
    max_so_far = -float("inf")
    curr_max = 0
    

    for x in b:
        curr_max += x
        if curr_max > max_so_far:
            max_so_far = curr_max
        if curr_max < 0:
            curr_max = 0
            
    print(max_so_far)

if __name__ == "__main__":
    solve()
