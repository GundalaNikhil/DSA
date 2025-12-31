def can_achieve_target(nums: list[int], K: int, target: int) -> bool:
    n = len(nums)
    memo = {}

    def backtrack(index, current_sum, negations):
        if index == n:
            return current_sum == target
        if (index, current_sum, negations) in memo:
            return memo[(index, current_sum, negations)]
        
        if backtrack(index + 1, current_sum + nums[index], negations):
            memo[(index, current_sum, negations)] = True
            return True
        if negations < K and backtrack(index + 1, current_sum - nums[index], negations + 1):
            memo[(index, current_sum, negations)] = True
            return True
        memo[(index, current_sum, negations)] = False
        return False

    return backtrack(0, 0, 0)

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return
    first_line = lines[0].split()
    n = int(first_line[0])
    K = int(first_line[1])
    target = int(first_line[2])
    nums = list(map(int, lines[1].split()))
    result = can_achieve_target(nums, K, target)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
