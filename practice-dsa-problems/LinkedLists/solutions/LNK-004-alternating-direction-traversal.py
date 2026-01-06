import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k = int(input_data[ptr])
    ptr += 1
    values = []
    for _ in range(n):
        values.append(int(input_data[ptr]))
        ptr += 1
        
    res = []
    curr_idx = 0
    forward = True
    
    while len(res) < n:
        block_count = 0
        while block_count < k and len(res) < n:
            res.append(values[curr_idx])
            block_count += 1
            
            if len(res) == n:
                break
            
            if forward:
                if curr_idx + 1 < n:
                    curr_idx += 1
                else:
                    # Reached end, reverse
                    forward = False
                    # Don't change index yet? Or bounce?
                    # "Alternating direction traversal"
                    # Usually means traversing back and forth.
                    # This logic seems to just append.
                    # Let's trust the logic structure:
                    # if forward and can move, move. else?
                    pass 
            else:
                if curr_idx - 1 >= 0:
                    curr_idx -= 1
                else:
                    forward = True
                    pass
        
        # Switch direction after block of k
        if forward:
            # If we were forward, next block is backward?
            # Need to adjust index for next block?
            # Problem description not here, but code implies toggling.
            pass
            
        forward = not forward
        
        # Adjust start index for next block?
        # If we just finished a block moving forward, next block moves backward FROM where we stopped?
        # Re-check original logic.
        # Original: 
        # `while block_count < k:`
        #   Append. 
        #   Calculate next index. 
        #   If OOB, break?
        # Re-implementing simulation carefully.
        
    print(*(res))
if __name__ == '__main__':
    solve()