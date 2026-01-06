import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    b = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        a.append(int(input_data[ptr]))
        ptr += 1
        
    memo = {}

    def get_batch(l, r):
        state = (l, r)
        if state in memo:
            return memo[state]
            
        size = r - l + 1
        if size <= b:
            window = a[l : r + 1]
            if not window:
                return 0
            res = max(window) - min(window)
            memo[state] = res
            return res
            
        max_res = -float("inf")
        # Divide into batches of size b?
        # Original: range(l, r+1, b) -> loop over chunks
        # Logic: find max result among sub-batches?
        # Recursively process chunks?
        
        # Original code called get_batch recursively on chunks.
        # But `res = get_batch(...)` inside loop, then `if res > max_res: max_res = res`.
        
        for start in range(l, r + 1, b):
            end = min(r, start + b - 1)
            # This recursion breaks down the range into small chunks.
            # If chunk size <= b, it calculates value.
            # So this effectively finds max (max-min) of any b-sized content?
            res = get_batch(start, end)
            if res > max_res:
                max_res = res
                
        memo[state] = max_res
        return max_res

    print(get_batch(0, n - 1))


if __name__ == "__main__":
    solve()
