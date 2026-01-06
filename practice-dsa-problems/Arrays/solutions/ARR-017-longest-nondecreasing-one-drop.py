import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
    except StopIteration:
        return
        
    if n == 0:
        print(0)
        return
        
    a = []
    try:
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        pass # Handle incomplete input if any
        
    
    max_len = 0
    l = 0
    drops = 0
    
    # Handle single element
    if n > 0:
        max_len = 1
        
    for r in range(1, n):
        if a[r - 1] > a[r]:
            drops += 1
            
        while drops > 1:
            # removing a[l]
            # check if dropping a[l] removes a drop relation at l -> l+1
            if l + 1 < n and a[l] > a[l + 1]:
                drops -= 1
            l += 1
            
        max_len = max(max_len, r - l + 1)
        
    print(max_len)

if __name__ == "__main__":
    solve()
