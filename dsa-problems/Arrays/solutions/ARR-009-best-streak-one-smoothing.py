import sys
import math

def best_streak_with_smoothing(a: list[int]) -> int:
    n = len(a)
    if n < 3: return 0

    max_ending_at = [0] * n
    global_max_prefix = [0] * n

    # Forward
    max_ending_at[0] = a[0]
    global_max_prefix[0] = a[0]
    for i in range(1, n):
        max_ending_at[i] = max(a[i], max_ending_at[i-1] + a[i])
        global_max_prefix[i] = max(global_max_prefix[i-1], max_ending_at[i])

    max_starting_at = [0] * n
    global_max_suffix = [0] * n

    # Backward
    max_starting_at[n-1] = a[n-1]
    global_max_suffix[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        max_starting_at[i] = max(a[i], max_starting_at[i+1] + a[i])
        global_max_suffix[i] = max(global_max_suffix[i+1], max_starting_at[i])

    ans = -float('inf')

    for i in range(1, n-1):
        smoothed_val = math.floor((a[i-1] + a[i] + a[i+1]) / 3)

        left_part = max(0, max_ending_at[i-1])
        right_part = max(0, max_starting_at[i+1])
        cross_sum = left_part + smoothed_val + right_part

        global_left = global_max_prefix[i-1]
        global_right = global_max_suffix[i+1]

        current_best = max(cross_sum, global_left, global_right)
        ans = max(ans, current_best)

    return ans

def main():
    n = int(input())
    a = list(map(int, input().split()))

    result = best_streak_with_smoothing(a)
    print(result)

if __name__ == "__main__":
    main()

