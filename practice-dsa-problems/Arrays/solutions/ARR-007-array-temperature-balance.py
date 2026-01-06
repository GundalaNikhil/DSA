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
    
    total_abs = sum(abs(x) for x in a)
    left_sum = 0
    
    for i in range(n):
        if left_sum == total_abs - left_sum - abs(a[i]):
            print(i + 1)
            return
        left_sum += abs(a[i])
        
    print("-1")

if __name__ == "__main__":
    solve()
