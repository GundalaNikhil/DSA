import sys

def check(mid, a, n, k_seg):
    count = 1
    curr_sum = 0
    for x in a:
        if x > mid:
            return False
            
        if curr_sum + x > mid:
            count += 1
            curr_sum = x
        else:
            curr_sum += x
            
    return count <= k_seg

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k_seg = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    
    
    low = max(a) if a else 0 
    high = sum(a) 
    
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid, a, n, k_seg):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == "__main__":
    solve()
