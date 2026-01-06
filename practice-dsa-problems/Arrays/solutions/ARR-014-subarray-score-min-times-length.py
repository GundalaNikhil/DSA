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

    left = [-1] * n
    right = [n] * n
    
    # Previous Less Element Index
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
        
    # Next Less Element Index
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
        
    max_score = -float("inf")
    for i in range(n):
        # Length of range (left[i], right[i]) exclusive
        # i.e. indices left[i]+1 to right[i]-1
        length = (right[i] - 1) - (left[i] + 1) + 1
        # simpler: right[i] - left[i] - 1
        
        score = a[i] * length
        max_score = max(max_score, score)
        
    print(max_score)

if __name__ == "__main__":
    solve()
