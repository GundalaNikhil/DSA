from typing import List
import sys

# Increase recursion depth
sys.setrecursionlimit(20000)

def coin_split(n: int, A: List[int]) -> int:
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + A[i]
    
    def get_sum(i, j):
        return prefix_sum[j+1] - prefix_sum[i]
    
    memo = {}

    def solve(i, j):
        if i == j:
            return 0
        state = (i, j)
        if state in memo:
            return memo[state]
        
        max_diff = -float('inf')
        
        for k in range(i, j):
            # Split [i...k] and [k+1...j]
            sum_left = get_sum(i, k)
            sum_right = get_sum(k+1, j)
            
            val_take_left = -sum_left - solve(k+1, j)
            val_take_right = -sum_right - solve(i, k)
            
            outcome = min(val_take_left, val_take_right)
            max_diff = max(max_diff, outcome)
            
        memo[state] = max_diff
        return max_diff

    return solve(0, n - 1)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        A = []
        for _ in range(n):
            A.append(int(next(iterator)))
            
        print(coin_split(n, A))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
