import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k_limit = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return


    if n <= 2:
        print(n)
        return
        
    is_peak = [False] * n
    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            is_peak[i] = True
            
    ans = 0
    l = 0
    curr_peaks = 0
    # Range [l, r]. Peaks valid in [l+1, r-1].
    
    for r in range(n):
        # Add r. New candidate peak at r-1.
        if r > 0 and is_peak[r - 1]:
            curr_peaks += 1
            
        while curr_peaks > k_limit:
            # Contract from left.
            # Current window [l, r]. Peaks in [l+1, r-1].
            # Move to [l+1, r]. Peaks in [l+2, r-1].
            # Losing check at l+1.
            if is_peak[l + 1]:
                curr_peaks -= 1
            l += 1
            
        ans = max(ans, r - l + 1)
        
    print(ans)

if __name__ == "__main__":
    solve()
