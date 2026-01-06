import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return
        
    
    prefix_counts = {0: 1}
    curr_sum = 0
    ans = 0
    
    for x in a:
        curr_sum = (curr_sum + x) % m
        count = prefix_counts.get(curr_sum, 0)
        ans += count
        prefix_counts[curr_sum] = count + 1
        
    print(ans)

if __name__ == "__main__":
    solve()
