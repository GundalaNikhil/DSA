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

    if n < 2:
        print(n)
        return

    
    
    ans = 1
    if n > 0:
       
        # Iteration:
        curr = 1 # number of edges? or nodes? "Subarray length" is nodes.
        # If nodes, start with 1.
        
        last_dir = 0 # 0: none, 1: up, -1: down
        curr = 1 # Subarray length starts at 1
        
        for i in range(n - 1):
            diff = a[i+1] - a[i]
            if diff > 0:
                d = 1
            elif diff < 0:
                d = -1
            else:
                d = 0
                
            if d != 0:
                if last_dir == 0:
                     # First significant edge
                     curr = 2 # e.g. a -> b (len 2)
                     last_dir = d
                elif d != last_dir:
                     # Alternating
                     curr += 1
                     last_dir = d
                else: 
                     # Same direction
                     curr = 2 # Reset to 2 nodes (last edge)
                     last_dir = d
            else:
                # Equal values break zigzag (usually strictly alternating)
                curr = 1
                last_dir = 0
                
            ans = max(ans, curr)
            
    print(ans)

if __name__ == '__main__':
    solve()