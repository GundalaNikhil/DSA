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
   
    
    counts = {}
    b = []
    
    for x in a:
        k = counts.get(x, 0) + 1
        counts[x] = k
        
        # Calculate decay
        val = x
        # decay loop
        for _ in range(k - 1):
            val = (val * 90) // 100
        b.append(val)
        
    # Max Subarray Sum of b
    # Kadane's Algorithm
    max_sum = -float("inf")
    curr_sum = 0
    
    # Handle empty array case? n can be 0.
    if not b:
        print(0)
        return

  
    for x in b:
        curr_sum += x
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
            
    print(max_sum)

if __name__ == "__main__":
    solve()
